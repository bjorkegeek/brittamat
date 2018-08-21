#!/usr/bin/python
# -*- coding: utf-8 -*-

import alg
import data
import html5
import codecs

def main():    
    found_undef = False
    menu = data.menu
    
    for ingredient in alg.find_undefined_ingredients(menu, data.ingredient_types):
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

    for i, menu_item in enumerate(menu):
        if menu_item.dish.name == u"Porterstek":
            menu[i].dish = alg.scaled_dish(menu[i].dish, 28.0/36.0) # scale to amouont of people on change day
        elif menu_item.dish.name == u"Extras":
            pass # do not scale extras
        else:
            menu[i].dish = alg.scaled_dish(menu[i].dish, 24.0/36.0) # scale to amount of poeple on other days

    shopping_list = alg.make_shopping_list(menu, data.ingredient_types)
    
    with codecs.open("all-ingredients.html","w","utf-8") as f:
        html5.shopping_list_to_html5(shopping_list,f)

    shopping_list = alg.subtract_from_shopping_list(shopping_list, data.prebought, data.ingredient_types)
    shopping_list = alg.subtract_from_shopping_list(shopping_list, data.buy_later, data.ingredient_types)
    with codecs.open("shopping.html","w","utf-8") as f:
        html5.shopping_list_to_html5(shopping_list,f)    
                
if __name__ == "__main__":
    main()
    #try:
    #    main()
    #except Exception as e:
    #    print unicode(e).encode("utf-8")
