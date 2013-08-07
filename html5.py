# -*- coding: utf-8 -*-

import alg
from cgi import escape
from babel.numbers import format_decimal

def shopping_list_to_html5(shopping_list, outputfile):
    print >>outputfile, u'<html><head><link rel="stylesheet" href="shopping.css"/><meta http-equiv="content-type" content="text/html; charset=UTF-8" /></head>'
    print >>outputfile, u'<body>'
    for cat, ingredients in sorted(alg.order_by_category(shopping_list)):
        print >>outputfile, u'<h1>' + escape(cat) + u'</h1>'
        print >>outputfile, u'<table class="tbl">'
        print >>outputfile, u'  <thead>'
        print >>outputfile, u'    <tr><th colspan="2">Mängd</th><th>Ingrediens</th><th>Till</th></tr>'
        print >>outputfile, u'  </thead>'
        print >>outputfile, u'  <tbody>'
        for ingredient in sorted(ingredients):
            print >>outputfile, u'  <tr>'
            if ingredient.quantity:
                print >>outputfile,u'    <td class="numeric">' + format_decimal(ingredient.quantity.magnitude, locale='sv_SE') + '</td>'
                print >>outputfile,u'    <td>' + escape(alg.translate_unit(unicode(ingredient.quantity.units))) + '</td>'
            else:
                print >>outputfile,u'    <td colspan="2"></td>'
            print >>outputfile,u'    <td>' + escape(ingredient.name) + '</td>'
            print >>outputfile,u'    <td class="sources">' + escape(", ".join([x.dish.name for x in ingredient.sources])) + '</td>'
            print >>outputfile, u'  </tr>'
        print >>outputfile, u'  </tbody>'
        print >>outputfile, u'</table>'
    print >>outputfile, u'</body></html>'
