# -*- coding: utf-8 -*-

from classes import Ingredient, Dish, MenuItem, NameDict, IngredientType
from wrapped_unit_registry import WrappedUnitRegistry

units = WrappedUnitRegistry()

ingredient_types: NameDict[IngredientType] = NameDict(
    [
        IngredientType(
            name="Oliver, svarta",
            purchase_unit=units.kilograms,
            category="burk",
            conversions=[657 * units.kilograms / units.meter**3],
        ),
        IngredientType(name="Olja, oliv", purchase_unit=units.liter, category="burk"),
        IngredientType(name="Olja, raps", purchase_unit=units.liter, category="burk"),
        IngredientType(
            name="Krossade tomater", purchase_unit=units.kilograms, category="burk"
        ),
        IngredientType(
            name="Matlagningsvin, vitt", purchase_unit=units.litres, category="burk"
        ),
        IngredientType(
            name="Tomatpuré",
            purchase_unit=units.kilograms,
            category="burk",
            conversions=[1 * units.cups / (8 * units.ounces)],
        ),
        IngredientType(
            name="Nyponsoppa Klassisk, pulver, färdig dryck",
            purchase_unit=units.liter,
            category="torr",
        ),
        IngredientType(
            name="Fransk senap",
            purchase_unit=units.grams,
            category="burk",
            conversions=[8.47 * units.ounce / (1 * units.cups)],
        ),
        IngredientType(
            name="Grovkornig senap",
            purchase_unit=units.grams,
            category="burk",
            conversions=[8.47 * units.ounce / (1 * units.cups)],
        ),
        IngredientType(name="Ketchup", purchase_unit=units.count, category="burk"),
        IngredientType(
            name="Sambal oelek",
            purchase_unit=units.grams,
            category="burk",
            conversions=[1 * units.cups / (8 * units.ounces)],
        ),
        IngredientType(
            name="Soya, kinesisk", purchase_unit=units.liter, category="burk"
        ),
        IngredientType(
            name="Majonäs, burk", purchase_unit=units.count, category="burk"
        ),
        IngredientType(
            name="Valnötter",
            purchase_unit=units.kilograms,
            category="torr",
            conversions=[1.1 * units.kilograms / (15 * units.deciliters)],
        ),
        IngredientType(name="Salt", purchase_unit=None, category="krydd"),
        IngredientType(name="Peppar, svart", purchase_unit=None, category="krydd"),
        IngredientType(name="Peppar, svart, hel", purchase_unit=None, category="krydd"),
        IngredientType(name="Basilika", purchase_unit=None, category="krydd"),
        IngredientType(name="Oregano", purchase_unit=None, category="krydd"),
        IngredientType(name="Timjan", purchase_unit=None, category="krydd"),
        IngredientType(name="Curry", purchase_unit=units.deciliters, category="krydd"),
        IngredientType(name="Salt, grov", purchase_unit=None, category="krydd"),
        IngredientType(
            name="Buljongtärning, fisk", purchase_unit=units.count, category="krydd"
        ),
        IngredientType(
            name="Buljongtärning, höns", purchase_unit=units.count, category="krydd"
        ),
        IngredientType(
            name="Buljongtärning, kött", purchase_unit=units.count, category="krydd"
        ),
        IngredientType(
            name="Buljongtärning, grönsak", purchase_unit=units.count, category="krydd"
        ),
        IngredientType(
            name="Pasta, skruvar", purchase_unit=units.kilograms, category="torr"
        ),
        IngredientType(
            name="Socker",
            purchase_unit=units.kilograms,
            category="torr",
            conversions=[1 * units.deciliters / (88 * units.grams)],
        ),
        IngredientType(
            name="Ris, parboiled",
            purchase_unit=units.kilograms,
            category="torr",
            conversions=[0.9 * units.grams / units.cm**3],
        ),
        IngredientType(
            name="Ris, fullkorn",
            purchase_unit=units.kilograms,
            category="torr",
            conversions=[0.9 * units.grams / units.cm**3],
        ),
        IngredientType(
            name="Vitlöksklyftor",
            purchase_unit=units.grams,
            category="grönt",
            conversions=[6 * units.grams / units.count],
        ),
        IngredientType(
            name="Apelsiner",
            purchase_unit=units.kilograms,
            category="grönt",
            conversions=[200 * units.grams / units.count],
        ),
        IngredientType(name="Fänkål", purchase_unit=units.kilograms, category="grönt"),
        IngredientType(
            name="Lök, gul",
            purchase_unit=units.kilograms,
            category="grönt",
            conversions=[100 * units.grams / units.count],
        ),
        IngredientType(
            name="Morötter",
            purchase_unit=units.kilograms,
            category="grönt",
            conversions=[70 * units.grams / units.count],
        ),
        IngredientType(name="Rotselleri", purchase_unit=units.count, category="grönt"),
        IngredientType(name="Palsternacka", purchase_unit=units.gram, category="grönt"),
        IngredientType(name="Purjolök", purchase_unit=units.gram, category="grönt"),
        IngredientType(
            name="Potatis",
            purchase_unit=units.kilograms,
            category="grönt",
            conversions=[80 * units.gram / units.count],
        ),
        IngredientType(
            name="Dill, färsk, planta/motsv",
            purchase_unit=units.count,
            category="grönt",
        ),
        IngredientType(
            name="Ingefära, färsk", purchase_unit=units.grams, category="grönt"
        ),
        IngredientType(
            name="Salladshuvud", purchase_unit=units.count, category="grönt"
        ),
        IngredientType(
            name="Tomater",
            purchase_unit=units.kilograms,
            category="grönt",
            conversions=[115 * units.grams / units.count],
        ),
        IngredientType(name="Chili, grön", purchase_unit=units.count, category="grönt"),
        IngredientType(
            name="Chili, röd, stark", purchase_unit=units.count, category="grönt"
        ),
        IngredientType(
            name="Kycklingfilé", purchase_unit=units.kilograms, category="frys"
        ),
        IngredientType(name="Broccoli", purchase_unit=units.kilograms, category="frys"),
        IngredientType(
            name="Persilja, fryst", purchase_unit=units.count, category="frys"
        ),
        IngredientType(
            name="Fetaost", purchase_unit=units.kilograms, category="mejeri"
        ),
        IngredientType(
            name="Fetaost, laktosfri", purchase_unit=units.kilograms, category="mejeri"
        ),
        IngredientType(name="Mjölk", purchase_unit=units.liters, category="mejeri"),
        IngredientType(name="Gräddfil", purchase_unit=units.liters, category="mejeri"),
        IngredientType(
            name="Gräddfil, laktosfri", purchase_unit=units.liters, category="mejeri"
        ),
        IngredientType(
            name="Creme Fraiche", purchase_unit=units.liters, category="mejeri"
        ),
        IngredientType(
            name="Köttfärs, nöt", purchase_unit=units.kilograms, category="kyl"
        ),
        IngredientType(name="Falukorv", purchase_unit=units.kilograms, category="kyl"),
        IngredientType(name="Chilipulver, röd", purchase_unit=None, category="krydd"),
        IngredientType(
            name="Gurka",
            purchase_unit=units.kilograms,
            category="grönt",
            conversions=[463 * units.grams / units.count],
        ),
        IngredientType(name="Koriander, malen", purchase_unit=None, category="krydd"),
        IngredientType(
            name="Vetemjöl",
            purchase_unit=units.kilograms,
            category="torr",
            conversions=[60 * units.grams / units.deciliters],
        ),
        IngredientType(
            name="Kidneybönor, avrunnen vikt",
            purchase_unit=units.kilogram,
            category="torr",
        ),
        IngredientType(
            name="Koriander, färsk", purchase_unit=units.count, category="grönt"
        ),
        IngredientType(
            name="Persilja, färsk", purchase_unit=units.count, category="grönt"
        ),
        IngredientType(name="Gurkmeja", purchase_unit=None, category="krydd"),
        IngredientType(
            name="Vinbärsaft, outspädd, bra (typ Önos)",
            purchase_unit=units.liter,
            category="burk",
        ),
        IngredientType(
            name="Kikärtor, avrunnen vikt",
            purchase_unit=units.kilogram,
            category="torr",
        ),
        IngredientType(name="Porter", purchase_unit=units.liter, category="burk"),
        IngredientType(name="Citroner", purchase_unit=units.count, category="grönt"),
        IngredientType(
            name="Enbär, torkade", purchase_unit=units.gram, category="krydd"
        ),
        IngredientType(name="Grädde", purchase_unit=units.liter, category="mejeri"),
        IngredientType(name="Spiskummin", purchase_unit=None, category="krydd"),
        IngredientType(
            name="Högrev, benfri", purchase_unit=units.kilogram, category="kyl"
        ),
        IngredientType(name="Kassler", purchase_unit=units.kilogram, category="kyl"),
        IngredientType(
            name="Vinäger, vitvins", purchase_unit=units.liters, category="burk"
        ),
        IngredientType(
            name="Lök, röd",
            purchase_unit=units.kilogram,
            category="grönt",
            conversions=[100 * units.grams / units.count],
        ),
        IngredientType(
            name="Rädisor, knippe", purchase_unit=units.count, category="grönt"
        ),
        IngredientType(name="Prinskorvar", purchase_unit=units.count, category="kyl"),
        IngredientType(
            name="Sill, burk, blandat", purchase_unit=units.count, category="kyl"
        ),
        IngredientType(
            name="Knäckebröd, skivor",
            purchase_unit=units.grams,
            category="torr",
            conversions=[14 * units.grams / units.count],
        ),
        IngredientType(name="Ägg", purchase_unit=units.count, category="kyl"),
        IngredientType(name="Köttbullar", purchase_unit=units.kilogram, category="kyl"),
        IngredientType(name="Bacon", purchase_unit=units.kilogram, category="kyl"),
        IngredientType(
            name="Paprika, röd", purchase_unit=units.kilogram, category="grönt"
        ),
        IngredientType(name="Paprikapulver", purchase_unit=None, category="krydd"),
        IngredientType(
            name="Bröd, ljust, skivor", purchase_unit=units.count, category="torr"
        ),
        IngredientType(name="Grytkött", purchase_unit=units.kilogram, category="kyl"),
        IngredientType(name="Kolbasz", purchase_unit=units.kilogram, category="kyl"),
        IngredientType(
            name="Rödbetor till pytt-i-panna, portioner",
            purchase_unit=units.count,
            category="burk",
        ),
        IngredientType(
            name="Ärtsoppa på burk, portioner",
            purchase_unit=units.count,
            category="burk",
        ),
        IngredientType(
            name="Pytt i panna, portioner", purchase_unit=units.count, category="frys"
        ),
        IngredientType(
            name="Pytt i panna, vegetarisk, portioner",
            purchase_unit=units.count,
            category="frys",
        ),
        IngredientType(
            name="Grädde, laktosfri", purchase_unit=units.liter, category="mejeri"
        ),
        IngredientType(
            name="Grädde, mjölkfri", purchase_unit=units.liter, category="mejeri"
        ),
        IngredientType(
            name="Creme Fraiche, laktosfri",
            purchase_unit=units.liter,
            category="mejeri",
        ),
        IngredientType(
            name="Pasta, glutenfri, portioner",
            purchase_unit=units.count,
            category="torr",
        ),
        IngredientType(
            name="Mjölk, laktosfri", purchase_unit=units.liter, category="mejeri"
        ),
        IngredientType(
            name="Tofu, portioner", purchase_unit=units.count, category="kyl"
        ),
        IngredientType(name="Quornburgare", purchase_unit=units.count, category="frys"),
        IngredientType(name="Quornfiléer", purchase_unit=units.count, category="frys"),
        IngredientType(
            name="Sojakorvar, Hälsans kök", purchase_unit=units.count, category="frys"
        ),
        IngredientType(name="Kaffe", purchase_unit=units.kilogram, category="torr"),
        IngredientType(
            name="Diskmedel, flaska", purchase_unit=units.count, category="torr"
        ),
        IngredientType(
            name="Rotsaksborste", purchase_unit=units.count, category="torr"
        ),
        IngredientType(
            name="Brödbakningsmix", purchase_unit=units.count, category="torr"
        ),
        IngredientType(
            name="Plastfilm, typ gladpack", purchase_unit=units.count, category="torr"
        ),
        IngredientType(
            name="Sopsäckar, stora, rullar", purchase_unit=units.count, category="torr"
        ),
        IngredientType(
            name="Kaffefilter 1X4", purchase_unit=units.count, category="torr"
        ),
        IngredientType(
            name="Soppåsar mindre, rullar", purchase_unit=units.count, category="torr"
        ),
        IngredientType(
            name="Hushållspapper, rullar", purchase_unit=units.count, category="torr"
        ),
        IngredientType(
            name="Tändare med lång hals", purchase_unit=units.count, category="torr"
        ),
        IngredientType(name="Märkpenna", purchase_unit=units.count, category="torr"),
        IngredientType(name="Frystejp", purchase_unit=units.count, category="torr"),
        IngredientType(
            name="Plastpåsar, 3L, paket", purchase_unit=units.count, category="torr"
        ),
        IngredientType(name="Filmjölk", purchase_unit=units.liter, category="mejeri"),
        IngredientType(
            name="Korvpålägg, skivor", purchase_unit=units.count, category="kyl"
        ),
        IngredientType(
            name="Köttpålägg, skivor", purchase_unit=units.count, category="kyl"
        ),
        IngredientType(
            name="Cornflakes", purchase_unit=units.kilogram, category="torr"
        ),
        IngredientType(
            name="Jordgubbssylt", purchase_unit=units.kilogram, category="burk"
        ),
        IngredientType(name="Digestivekex", purchase_unit=units.count, category="torr"),
        IngredientType(
            name="Josextrakt, äpple (måttet är för färdigblandad jos)",
            purchase_unit=units.liter,
            category="burk",
        ),
        IngredientType(
            name="Havregryn (bara)", purchase_unit=units.kilogram, category="torr"
        ),
        IngredientType(
            name="Josextrakt, apelsin (måttet är för färdigblandad jos)",
            purchase_unit=units.liter,
            category="burk",
        ),
        IngredientType(
            name="Kakmix, chokladkaka", purchase_unit=units.count, category="torr"
        ),
        IngredientType(name="Marmelad", purchase_unit=units.kilogram, category="burk"),
        IngredientType(name="Russin", purchase_unit=units.kilogram, category="torr"),
        IngredientType(
            name="Ljust bröd (typ polar), skivor",
            purchase_unit=units.count,
            category="torr",
        ),
        IngredientType(name="Äppelmos", purchase_unit=units.kilogram, category="burk"),
        IngredientType(
            name="Mörkt bröd, skivor", purchase_unit=units.count, category="torr"
        ),
        IngredientType(name="Bröd, glutenfritt", purchase_unit=None, category="torr"),
        IngredientType(
            name="Frukt, blandad prisvärd",
            purchase_unit=units.kilogram,
            category="grönt",
        ),
        IngredientType(name="Mariekex", purchase_unit=units.count, category="torr"),
        IngredientType(name="Müsli", purchase_unit=units.kilogram, category="torr"),
        IngredientType(
            name="Paprika, valfri", purchase_unit=units.kilogram, category="grönt"
        ),
        IngredientType(
            name="Skorpor, kardemumma", purchase_unit=units.kilogram, category="torr"
        ),
        IngredientType(
            name="Skorpor, grova", purchase_unit=units.kilogram, category="torr"
        ),
        IngredientType(name="Tepåsar", purchase_unit=units.count, category="torr"),
        IngredientType(name="Kanel", purchase_unit=None, category="krydd"),
        IngredientType(name="Bregott", purchase_unit=units.kilogram, category="mejeri"),
        IngredientType(
            name="Färdigrätt, åt Hannah H E", purchase_unit=units.count, category="frys"
        ),
        IngredientType(
            name="Filmjölk, laktosfri", purchase_unit=units.liter, category="mejeri"
        ),
        IngredientType(
            name="Yoghurt, laktosfri", purchase_unit=units.liter, category="mejeri"
        ),
        IngredientType(
            name="Knäckebröd, glutenfritt, skivor",
            purchase_unit=units.count,
            category="torr",
        ),
        IngredientType(
            name="Pasta, Penne", purchase_unit=units.kilogram, category="torr"
        ),
        IngredientType(
            name="Cirtronjuice", purchase_unit=units.deciliter, category="burk"
        ),
        IngredientType(name="Lax", purchase_unit=units.gram, category="kyl"),
        IngredientType(
            name="Fisk (kolja, sej)", purchase_unit=units.gram, category="frys"
        ),
        IngredientType(
            name="Ris, basmati",
            purchase_unit=units.kilograms,
            category="torr",
            conversions=[0.9 * units.grams / units.cm**3],
        ),
        IngredientType(
            name="Sojamjölk",
            purchase_unit=units.liters,
            category="mejeri",
        ),
        IngredientType(
            name="Hollandaise, mjölkfri",
            purchase_unit=units.grams,
            category="kyl",
        ),
        IngredientType(
            name="Mjölkfri Creme Fraiche",
            purchase_unit=units.milliliters,
            category="mejeri",
        ),
        IngredientType(
            name="Smör, normalsaltat 80%", purchase_unit=units.grams, category="mejeri"
        ),
        IngredientType(name="Sojamjölk", purchase_unit=units.liters, category="mejeri"),
        IngredientType(
            name="Maizena, ej ljus/mörk", purchase_unit=None, category="torr"
        ),
        IngredientType(
            name="Ost mild", purchase_unit=units.kilogram, category="mejeri"
        ),
        IngredientType(
            name="Ost med smak", purchase_unit=units.kilogram, category="mejeri"
        ),
        IngredientType(
            name="Vegetarisk ärtsoppa burk", purchase_unit=units.count, category="burk"
        ),
        IngredientType(name="Sirap, ljus", purchase_unit=units.grams, category="burk"),
        IngredientType(
            name="Bladspenat", purchase_unit=units.kilogram, category="grönt"
        ),
        IngredientType(name="Lime", purchase_unit=units.count, category="grönt"),
        IngredientType(
            name="Jordnötssmör, crunchy",
            purchase_unit=units.grams,
            category="burk",
            conversions=[1092 * units.kilograms / units.meter**3],
        ),
        IngredientType(name="Mjölkchoklad", purchase_unit=units.gram, category="torr"),
        IngredientType(
            name="Laktosfritt smör", purchase_unit=units.grams, category="torr"
        ),
        IngredientType(name="Farinsocker", purchase_unit=None, category="torr"),
        IngredientType(name="Sesamfrön", purchase_unit=None, category="krydd"),
        IngredientType(
            name="Kikärtor, okokta", purchase_unit=units.kilogram, category="torr"
        ),
        IngredientType(name="Sriracha", purchase_unit=None, category="burk"),
    ]
)

