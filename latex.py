import alg
import locale

CHARS = {
    '&':  r'\&',
    '%':  r'\%', 
    '$':  r'\$', 
    '#':  r'\#', 
    '_':  r'\letterunderscore{}', 
    '{':  r'\letteropenbrace{}', 
    '}':  r'\letterclosebrace{}',
    '~':  r'\lettertilde{}', 
    '^':  r'\letterhat{}', 
    '\\': r'\letterbackslash{}',
}

def escape(st):
    return "".join([CHARS.get(x,x) for x in st])

def shopping_list_to_latex(shopping_list, outputfile):
    print >>outputfile, r"""\documentclass[a4paper,swedish]{article}
\usepackage[utf8]{inputenc}
\usepackage{babel}
\begin{document}"""
    for cat, ingredients in sorted(alg.order_by_category(shopping_list)):
        print >>outputfile, "\\clearpage\\section*{" + escape(cat)+ "}"
        print >>outputfile, "\\begin{tabular}{r@{ }l l}"
        for ingredient in sorted(ingredients):
            if ingredient.quantity:
                formatst = "%.1f"
                print >>outputfile,locale.format(formatst,ingredient.quantity.magnitude),"&",
                print >>outputfile,escape(alg.translate_unit(unicode(ingredient.quantity.units))),"&",
                print >>outputfile,escape(ingredient.name),"\\\\"
            else:
                print >>outputfile,"& &",escape(ingredient.name),"\\\\"
        print >>outputfile, "\\end{tabular}"
    print >>outputfile, r"""\end{document}"""