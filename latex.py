import alg
import locale

CHARS = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\letterunderscore{}",
    "{": r"\letteropenbrace{}",
    "}": r"\letterclosebrace{}",
    "~": r"\lettertilde{}",
    "^": r"\letterhat{}",
    "\\": r"\letterbackslash{}",
}


def escape(st):
    return "".join([CHARS.get(x, x) for x in st])


def shopping_list_to_latex(shopping_list, outputfile):
    print(
        r"""\documentclass[a4paper,swedish]{article}
\usepackage[utf8]{inputenc}
\usepackage{babel}
\begin{document}""",
        file=outputfile,
    )
    for cat, ingredients in sorted(alg.order_by_category(shopping_list)):
        print("\\clearpage\\section*{" + escape(cat) + "}", file=outputfile)
        print("\\begin{tabular}{r@{ }l l}", file=outputfile)
        for ingredient in sorted(ingredients):
            if ingredient.quantity:
                formatst = "%.1f"
                print(
                    locale.format(formatst, ingredient.quantity.magnitude),
                    "&",
                    end=" ",
                    file=outputfile,
                )
                print(
                    escape(alg.translate_unit(str(ingredient.quantity.units))),
                    "&",
                    end=" ",
                    file=outputfile,
                )
                print(escape(ingredient.name), "\\\\", file=outputfile)
            else:
                print("& &", escape(ingredient.name), "\\\\", file=outputfile)
        print("\\end{tabular}", file=outputfile)
    print(r"""\end{document}""", file=outputfile)
