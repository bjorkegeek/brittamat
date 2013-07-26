#!/usr/bin/python
# -*- coding: utf-8 -*-

import alg
import data
import locale
import latex
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
    with codecs.open("shopping.tex","w","utf-8") as f:
        latex.shopping_list_to_latex(shopping_list,f)
        
if __name__ == "__main__":
    main()
 