dishes: NameDict[Dish] = NameDict(
    [
        Dish(
            name="Fänkål och kycklingsallad",
            ingredients=[
                Ingredient(name="Fänkål", quantity=7.2 * units.kilograms),
                Ingredient(name="Kycklingfilé", quantity=3.6 * units.kilograms),
                Ingredient(name="Fetaost", quantity=2.2 * units.kilograms),
                Ingredient(name="Valnötter", quantity=15 * units.deciliters),
                Ingredient(name="Oliver, svarta", quantity=15 * units.deciliters),
                Ingredient(name="Apelsiner", quantity=18 * units.count),
                Ingredient(name="Cirtronjuice", quantity=7 * units.deciliters),
                Ingredient(name="Olja, oliv", quantity=6 * units.deciliters),
                Ingredient(name="Salt", quantity=None),
                Ingredient(name="Peppar, svart", quantity=None),
            ],
            variants={
                "vegetarian": [
                    Ingredient(name="Quornfiléer", quantity=1 * units.count)
                ],
                "laktosfri": [
                    Ingredient(name="Fetaost, laktosfri", quantity=55 * units.gram)
                ],
            },
        ),
        Dish(
            name="Kycklinggryta med fetaost",
            ingredients=[
                Ingredient(name="Olja, raps", quantity=1.6 * units.deciliters),
                Ingredient(name="Vitlöksklyftor", quantity=8 * units.count),
                Ingredient(name="Kycklingfilé", quantity=5 * units.kilogram),
                Ingredient(name="Krossade tomater", quantity=24 * 400 * units.gram),
                Ingredient(name="Buljongtärning, höns", quantity=16 * units.count),
                Ingredient(name="Matlagningsvin, vitt", quantity=12 * units.deciliters),
                Ingredient(name="Peppar, svart", quantity=None),
                Ingredient(name="Broccoli", quantity=2 * units.kilogram),
                Ingredient(name="Fetaost", quantity=1.6 * units.kilogram),
                Ingredient(name="Basilika", quantity=None),
                Ingredient(name="Salt", quantity=None),
                Ingredient(name="Pasta, Penne", quantity=5 * units.kilogram),
            ],
            variants={
                "vegetarian": [
                    Ingredient(name="Quornfiléer", quantity=2 * units.count),
                    Ingredient(
                        name="Buljongtärning, grönsak", quantity=0.5 * units.count
                    ),
                ],
                "glutenfri": [
                    Ingredient(
                        name="Pasta, glutenfri, portioner", quantity=1 * units.count
                    )
                ],
                "mjölkfri": [],
                "laktosfri": [
                    Ingredient(name="Fetaost, laktosfri", quantity=45 * units.gram)
                ],
            },
        ),
        Dish(
            name="Pasta & köttfärssås",
            ingredients=[
                Ingredient(name="Lök, gul", quantity=15 * units.count),
                Ingredient(name="Morötter", quantity=15 * units.count),
                Ingredient(name="Rotselleri", quantity=3 * units.count),
                Ingredient(name="Vitlöksklyftor", quantity=10 * units.count),
                Ingredient(name="Köttfärs, nöt", quantity=5 * units.kilogram),
                Ingredient(name="Buljongtärning, kött", quantity=6 * units.count),
                Ingredient(name="Peppar, svart", quantity=None),
                Ingredient(name="Oregano", quantity=None),
                Ingredient(name="Timjan", quantity=None),
                Ingredient(name="Basilika", quantity=None),
                Ingredient(name="Krossade tomater", quantity=20 * 400 * units.gram),
                Ingredient(name="Tomatpuré", quantity=3 * units.deciliters),
                Ingredient(name="Pasta, skruvar", quantity=5 * units.kilograms),
            ],
            variants={
                "glutenfri": [
                    Ingredient(
                        name="Pasta, glutenfri, portioner", quantity=1 * units.count
                    )
                ],
                "vegetarian": [
                    Ingredient(name="Quornburgare", quantity=1 * units.count),
                    Ingredient(
                        name="Buljongtärning, grönsak", quantity=0.5 * units.count
                    ),
                ],
            },
        ),
        Dish(
            name="Korv stroganoff",
            ingredients=[
                Ingredient(name="Falukorv", quantity=5 * units.kilogram),
                Ingredient(name="Lök, gul", quantity=20 * units.count),
                Ingredient(name="Tomatpuré", quantity=6 * units.deciliters),
                Ingredient(name="Fransk senap", quantity=1.5 * units.deciliters),
                Ingredient(name="Mjölk", quantity=2.5 * units.liters),
                Ingredient(name="Buljongtärning, grönsak", quantity=4 * units.count),
                Ingredient(name="Creme Fraiche", quantity=3 * units.liters),
                Ingredient(name="Ketchup", quantity=0.5 * units.count),
                Ingredient(name="Sambal oelek", quantity=4 * units.tablespoons),
                Ingredient(name="Socker", quantity=2.5 * units.deciliters),
                Ingredient(name="Soya, kinesisk", quantity=3 * units.deciliters),
                Ingredient(name="Vitlöksklyftor", quantity=1 * units.ounce),
                Ingredient(name="Peppar, svart", quantity=None),
                Ingredient(name="Salt", quantity=None),
                Ingredient(name="Timjan", quantity=None),
                Ingredient(name="Olja, raps", quantity=1 * units.deciliters),
                Ingredient(name="Ris, parboiled", quantity=3 * units.kilogram),
            ],
            variants={
                "laktosfri": [
                    Ingredient(name="Mjölk, laktosfri", quantity=1 * units.deciliters),
                    Ingredient(
                        name="Creme Fraiche, laktosfri", quantity=0.5 * units.deciliters
                    ),
                ],
                "vegetarian": [
                    Ingredient(name="Sojakorvar, Hälsans kök", quantity=4 * units.count)
                ],
                "mjölkfri": [
                    Ingredient(name="Sojamjölk", quantity=1 * units.deciliters),
                    Ingredient(
                        name="Mjölkfri Creme Fraiche", quantity=0.5 * units.deciliters
                    ),
                ],
            },
        ),
        Dish(
            name="Fisksoppa",
            ingredients=[
                Ingredient(name="Fisk (kolja, sej)", quantity=5.5 * units.kilograms),
                Ingredient(name="Potatis", quantity=3 * units.kilograms),
                Ingredient(name="Morötter", quantity=2 * units.kilograms),
                Ingredient(name="Palsternacka", quantity=1.2 * units.kilograms),
                Ingredient(name="Buljongtärning, fisk", quantity=18 * units.count),
                Ingredient(name="Socker", quantity=1.5 * units.deciliters),
                Ingredient(name="Purjolök", quantity=2 * units.kilograms),
                Ingredient(name="Vetemjöl", quantity=2.5 * units.deciliters),
                Ingredient(name="Persilja, färsk", quantity=2 * units.count),
                Ingredient(name="Curry", quantity=0.5 * units.deciliters),
                Ingredient(name="Salt, grov", quantity=None),
                Ingredient(name="Peppar, svart", quantity=None),
                Ingredient(name="Creme Fraiche", quantity=2 * units.liters),
            ],
            variants={
                "vegan": [
                    Ingredient(
                        name="Vegetarisk ärtsoppa burk", quantity=1 * units.count
                    )
                ],
                "laktosfri": [
                    Ingredient(
                        name="Gräddfil, laktosfri", quantity=1 * units.deciliters
                    )
                ],
                "vegetarian": [],
                "glutenfri": [Ingredient(name="Maizena, ej ljus/mörk", quantity=None)],
            },
        ),
        Dish(
            name="Ärtsoppa",
            ingredients=[
                Ingredient(
                    name="Ärtsoppa på burk, portioner", quantity=40 * units.count
                ),
                Ingredient(name="Grovkornig senap", quantity=40 * 25 * units.grams),
                Ingredient(
                    name="Ljust bröd (typ polar), skivor",
                    quantity=40 * 1.5 * units.count,
                ),
            ],
            variants={
                "vegetarian": [
                    Ingredient(
                        name="Vegetarisk ärtsoppa burk", quantity=1 * units.count
                    )
                ]
            },
        ),
        Dish(
            name="Lax",
            ingredients=[
                Ingredient(name="Salt, grov", quantity=None),
                Ingredient(name="Majonäs, burk", quantity=2 * units.count),
                Ingredient(name="Persilja, fryst", quantity=1 * units.count),
                Ingredient(name="Peppar, svart", quantity=None),
                Ingredient(name="Timjan", quantity=None),
                Ingredient(name="Potatis", quantity=16 * units.kilograms),
                Ingredient(name="Dill, färsk, planta/motsv", quantity=4 * units.count),
                Ingredient(name="Gräddfil", quantity=3 * units.liters),
                Ingredient(name="Lax", quantity=150 * 1.10 * 36 * units.gram),
            ],
            variants={
                "vegan": [
                    Ingredient(
                        name="Vegetarisk ärtsoppa burk", quantity=1 * units.count
                    )
                ],
                "laktosfri": [
                    Ingredient(
                        name="Gräddfil, laktosfri", quantity=1 * units.deciliters
                    )
                ],
                "mjölkfri": [
                    Ingredient(name="Hollandaise, mjölkfri", quantity=50 * units.grams)
                ],
            },
        ),
        Dish(
            name="2 x Indisk curry",
            ingredients=[
                Ingredient(
                    name="Kidneybönor, avrunnen vikt",
                    quantity=1.4 * 500 / 255 * units.kilograms,
                ),
                Ingredient(name="Lök, gul", quantity=20 * units.count),
                Ingredient(name="Tomater", quantity=(10 + 10) * units.count),
                Ingredient(name="Chili, grön", quantity=10 * units.count),
                Ingredient(name="Vitlöksklyftor", quantity=10 * units.count),
                Ingredient(name="Olja, raps", quantity=(4 + 6) * units.deciliters),
                Ingredient(name="Gurkmeja", quantity=None),
                Ingredient(name="Ingefära, färsk", quantity=200 * units.grams),
                Ingredient(name="Koriander, färsk", quantity=4 * units.count),
                Ingredient(
                    name="Kikärtor, avrunnen vikt",
                    quantity=1.2 * 500 / 255 * units.kilograms,
                ),
                Ingredient(name="Spiskummin", quantity=None),
                Ingredient(name="Chilipulver, röd", quantity=None),
                Ingredient(name="Koriander, malen", quantity=None),
                Ingredient(name="Citroner", quantity=3 * units.count),
                Ingredient(name="Ris, basmati", quantity=6 * units.liters),
            ],
            variants={
                "vegetarian": [],
                "laktosfri": [],
            },
        ),
        Dish(
            name="Porterstek",
            ingredients=[
                Ingredient(name="Högrev, benfri", quantity=10 * units.kilograms),
                Ingredient(name="Porter", quantity=10 * 33 * units.centiliters),
                Ingredient(
                    name="Vinbärsaft, outspädd, bra (typ Önos)",
                    quantity=0.5 * units.liters,
                ),
                Ingredient(name="Soya, kinesisk", quantity=3 * units.liters),
                Ingredient(name="Timjan", quantity=None),
                Ingredient(name="Enbär, torkade", quantity=8 * units.grams),
                Ingredient(name="Peppar, svart, hel", quantity=None),
                Ingredient(name="Buljongtärning, kött", quantity=25 * units.count),
                Ingredient(name="Vitlöksklyftor", quantity=20 * units.count),
                Ingredient(name="Lök, gul", quantity=10 * units.count),
                Ingredient(name="Vetemjöl", quantity=3.75 * units.deciliters),
                Ingredient(name="Grädde", quantity=1 * units.liters),
                Ingredient(name="Potatis", quantity=16 * units.kilograms),
                Ingredient(name="Salladshuvud", quantity=6 * units.count),
                Ingredient(name="Gurka", quantity=5 * units.count),
                Ingredient(name="Tomater", quantity=10 * units.count),
            ],
            variants={
                "laktosfri": [
                    Ingredient(name="Grädde, laktosfri", quantity=1 * units.deciliters)
                ],
                "mjölkfri": [
                    Ingredient(name="Grädde, mjölkfri", quantity=1 * units.deciliters)
                ],
                "vegetarian": [
                    Ingredient(name="Quornfiléer", quantity=2 * units.count),
                    Ingredient(
                        name="Buljongtärning, grönsak", quantity=0.5 * units.count
                    ),
                ],
                "glutenfri": [Ingredient(name="Maizena, ej ljus/mörk", quantity=None)],
            },
        ),
        Dish(
            name="Kassler med potatissallad",
            ingredients=[
                Ingredient(name="Potatis", quantity=13 * units.kilograms),
                Ingredient(name="Lök, röd", quantity=13 * units.count),
                Ingredient(name="Rädisor, knippe", quantity=13 * units.count),
                Ingredient(name="Salt", quantity=None),
                Ingredient(name="Kassler", quantity=5 * units.kilograms),
                Ingredient(name="Vinäger, vitvins", quantity=2 * units.deciliters),
                Ingredient(name="Olja, raps", quantity=4 * units.deciliters),
                Ingredient(name="Fransk senap", quantity=7 * units.tablespoons),
                Ingredient(name="Peppar, svart", quantity=None),
            ],
            variants={
                "vegetarian": [
                    Ingredient(name="Quornburgare", quantity=2 * units.count)
                ],
                "laktosfri": [],
            },
        ),
        Dish(
            name="Sill och potatis",
            ingredients=[
                Ingredient(name="Sill, burk, blandat", quantity=10 * units.count),
                Ingredient(name="Potatis", quantity=16 * units.kilograms),
                Ingredient(name="Knäckebröd, skivor", quantity=60 * units.count),
                Ingredient(name="Lök, röd", quantity=5 * units.count),
                Ingredient(name="Gräddfil", quantity=3 * units.liters),
            ],
            variants={
                "laktosfri": [
                    Ingredient(
                        name="Gräddfil, laktosfri", quantity=0.5 * units.deciliters
                    )
                ],
                "vegan": [
                    Ingredient(
                        name="Sojakorvar, Hälsans kök", quantity=4 * units.count
                    ),
                ],
            },
        ),
        Dish(
            name="Brunch",
            ingredients=[
                Ingredient(name="Bacon", quantity=12 * 125 * units.grams),
                Ingredient(name="Prinskorvar", quantity=60 * units.count),
                Ingredient(name="Ägg", quantity=90 * units.count),
                Ingredient(name="Köttbullar", quantity=2 * units.kilograms),
                Ingredient(name="Tomater", quantity=30 * units.count),
                Ingredient(name="Mjölk", quantity=1 * units.liter),
                Ingredient(name="Grädde", quantity=1 * units.liter),
                Ingredient(name="Smör, normalsaltat 80%", quantity=340 * units.grams),
            ],
            variants={
                "laktosfri": [
                    Ingredient(
                        name="Grädde, laktosfri", quantity=0.2 * units.deciliters
                    )
                ],
                "vegan": [
                    Ingredient(
                        name="Sojakorvar, Hälsans kök", quantity=4 * units.count
                    ),
                ],
                "vegetarian": [
                    Ingredient(
                        name="Sojakorvar, Hälsans kök", quantity=4 * units.count
                    ),
                ],
            },
        ),
        Dish(
            name="Gulasch",
            ingredients=[
                Ingredient(name="Grytkött", quantity=5 * units.kilograms),
                Ingredient(name="Kolbasz", quantity=1 * units.kilograms),
                Ingredient(name="Lök, gul", quantity=2.2 * units.kilograms),
                Ingredient(name="Buljongtärning, kött", quantity=20 * units.count),
                Ingredient(name="Tomatpuré", quantity=3.5 * units.deciliters),
                Ingredient(name="Paprikapulver", quantity=None),
                Ingredient(name="Potatis", quantity=4.5 * units.kilograms),
                Ingredient(name="Paprika, röd", quantity=1.4 * units.kilograms),
                Ingredient(name="Salt", quantity=None),
                Ingredient(name="Vitlöksklyftor", quantity=10 * units.count),
                Ingredient(name="Olja, raps", quantity=1.6 * units.deciliters),
                Ingredient(
                    name="Ljust bröd (typ polar), skivor", quantity=40 * units.count
                ),
            ],
            variants={
                "vegetarian": [
                    Ingredient(
                        name="Sojakorvar, Hälsans kök", quantity=4 * units.count
                    ),
                    Ingredient(
                        name="Buljongtärning, grönsak", quantity=0.5 * units.count
                    ),
                ],
                "laktosfri": [],
            },
        ),
        Dish(
            name="Pytt-i-panna",
            ingredients=[
                Ingredient(
                    name="Rödbetor till pytt-i-panna, portioner",
                    quantity=40 * units.count,
                ),
                Ingredient(name="Pytt i panna, portioner", quantity=40 * units.count),
            ],
            variants={
                "vegetarian": [
                    Ingredient(
                        name="Pytt i panna, vegetarisk, portioner",
                        quantity=1 * units.count,
                    ),
                ],
                "vegan": [
                    Ingredient(
                        name="Pytt i panna, vegetarisk, portioner",
                        quantity=1 * units.count,
                    ),
                ],
                "laktosfri": [],
            },
        ),
        Dish(
            name="Chili",
            ingredients=[
                Ingredient(name="Ris, parboiled", quantity=6 * units.liters),
            ],
            variants={
                "hannah": [
                    Ingredient(
                        name="Färdigrätt, åt Hannah H E", quantity=1 * units.count
                    )
                ],
                "vegetarian": [],  # blandar inte i kött i en andel
                "vegan": [],  # blandar inte i kött i en andel
                "laktosfri": [],
            },
        ),
        Dish(
            name="Västafrikansk kikärtsgryta med jordnötssås",
            ingredients=[
                Ingredient(name="Lök, gul", quantity=7 * units.count),
                Ingredient(name="Chili, grön", quantity=14 * units.count),
                Ingredient(name="Vitlöksklyftor", quantity=20 * units.count),
                Ingredient(name="Jordnötssmör, crunchy", quantity=7 * units.deciliters),
                Ingredient(name="Tomatpuré", quantity=14 * units.tablespoons),
                Ingredient(name="Kikärtor, okokta", quantity=0.805 * units.kilograms),
                Ingredient(name="Bladspenat", quantity=2.800 * units.kilograms),
                Ingredient(name="Krossade tomater", quantity=2.800 * units.kilograms),
                Ingredient(name="Chilipulver, röd", quantity=None),
                Ingredient(name="Salt", quantity=None),
                Ingredient(name="Peppar, svart", quantity=None),
                Ingredient(name="Olja, raps", quantity=1.6 * units.deciliters),
                Ingredient(name="Ris, fullkorn", quantity=5 * units.kilograms),
                Ingredient(name="Sriracha", quantity=None),
            ],
        ),
        Dish(
            name="Fest",
            ingredients=[
                Ingredient(name="Salt", quantity=None),
            ],  # Se till att göra något bra.. + kom ihåg natta-mat!
            variants={
                "vegetarian": [
                    Ingredient(name="Salt", quantity=None),
                ],  # Se till att göra något bra..
            },
        ),
        Dish(
            name="Extras",
            ingredients=[
                Ingredient(name="Märkpenna", quantity=2 * units.count),
                Ingredient(name="Tändare med lång hals", quantity=1 * units.count),
                Ingredient(name="Frystejp", quantity=2 * units.count),
                Ingredient(name="Ketchup", quantity=2 * units.count),
                Ingredient(name="Brödbakningsmix", quantity=2 * units.count),
                Ingredient(name="Diskmedel, flaska", quantity=1 * units.count),
                Ingredient(name="Hushållspapper, rullar", quantity=4 * units.count),
                Ingredient(name="Kaffe", quantity=10 * units.kilogram),
                Ingredient(name="Kaffefilter 1X4", quantity=40 * units.count),
                Ingredient(name="Plastfilm, typ gladpack", quantity=1 * units.count),
                Ingredient(name="Plastpåsar, 3L, paket", quantity=1 * units.count),
                Ingredient(name="Rotsaksborste", quantity=1 * units.count),
                Ingredient(name="Soppåsar mindre, rullar", quantity=2 * units.count),
                Ingredient(name="Sopsäckar, stora, rullar", quantity=5 * units.count),
                Ingredient(name="Laktosfritt smör", quantity=2 * units.kilogram),
                Ingredient(name="Grädde", quantity=1 * units.liter),
                Ingredient(name="Havregryn (bara)", quantity=3 * units.kilogram),
                Ingredient(name="Sirap, ljus", quantity=750 * units.gram),
                Ingredient(name="Vetemjöl", quantity=2 * units.kilogram),
                Ingredient(
                    name="Nyponsoppa Klassisk, pulver, färdig dryck",
                    quantity=2 * 5 * units.liters,
                ),
                Ingredient(name="Kakmix, chokladkaka", quantity=4 * units.count),
            ],
        ),
        Dish(
            name="Frukost/fika",
            ingredients=[
                Ingredient(name="Jordgubbssylt", quantity=2 * units.kilogram),
                Ingredient(
                    name="Josextrakt, äpple (måttet är för färdigblandad jos)",
                    quantity=27 * units.liter,
                ),
                Ingredient(
                    name="Josextrakt, apelsin (måttet är för färdigblandad jos)",
                    quantity=27 * units.liter,
                ),
                Ingredient(name="Marmelad", quantity=3 * units.kilogram),
                Ingredient(name="Russin", quantity=1.5 * units.kilogram),
                Ingredient(name="Äppelmos", quantity=6 * units.kilogram),
                Ingredient(
                    name="Frukt, blandad prisvärd", quantity=32.5 * units.kilogram
                ),
                Ingredient(name="Gurka", quantity=2 * units.kilogram),
                Ingredient(name="Paprika, valfri", quantity=2 * units.kilogram),
                Ingredient(name="Tomater", quantity=2 * units.kilogram),
                Ingredient(name="Kanel", quantity=None),
                Ingredient(name="Bregott", quantity=4.2 * units.kilogram),
                Ingredient(name="Filmjölk", quantity=16 * units.liter),
                Ingredient(name="Korvpålägg, skivor", quantity=150 * units.count),
                Ingredient(name="Köttpålägg, skivor", quantity=250 * units.count),
                Ingredient(name="Mjölk", quantity=18 * units.liter),
                Ingredient(name="Cornflakes", quantity=2 * units.kilogram),
                Ingredient(name="Digestivekex", quantity=350 * units.count),
                Ingredient(name="Havregryn (bara)", quantity=5 * 1.5 * units.kilogram),
                Ingredient(name="Knäckebröd, skivor", quantity=2 * units.kilogram),
                Ingredient(
                    name="Ljust bröd (typ polar), skivor", quantity=9 * 40 * units.count
                ),
                Ingredient(name="Mörkt bröd, skivor", quantity=7 * 40 * units.count),
                Ingredient(name="Mariekex", quantity=600 * units.count),
                Ingredient(name="Müsli", quantity=4 * units.kilogram),
                Ingredient(name="Skorpor, kardemumma", quantity=3 * units.kilogram),
                Ingredient(name="Skorpor, grova", quantity=3 * units.kilogram),
                Ingredient(name="Tepåsar", quantity=150 * units.count),
                Ingredient(name="Ost mild", quantity=3 * units.kilogram),
                Ingredient(name="Ost med smak", quantity=5.3 * units.kilogram),
            ],
            variants={
                "glutenfri": [
                    Ingredient(
                        name="Knäckebröd, glutenfritt, skivor",
                        quantity=20 * units.count,
                    ),
                ],
                "laktosfri": [
                    Ingredient(name="Mjölk, laktosfri", quantity=1 * units.liter),
                    Ingredient(name="Filmjölk, laktosfri", quantity=1 * units.liter),
                    Ingredient(name="Yoghurt, laktosfri", quantity=1 * units.liter),
                ],
                "mjölkfri": [
                    Ingredient(name="Sojamjölk", quantity=1 * units.liter),
                ],
            },
        ),
    ]
)

