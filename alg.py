import classes
import operator
import itertools
import pint
import re
import data

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def to_purchase_unit(ingredient, ingredient_types):
    it = ingredient_types[ingredient.name]
    if ingredient.quantity is None and it.purchase_unit is None:
        return None

    try:
        conversions = it.conversions
    except AttributeError:
        conversions = []
    for subconversions, op in itertools.product(powerset(conversions), (operator.mul, operator.div)):
        try:
            v = ingredient.quantity
            for conversion in subconversions:
                v = op(v, conversion)
            return v.to(it.purchase_unit)
        except pint.unit.DimensionalityError:
            pass
    raise ValueError(u"Could not convert %s from %s to %s" % (it.name,ingredient.quantity,it.purchase_unit))

_translate_re = re.compile("|".join([re.escape(fr) for fr,to in data.translations]))
_translate_dict = dict(data.translations)

def translate_unit(unit_string):
    return _translate_re.sub(lambda x: _translate_dict[x.group(0)], unit_string)
    

def find_undefined_ingredients(menu, ingredient_types):
    not_found = set()
    for menuitem in menu:
        ingredients = list(menuitem.dish.ingredients)
        for variant in menuitem.variants.iterkeys():
            try:
                ingredients.extend(menuitem.dish.variants[variant])
            except KeyError:
                print variant, menuitem.dish.name
                raise ValueError(u"Missing variant '%s' for dish '%s'" %\
                                     (variant, menuitem.dish.name))

        for ingredient in ingredients:
            if ingredient.name not in ingredient_types:
                not_found.add(ingredient)
    return not_found

def make_shopping_list(menu, ingredient_types):
    shopping_list = classes.NameDict()
    for menuitem in menu:
        ingredients = zip(menuitem.dish.ingredients, itertools.repeat(1))
        for variant, count in menuitem.variants.iteritems():
            ingredients.extend(zip(menuitem.dish.variants[variant], itertools.repeat(count)))
        for ingredient, count in ingredients:
            pu = to_purchase_unit(ingredient, ingredient_types)
            if not pu is None:
                pu *= count

            entry = shopping_list.get(ingredient.name)
            if entry:
                if not pu is None:
                    entry.quantity += pu
                    entry.sources.append(menuitem)
            else:
                entry = classes.Ingredient(ingredient_types[ingredient.name])
                entry.quantity = pu
                entry.sources = [menuitem]
                shopping_list.append(entry)
    return shopping_list.values()

def subtract_from_shopping_list(shopping_list, sub, ingredient_types):
    subd = classes.NameDict(sub)
    for ingredient in shopping_list:
        sub_ingredient = subd.get(ingredient.name, None)
        if sub_ingredient is None:
            yield ingredient
        else:
            # Copy
            ing = classes.Ingredient(ingredient)
            pu = to_purchase_unit(sub_ingredient, ingredient_types)
            ing.quantity -= pu
            if ing.quantity and ing.quantity.magnitude>0:
                yield ing

def order_by_category(shopping_list):
    cats = {}
    for item in shopping_list:
        cats.setdefault(item.category, []).append(item)
    
    for x in sorted(cats.iteritems()):
        yield x
