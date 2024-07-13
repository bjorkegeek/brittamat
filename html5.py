# -*- coding: utf-8 -*-

import alg
from html import escape
from babel.numbers import format_decimal


def shopping_list_to_html5(shopping_list, outputfile):
    print(
        '<html><head><link rel="stylesheet" href="shopping.css"/><meta http-equiv="content-type" content="text/html; charset=UTF-8" /></head>',
        file=outputfile,
    )
    print("<body>", file=outputfile)
    for cat, ingredients in sorted(alg.order_by_category(shopping_list)):
        print("<h1>" + escape(cat) + "</h1>", file=outputfile)
        print('<table class="tbl">', file=outputfile)
        print("  <thead>", file=outputfile)
        print(
            '    <tr><th></th><th colspan="2" class="amt">Mängd</th><th class="ingredient">Ingrediens</th><th class="sources">Till</th></tr>',
            file=outputfile,
        )
        print("  </thead>", file=outputfile)
        print("  <tbody>", file=outputfile)
        for ingredient in sorted(ingredients):
            print("  <tr>", file=outputfile)
            print("    <td>&#x25a2;</td>", file=outputfile)
            if ingredient.quantity:
                formatst = "%.1f"
                print(
                    '    <td class="numeric amt-magnitude">'
                    + format_decimal(
                        round(ingredient.quantity.magnitude, 2), locale="sv_SE"
                    )
                    + "</td>",
                    file=outputfile,
                )
                print(
                    '    <td class="amt-unit">'
                    + escape(alg.translate_unit(str(ingredient.quantity.units)))
                    + "</td>",
                    file=outputfile,
                )
            else:
                print('    <td colspan="2"></td>', file=outputfile)
            print(
                '    <td class="ingredient">' + escape(ingredient.name) + "</td>",
                file=outputfile,
            )
            print(
                '    <td class="sources">'
                + escape(", ".join([x.dish.name for x in ingredient.sources]))
                + "</td>",
                file=outputfile,
            )
            print("  </tr>", file=outputfile)
        print("  </tbody>", file=outputfile)
        print("</table>", file=outputfile)
    print("</body></html>", file=outputfile)