# laktosfri
# mjölkfri
# glutenfri
# veg
# vegan

menu: list[MenuItem] = [
    MenuItem(
        dish=dishes["Korv stroganoff"],
        day="tisdag",
        variants={"laktosfri": 2, "vegetarian": 1},
    ),
    MenuItem(
        dish=dishes["Fisksoppa"],
        day="tisdag",
        variants={"laktosfri": 2, "vegetarian": 0},
    ),
    MenuItem(
        dish=dishes["Kassler med potatissallad"],
        day="onsdag",
        variants={"laktosfri": 2, "vegetarian": 1},
    ),
    MenuItem(
        dish=dishes["Kycklinggryta med fetaost"],
        day="onsdag",
        variants={"laktosfri": 2, "vegetarian": 1},
    ),
    MenuItem(
        dish=dishes["Västafrikansk kikärtsgryta med jordnötssås"],
        day="torsdag",
    ),
    MenuItem(
        dish=dishes["Gulasch"],
        day="torsdag",
        variants={"vegetarian": 2},
    ),
    MenuItem(
        dish=dishes["Fänkål och kycklingsallad"],
        day="fredag",
        variants={"vegetarian": 1},
    ),
    MenuItem(
        dish=dishes["Porterstek"],
        day="fredag",
        variants={"glutenfri": 0, "laktosfri": 0, "vegetarian": 1},
    ),
    MenuItem(
        dish=dishes["Ärtsoppa"],
        day="lördag",
        variants={"vegetarian": 1},
    ),
    # MenuItem(
    #     dish=dishes["Lax"],
    #     day="lördag",
    #     variants={"laktosfri": 0},
    # ),
    # MenuItem(
    #     dish=dishes["Sill och potatis"],
    #     day="lördag",
    #     variants={"laktosfri": 0},
    # ),
    MenuItem(dish=dishes["Fest"], day="lördag", variants={"vegetarian": 1}),
    MenuItem(
        dish=dishes["Brunch"], day="söndag", variants={"laktosfri": 1, "vegetarian": 2}
    ),
    # MenuItem(
    #     dish=dishes["Pytt-i-panna"],
    #     day="söndag",
    #     variants={"laktosfri": 1, "vegetarian": 2},
    # ),
    MenuItem(
        dish=dishes["Frukost/fika"],
        day=None,
        variants={"laktosfri": 2, "mjölkfri": 0, "glutenfri": 1},
    ),
    MenuItem(dish=dishes["Extras"], day=None),
]

