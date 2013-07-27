#!/usr/bin/python
# -*- coding: utf-8 -*-

import alg
import data
import locale
import html5
import codecs

def main():
    locale.setlocale(locale.LC_ALL, 'sv_SE')
    found_undef = False
    for ingredient in alg.find_undefined_ingredients(data.menu, data.ingredient_types):
        if not found_undef:
            print "# Undefined ingredients:" 
            found_undef = True

        if ingredient.quantity is None:
            unt = "None"
        else:
            unt = "units."+str(ingredient.quantity.units)
        print u'    Ingredient(name=%r,purchase_unit=%s, category=u"fixme"),' %\
            (ingredient.name,unt)
    
    if found_undef:
        return

    shopping_list = alg.make_shopping_list(data.menu, data.ingredient_types)
    shopping_list = alg.subtract_from_shopping_list(shopping_list, data.prebought, data.ingredient_types)
    with codecs.open("shopping.html","w","utf-8") as f:
        html5.shopping_list_to_html5(shopping_list,f)
        
if __name__ == "__main__":
    main()
 