translations = [("kilogram", "kg"), ("count", "st"), ("deciliter", "dl"), ("gram", "g")]

# prebought = [
#                Ingredient(name=u"Korvpålägg, skivor", quantity=50*units.count),
#                Ingredient(name=u"Köttpålägg, skivor", quantity=150*units.count),
#                Ingredient(name=u"Sill, burk, blandat",  quantity=10 * units.count),
#                Ingredient(name=u"Vetemjöl",             quantity=940 * units.grams),
#                Ingredient(name=u"Tomatpuré",             quantity=350 * units.grams),
#                Ingredient(name=u"Kikärtor, okokta",     quantity=1.2 * units.kilograms),
#                Ingredient(name=u"Kidneybönor, okokta",  quantity=1.4 * units.kilograms),
#                 Ingredient(name=u"Fänkål",         quantity=7.2 * units.kilograms),
#                 Ingredient(name=u"Valnötter",      quantity=15 * units.deciliters),
#                 Ingredient(name=u"Ost med smak", quantity=4.3*units.kilogram),
#                 Ingredient(name=u"Buljongtärning, grönsak", quantity=11*units.count),
#             ]

# Remove this from the list, already bought!
prebought: list[Ingredient] = [
    # Ingredient(name="Kycklingfilé", quantity=5 * units.kilogram),
    # Ingredient(name="Fisk (kolja, sej)", quantity=2.5 * units.kilogram),
    # Ingredient(name="Buljongtärning, kött", quantity=6 * units.count),
    # Ingredient(name="Buljongtärning, grönsak", quantity=8 * units.count),
    # Ingredient(name="Grädde", quantity=9 * units.liters),
    # Ingredient(name="Olja, raps", quantity=9 * units.deciliters),
    #                Ingredient(name=u"Kikärtor, avrunnen vikt",     quantity=1.5 * units.kilograms),
    #                Ingredient(name=u"Kidneybönor, avrunnen vikt",  quantity=1.5 * units.kilograms),
    #                Ingredient(name=u"Fänkål",               quantity=5.4 * units.kilograms),
    #                Ingredient(name=u"Lax",                  quantity=150 * 40 * units.gram),
    #                Ingredient(name=u"Tomatpuré",            quantity=440 * units.grams),
]

# Remove this from the list, save for buying later
buy_later: list[Ingredient] = [
    Ingredient(name="Ägg", quantity=90 * units.count),  # simply do not buy them before
    Ingredient(name="Mjölk", quantity=14 * units.liters),
    Ingredient(name="Bröd, ljust, skivor", quantity=80 * units.count),
    Ingredient(name="Filmjölk", quantity=8 * units.liter),
    Ingredient(name="Frukt, blandad prisvärd", quantity=16.5 * units.kilogram),
]
