# -*- coding: utf-8 -*-

from pint import UnitRegistry, quantity
from datetime import datetime

from classes import Ingredient, Dish, MenuItem, NameDict

units = UnitRegistry()

ingredient_types = NameDict([
    Ingredient(name=u"Oliver, svarta", purchase_unit=units.kilograms, category=u"burk",
               conversions=[657 * units.kilograms / units.meter**3]),
    Ingredient(name=u"Olja, oliv",     purchase_unit=units.liter,     category=u"burk"),
    Ingredient(name=u"Olja, raps",     purchase_unit=units.liter,     category=u"burk"),
    Ingredient(name=u"Krossade tomater",purchase_unit=units.kilograms, category=u"burk"),
    Ingredient(name=u"Matlagningsvin, vitt",purchase_unit=units.litres, category=u"burk"),
    Ingredient(name=u"Tomatpuré",      purchase_unit=units.kilograms,  category=u"burk",
               conversions=[1 * units.cups / (8*units.ounces)]),
    Ingredient(name=u"Fransk senap",   purchase_unit=units.grams, category=u"burk",
               conversions=[8.47 * units.ounce / (1*units.cups)]),
    Ingredient(name=u"Ketchup",        purchase_unit=units.count, category=u"burk"),
    Ingredient(name=u"Sambal oelek",   purchase_unit=units.grams, category=u"burk",
               conversions=[1 * units.cups / (8*units.ounces)]),
    Ingredient(name=u"Soya, kinesisk", purchase_unit=units.liter,     category=u"burk"),
    Ingredient(name=u"Majonäs, burk",  purchase_unit=units.count,     category=u"burk"),
    Ingredient(name=u"Valnötter",      purchase_unit=units.kilograms, category=u"torr",
               conversions=[1.1 * units.kilograms / (15 * units.deciliters)]),
    Ingredient(name=u"Salt",           purchase_unit=None,            category=u"krydd"),
    Ingredient(name=u"Peppar, svart",  purchase_unit=None,            category=u"krydd"),
    Ingredient(name=u"Peppar, svart, hel",purchase_unit=None,            category=u"krydd"),
    Ingredient(name=u"Basilika",       purchase_unit=None,            category=u"krydd"),
    Ingredient(name=u"Oregano",        purchase_unit=None,            category=u"krydd"),
    Ingredient(name=u"Timjan",         purchase_unit=None,            category=u"krydd"),
    Ingredient(name=u"Salt, grov",     purchase_unit=None,            category=u"krydd"),
    Ingredient(name=u"Buljongtärning, höns", purchase_unit=units.count, category=u"krydd"),
    Ingredient(name=u"Buljongtärning, kött", purchase_unit=units.count, category=u"krydd"),
    Ingredient(name=u"Buljongtärning, grönsak", purchase_unit=units.count, category=u"krydd"),
    Ingredient(name=u"Pasta, skruvar", purchase_unit=units.kilograms, category=u"torr"),
    Ingredient(name=u"Socker",         purchase_unit=units.kilograms, category=u"torr",
               conversions=[1 * units.deciliters / (88 * units.grams)]),
    Ingredient(name=u"Ris",            purchase_unit=units.kilograms, category=u"torr",
               conversions=[0.9 * units.grams / units.cm**3]),
    Ingredient(name=u"Vitlöksklyftor", purchase_unit=units.grams, category=u"grönt",
               conversions=[6 * units.grams / units.count]),
    Ingredient(name=u"Apelsiner",      purchase_unit=units.kilograms, category=u"grönt",
               conversions=[200 * units.grams / units.count]),
    Ingredient(name=u"Fänkål",         purchase_unit=units.kilograms, category=u"grönt"),
    Ingredient(name=u"Lök, gul",        purchase_unit=units.kilograms, category=u"grönt",
               conversions=[100 * units.grams / units.count]),
    Ingredient(name=u"Morötter",       purchase_unit=units.kilograms, category=u"grönt",
               conversions=[70 * units.grams / units.count]),
    Ingredient(name=u"Rotselleri",     purchase_unit=units.count,     category=u"grönt"),
    Ingredient(name=u"Potatis",        purchase_unit=units.kilograms, category=u"grönt"),
    Ingredient(name=u"Dill, färsk, planta/motsv",    purchase_unit=units.count,            category=u"grönt"),
    Ingredient(name=u'Ingefära, färsk',purchase_unit=units.grams,     category=u"grönt"),
    Ingredient(name=u'Salladshuvud',   purchase_unit=units.count,     category=u"grönt"),
    Ingredient(name=u'Tomater',        purchase_unit=units.kilograms, category=u"grönt",
               conversions=[115 * units.grams / units.count]),
    Ingredient(name=u'Chili, grön',    purchase_unit=units.count,     category=u"grönt"),
    Ingredient(name=u"Kycklingfilé",   purchase_unit=units.kilograms, category=u"frys"),
    Ingredient(name=u"Broccoli",       purchase_unit=units.kilograms, category=u"frys"),
    Ingredient(name=u"Persilja, fryst",purchase_unit=units.count,     category=u"frys"),
    Ingredient(name=u"Fetaost",        purchase_unit=units.kilograms, category=u"mejeri"),
    Ingredient(name=u"Mjölk",          purchase_unit=units.liters,    category=u"mejeri"),
    Ingredient(name=u"Gräddfil",       purchase_unit=units.liters,    category=u"mejeri"),
    Ingredient(name=u"Gräddfil, laktosfri",       purchase_unit=units.liters,    category=u"mejeri"),
    Ingredient(name=u"Creme Fraiche, lätt",          purchase_unit=units.liters,    category=u"mejeri"),
    Ingredient(name=u"Köttfärs, nöt",  purchase_unit=units.kilograms, category=u"kyl"),
    Ingredient(name=u"Falukorv",       purchase_unit=units.kilograms, category=u"kyl"),

    Ingredient(name=u'Chilipulver, röd',purchase_unit=None,           category=u"krydd"),
    Ingredient(name=u'Gurka',          purchase_unit=units.kilograms,     category=u"grönt",
               conversions=[463 * units.grams/ units.count]),
    Ingredient(name=u'Koriander, malen',purchase_unit=None,           category=u"krydd"),
    Ingredient(name=u'Vetemjöl',       purchase_unit=units.kilograms, category=u"torr",
               conversions=[60 * units.grams / units.deciliters]),
    Ingredient(name=u'Kidneybönor, okokta',purchase_unit=units.kilogram, category=u"torr"),
    Ingredient(name=u'Koriander, färsk',purchase_unit=units.count,    category=u"grönt"),
    Ingredient(name=u'Gurkmeja',       purchase_unit=None,            category=u"krydd"),
    Ingredient(name=u'Vinbärsaft, outspädd, bra (typ Önos)',purchase_unit=units.liter, category=u"burk"),
    Ingredient(name=u'Kikärtor, okokta',purchase_unit=units.kilogram, category=u"torr"),
    Ingredient(name=u'Porter',         purchase_unit=units.liter,     category=u"burk"),
    Ingredient(name=u'Citroner',       purchase_unit=units.count,     category=u"grönt"),
    Ingredient(name=u'Enbär, torkade', purchase_unit=units.gram,      category=u"krydd"),
    Ingredient(name=u'Grädde',         purchase_unit=units.liter,     category=u"mejeri"),
    Ingredient(name=u'Spiskummin',     purchase_unit=None,            category=u"krydd"),
    Ingredient(name=u'Högrev, benfri',purchase_unit=units.kilogram,category=u"kyl"),

    Ingredient(name=u'Kassler',        purchase_unit=units.kilogram,  category=u"kyl"),
    Ingredient(name=u'Vinäger, vitvins',purchase_unit=units.liters, category=u"burk"),
    Ingredient(name=u'Lök, röd',purchase_unit=units.kilogram,            category=u"grönt",
               conversions=[100 * units.grams / units.count]),
    Ingredient(name=u'Rädisor, knippe',purchase_unit=units.count, category=u"grönt"),

    Ingredient(name=u'Prinskorvar',    purchase_unit=units.count, category=u"kyl"),
    Ingredient(name=u'Sill, burk, blandat',purchase_unit=units.count, category=u"kyl"),
    Ingredient(name=u'Knäckebröd, skivor',purchase_unit=units.count, category=u"torr",
               conversions=[17 * units.grams / units.count]),
    Ingredient(name=u'Ägg',            purchase_unit=units.count, category=u"kyl"),
    Ingredient(name=u'Köttbullar',     purchase_unit=units.kilogram, category=u"kyl"),
    Ingredient(name=u'Bacon',          purchase_unit=units.kilogram, category=u"kyl"),

    Ingredient(name=u'Paprika, röd',purchase_unit=units.kilogram, category=u"grönt"),
    Ingredient(name=u'Paprikapulver',  purchase_unit=None,           category=u"krydd"),
    Ingredient(name=u'Bröd, ljust, skivor',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Grytkött',purchase_unit=units.kilogram, category=u"kyl"),
    Ingredient(name=u'Kolbasz',purchase_unit=units.kilogram, category=u"kyl"),
    Ingredient(name=u'Rödbetor till pytt-i-panna, portioner',purchase_unit=units.count, category=u"burk"),
    Ingredient(name=u'Pytt i panna, portioner',purchase_unit=units.count, category=u"frys"),

    Ingredient(name=u'Grädde, laktosfri',purchase_unit=units.liter, category=u"mejeri"),
    Ingredient(name=u'Creme Fraiche, laktosfri',purchase_unit=units.liter, category=u"mejeri"),
    Ingredient(name=u'Pasta, glutenfri, portioner',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Mjölk, laktosfri',purchase_unit=units.liter, category=u"mejeri"),

    Ingredient(name=u'Tofu, portioner',purchase_unit=units.count, category=u"kyl"),

    Ingredient(name=u'Quornburgare',purchase_unit=units.count, category=u"frys"),
    Ingredient(name=u'Quornfiléer',purchase_unit=units.count, category=u"frys"),
    Ingredient(name=u'Sojakorvar, Hälsans kök',purchase_unit=units.count, category=u"frys"),

    Ingredient(name=u'Kaffe',purchase_unit=units.kilogram, category=u"torr"),
    Ingredient(name=u'Diskmedel, flaska',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Rotsaksborste',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Brödbakningsmix',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Plastfilm, typ gladpack',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Sopsäckar, stora, rullar',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Kaffefilter 1X4',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Soppåsar mindre, rullar',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Hushållspapper, rullar',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Plastpåsar, 3L, paket',purchase_unit=units.count, category=u"torr"),

    Ingredient(name=u'Filmjölk',purchase_unit=units.liter, category=u"mejeri"),
    Ingredient(name=u'Korvpålägg, skivor',purchase_unit=units.count, category=u"kyl"),
    Ingredient(name=u'Köttpålägg, skivor',purchase_unit=units.count, category=u"kyl"),
    Ingredient(name=u'Cornflakes',purchase_unit=units.kilogram, category=u"torr"),
    Ingredient(name=u'Jordgubbssylt',purchase_unit=units.kilogram, category=u"burk"),
    Ingredient(name=u'Digestivekex',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Josextrakt, äpple (måttet är för färdigblandad jos)',purchase_unit=units.liter, category=u"burk"),
    Ingredient(name=u'Havregryn (bara)',purchase_unit=units.kilogram, category=u"torr"),
    Ingredient(name=u'Josextrakt, apelsin (måttet är för färdigblandad jos)',purchase_unit=units.liter, category=u"burk"),
    Ingredient(name=u'Kakmix, chokladkaka',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Marmelad',purchase_unit=units.kilogram, category=u"burk"),
    Ingredient(name=u'Russin',purchase_unit=units.kilogram, category=u"torr"),
    Ingredient(name=u'Ljust bröd, skivor',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Äppelmos',purchase_unit=units.kilogram, category=u"burk"),
    Ingredient(name=u'Mörkt bröd, skivor',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Frukt, blandad prisvärd',purchase_unit=units.kilogram, category=u"grönt"),
    Ingredient(name=u'Mariekex',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Müsli',purchase_unit=units.kilogram, category=u"torr"),
    Ingredient(name=u'Paprika, valfri',purchase_unit=units.kilogram, category=u"grönt"),
    Ingredient(name=u'Skorpor',purchase_unit=units.kilogram, category=u"torr"),
    Ingredient(name=u'Tepåsar',purchase_unit=units.count, category=u"torr"),
    Ingredient(name=u'Kanel',purchase_unit=None, category=u"krydd"),
    Ingredient(name=u'Bregott',purchase_unit=units.kilogram, category=u"mejeri"),
    
    Ingredient(name=u"Färdigrätt, åt Hannah H E", purchase_unit=units.count, category=u"frys"),

    Ingredient(name=u'Filmjölk, laktosfri',purchase_unit=units.liter, category=u"mejeri"),
    Ingredient(name=u'Yoghurt, laktosfri',purchase_unit=units.liter, category=u"mejeri"),
    Ingredient(name=u'Knäckebröd, glutenfritt, skivor',purchase_unit=units.count, category=u"torr"),

    Ingredient(name=u'Pasta, Penne',purchase_unit=units.kilogram, category=u"torr"),
    Ingredient(name=u'Cirtronjuice',purchase_unit=units.deciliter, category=u"burk"),
    Ingredient(name=u'Lax',purchase_unit=units.gram, category=u"kyl"),

])

dishes = NameDict([
    Dish(name=u"Fänkål och kycklingsallad", ingredients=[
                Ingredient(name=u"Fänkål",         quantity=7.2 * units.kilograms),
                Ingredient(name=u"Kycklingfilé",   quantity=3.6 * units.kilograms),
                Ingredient(name=u"Fetaost",        quantity=2.2 * units.kilograms),
                Ingredient(name=u"Valnötter",      quantity=15 * units.deciliters),
                Ingredient(name=u"Oliver, svarta", quantity=15 * units.deciliters),
                Ingredient(name=u"Apelsiner",      quantity=18 * units.count),
                Ingredient(name=u"Cirtronjuice",   quantity=7 * units.deciliters),
                Ingredient(name=u"Olja, oliv",     quantity=6 * units.deciliters),
                Ingredient(name=u"Salt",           quantity=None),
                Ingredient(name=u"Peppar, svart",  quantity=None)
                ], variants={
                "veg": [
                    Ingredient(name=u"Quornfiléer", quantity=1*units.count)
                    ]
                }),
    Dish(name=u"Kycklinggryta med fetaost", ingredients=[
                Ingredient(name=u"Olja, raps",           quantity=1.6 * units.deciliters),
                Ingredient(name=u"Vitlöksklyftor",       quantity=8 * units.count),
                Ingredient(name=u"Kycklingfilé",         quantity=5 * units.kilogram),
                Ingredient(name=u"Krossade tomater",     quantity=24*400*units.gram),
                Ingredient(name=u"Buljongtärning, höns", quantity=16 * units.count),
                Ingredient(name=u"Matlagningsvin, vitt", quantity=12 * units.deciliters),
                Ingredient(name=u"Peppar, svart",        quantity=None),
                Ingredient(name=u"Broccoli",             quantity=2 * units.kilogram),
                Ingredient(name=u"Fetaost",              quantity=1.6 * units.kilogram),
                Ingredient(name=u"Basilika",             quantity=None),
                Ingredient(name=u"Salt",                 quantity=None),
                Ingredient(name=u"Pasta, Penne",         quantity=5 * units.kilogram),
                ], variants={
                "veg": [
                    Ingredient(name=u"Quornfiléer", quantity=2*units.count),
                    Ingredient(name=u"Buljongtärning, grönsak", quantity=.5*units.count)
                    ],
                "glutenfri": [
                    Ingredient(name=u"Pasta, glutenfri, portioner", quantity=1*units.count)
                    ],
                }),
    Dish(name=u"Pasta & köttfärssås", ingredients=[
                Ingredient(name=u"Lök, gul",              quantity=15 * units.count),
                Ingredient(name=u"Morötter",             quantity=15 * units.count),
                Ingredient(name=u"Rotselleri",           quantity=3 * units.count),
                Ingredient(name=u"Vitlöksklyftor",       quantity=10 * units.count),
                Ingredient(name=u"Köttfärs, nöt",        quantity=5 * units.kilogram),
                Ingredient(name=u"Buljongtärning, kött", quantity=6 * units.count),
                Ingredient(name=u"Peppar, svart",        quantity=None),
                Ingredient(name=u"Oregano",              quantity=None),
                Ingredient(name=u"Timjan",               quantity=None),
                Ingredient(name=u"Basilika",             quantity=None),
                Ingredient(name=u"Krossade tomater",     quantity=20*400*units.gram),
                Ingredient(name=u"Tomatpuré",            quantity=3*units.deciliters),
                Ingredient(name=u"Pasta, skruvar",       quantity=5*units.kilograms),                
                ], variants={
                "glutenfri": [
                    Ingredient(name=u"Pasta, glutenfri, portioner", quantity=1*units.count)
                    ],
                "veg": [
                    Ingredient(name=u"Quornburgare", quantity=1*units.count),
                    Ingredient(name=u"Buljongtärning, grönsak", quantity=.5*units.count)
                    ],
                }),
    Dish(name=u"Korv stroganoff", ingredients=[
                Ingredient(name=u"Falukorv",             quantity=5 * units.kilogram),
                Ingredient(name=u"Lök, gul",              quantity=20 * units.count),
                Ingredient(name=u"Tomatpuré",            quantity=6 * units.deciliters),
                Ingredient(name=u"Fransk senap",         quantity=1.5 * units.deciliters),
                Ingredient(name=u"Mjölk",                quantity=3 * units.liters),
                Ingredient(name=u"Buljongtärning, grönsak", quantity=4 * units.count),
                Ingredient(name=u"Creme Fraiche, lätt",  quantity=3 * units.liters),
                Ingredient(name=u"Ketchup",              quantity=.5 * units.count),
                Ingredient(name=u"Sambal oelek",         quantity=4 * units.tablespoons),
                Ingredient(name=u"Socker",               quantity=4 * units.deciliters),
                Ingredient(name=u"Soya, kinesisk",       quantity=3 * units.deciliters),
                Ingredient(name=u"Vitlöksklyftor",       quantity=1 * units.ounce),
                Ingredient(name=u"Peppar, svart",        quantity=None),
                Ingredient(name=u"Salt",                 quantity=None),
                Ingredient(name=u"Timjan",               quantity=None),
                Ingredient(name=u"Olja, raps",           quantity=1 * units.deciliters),
                Ingredient(name=u"Ris",                  quantity=6 * units.liters),
                ], variants={
                "laktosfri": [
                    Ingredient(name=u"Mjölk, laktosfri", quantity=1 * units.deciliters),
                    Ingredient(name=u"Creme Fraiche, laktosfri", quantity=.5 * units.deciliters),
                    ],
                "veg": [
                    Ingredient(name=u"Sojakorvar, Hälsans kök", quantity=4 * units.count)
                    ]
                }),
    Dish(name=u"Lax", ingredients=[
                Ingredient(name=u"Salt, grov",           quantity=None),
                Ingredient(name=u"Majonäs, burk",        quantity=2 * units.count),
                Ingredient(name=u"Persilja, fryst",      quantity=1 * units.count),
                Ingredient(name=u"Peppar, svart",        quantity=None),
                Ingredient(name=u"Timjan",               quantity=None),
                Ingredient(name=u"Potatis",              quantity=16 * units.kilograms),
                Ingredient(name=u"Dill, färsk, planta/motsv", quantity=4 * units.count),
                Ingredient(name=u"Gräddfil",             quantity=3 * units.liters),                
                Ingredient(name=u"Lax",                  quantity=150 * 40 * units.gram),                
                ], variants={
                "laktosfri": [
                    Ingredient(name=u"Gräddfil, laktosfri", quantity=1 * units.deciliters)
                    ]
                }),
    Dish(name=u"2 x Indisk curry", ingredients=[
                Ingredient(name=u"Kidneybönor, okokta",  quantity=1.4 * units.kilograms),
                Ingredient(name=u"Lök, gul",             quantity=20 * units.count),
                Ingredient(name=u"Tomater",              quantity=(10+10) * units.count),
                Ingredient(name=u"Chili, grön",          quantity=10 * units.count),
                Ingredient(name=u"Vitlöksklyftor",       quantity=10 * units.count),
                Ingredient(name=u"Olja, raps",           quantity=(4+6) * units.deciliters),
                Ingredient(name=u"Gurkmeja",             quantity=None),
                Ingredient(name=u"Ingefära, färsk",      quantity=200 * units.grams),
                Ingredient(name=u"Koriander, färsk",     quantity=4 * units.count),
                Ingredient(name=u"Kikärtor, okokta",     quantity=1.2 * units.kilograms),
                Ingredient(name=u"Spiskummin",           quantity=None),
                Ingredient(name=u"Chilipulver, röd",     quantity=None),
                Ingredient(name=u"Koriander, malen",     quantity=None),
                Ingredient(name=u"Citroner",             quantity=3 * units.count),
                ], variants={
                "hannah": [
                    Ingredient(name=u"Tofu, portioner", quantity=1 * units.count)
                    ]
                }),
    Dish(name=u"Porterstek", ingredients=[
                Ingredient(name=u"Högrev, benfri",       quantity=10 * units.kilograms),
                Ingredient(name=u"Porter",               quantity=10 * 33 * units.centiliters),
                Ingredient(name=u"Vinbärsaft, outspädd, bra (typ Önos)", quantity=.5 * units.liters),
                Ingredient(name=u"Soya, kinesisk",       quantity=3 * units.liters),
                Ingredient(name=u"Timjan",               quantity=None),
                Ingredient(name=u"Enbär, torkade",       quantity=8 * units.grams),
                Ingredient(name=u"Peppar, svart, hel",   quantity=None),
                Ingredient(name=u"Buljongtärning, kött", quantity=25 * units.count),
                Ingredient(name=u"Vitlöksklyftor",       quantity=20 * units.count),
                Ingredient(name=u"Lök, gul",             quantity=10 * units.count),
                Ingredient(name=u"Vetemjöl",             quantity=3.75 * units.deciliters),
                Ingredient(name=u"Grädde",               quantity=1 * units.liters),
                Ingredient(name=u"Potatis",              quantity=16 * units.kilograms),
                Ingredient(name=u"Salladshuvud",         quantity=6 * units.count),
                Ingredient(name=u"Gurka",                quantity=5 * units.count),
                Ingredient(name=u"Tomater",              quantity=10 * units.count),
                ], variants={
                "laktosfri": [
                    Ingredient(name=u"Grädde, laktosfri", quantity=1 * units.deciliters)
                    ],
                "veg": [
                    Ingredient(name=u"Quornfiléer", quantity=2*units.count),
                    Ingredient(name=u"Buljongtärning, grönsak", quantity=.5*units.count),
                    ],
                }),
    Dish(name=u"Kassler med potatissallad", ingredients=[
                Ingredient(name=u"Potatis",              quantity=13 * units.kilograms),
                Ingredient(name=u"Lök, röd",             quantity=13 * units.count),
                Ingredient(name=u"Rädisor, knippe",      quantity=13 * units.count),
                Ingredient(name=u"Salt",                 quantity=None),
                Ingredient(name=u"Kassler",              quantity=5 * units.kilograms),
                Ingredient(name=u"Vinäger, vitvins",     quantity=2 * units.deciliters),
                Ingredient(name=u"Olja, raps",           quantity=4 * units.deciliters),
                Ingredient(name=u"Fransk senap",         quantity=7 * units.tablespoons),
                Ingredient(name=u"Peppar, svart",        quantity=None),
                ], variants={
                "veg": [
                    Ingredient(name=u"Quornburgare", quantity=2 * units.count)
                    ]
                }),
    Dish(name=u"Sill och potatis", ingredients=[
                Ingredient(name=u"Sill, burk, blandat",  quantity=10 * units.count),
                Ingredient(name=u"Potatis",              quantity=16 * units.kilograms),
                Ingredient(name=u"Knäckebröd, skivor",   quantity=60 * units.count),
                Ingredient(name=u"Lök, röd",             quantity=5 * units.count),
                Ingredient(name=u"Gräddfil",             quantity=3 * units.liters),                
                ], variants={
                "laktosfri": [
                    Ingredient(name=u"Gräddfil, laktosfri", quantity=.5 * units.deciliters)
                    ]
                }),
    Dish(name=u"Brunch", ingredients=[
                Ingredient(name=u"Bacon",                quantity=12*125 * units.grams),                
                Ingredient(name=u"Prinskorvar",          quantity=60 * units.count),                
                Ingredient(name=u"Ägg",                  quantity=90 * units.count),                
                Ingredient(name=u"Köttbullar",           quantity=2 * units.kilograms),            
                Ingredient(name=u"Tomater",              quantity=30 * units.count),
                ]),                
    Dish(name=u"Gulasch", ingredients=[
                Ingredient(name=u"Grytkött",             quantity=5 * units.kilograms),
                Ingredient(name=u"Kolbasz",              quantity=1 * units.kilograms),
                Ingredient(name=u"Lök, gul",             quantity=2.2 * units.kilograms),
                Ingredient(name=u"Buljongtärning, kött", quantity=20 * units.count),
                Ingredient(name=u"Tomatpuré",            quantity=3.5*units.deciliters),
                Ingredient(name=u"Paprikapulver",        quantity=None),
                Ingredient(name=u"Potatis",              quantity=4.5 * units.kilograms),
                Ingredient(name=u"Paprika, röd",         quantity=1.4 * units.kilograms),
                Ingredient(name=u"Salt",                 quantity=None),
                Ingredient(name=u"Vitlöksklyftor",       quantity=10 * units.count),
                Ingredient(name=u"Olja, raps",           quantity=1.6 * units.deciliters),
                Ingredient(name=u"Bröd, ljust, skivor",  quantity=40 * units.count),                
                ], variants={
                "veg": [
                    Ingredient(name=u"Sojakorvar, Hälsans kök", quantity=4 * units.count),
                    Ingredient(name=u"Buljongtärning, grönsak", quantity=.5*units.count),
                    ]
                }),
    Dish(name=u"Pytt-i-panna", ingredients=[
                Ingredient(name=u"Rödbetor till pytt-i-panna, portioner", quantity=40 * units.count),
                Ingredient(name=u"Pytt i panna, portioner", quantity=40 * units.count),
    ]),
    Dish(name=u"Chili", ingredients=[
                Ingredient(name=u"Ris",                  quantity=6 * units.liters),
                ], variants={
                "hannah": [ Ingredient(name=u"Färdigrätt, åt Hannah H E", quantity=1 * units.count) ]}),
    Dish(name=u"Extras", ingredients=[
                Ingredient(name=u"Ketchup", quantity=2 * units.count),
                Ingredient(name=u"Brödbakningsmix", quantity=2 * units.count),
                Ingredient(name=u"Diskmedel, flaska", quantity=1 * units.count),
                Ingredient(name=u"Hushållspapper, rullar", quantity=4 * units.count),
                Ingredient(name=u"Kaffe", quantity=10 * units.kilogram),
                Ingredient(name=u"Kaffefilter 1X4", quantity=40 * units.count),
                Ingredient(name=u"Plastfilm, typ gladpack", quantity=1 * units.count),
                Ingredient(name=u"Plastpåsar, 3L, paket", quantity=1 * units.count),
                Ingredient(name=u"Rotsaksborste", quantity=1 * units.count),
                Ingredient(name=u"Soppåsar mindre, rullar", quantity=2 * units.count),
                Ingredient(name=u"Sopsäckar, stora, rullar", quantity=5 * units.count),
    ]),
    Dish(name=u"Frukost/fika", ingredients=[
                Ingredient(name=u"Jordgubbssylt", quantity=2*units.kilogram),
                Ingredient(name=u"Josextrakt, äpple (måttet är för färdigblandad jos)", quantity=27*units.liter),
                Ingredient(name=u"Josextrakt, apelsin (måttet är för färdigblandad jos)", quantity=27*units.liter),
                Ingredient(name=u"Marmelad", quantity=3*units.kilogram),
                Ingredient(name=u"Russin", quantity=1.5*units.kilogram),
                Ingredient(name=u"Äppelmos", quantity=6*units.kilogram),
                Ingredient(name=u"Frukt, blandad prisvärd", quantity=32.5*units.kilogram),
                Ingredient(name=u"Gurka", quantity=2*units.kilogram),
                Ingredient(name=u"Paprika, valfri", quantity=2*units.kilogram),
                Ingredient(name=u"Tomater", quantity=2*units.kilogram),
                Ingredient(name=u"Kanel", quantity=None),
                Ingredient(name=u"Bregott", quantity=4.2*units.kilogram),
                Ingredient(name=u"Filmjölk", quantity=16*units.liter),
                Ingredient(name=u"Korvpålägg, skivor", quantity=150*units.count),
                Ingredient(name=u"Köttpålägg, skivor", quantity=250*units.count),
                Ingredient(name=u"Mjölk", quantity=22*units.liter),
                Ingredient(name=u"Cornflakes", quantity=2*units.kilogram),
                Ingredient(name=u"Digestivekex", quantity=400*units.count),
                Ingredient(name=u"Havregryn (bara)", quantity=5*1.5*units.kilogram),
                Ingredient(name=u"Kakmix, chokladkaka", quantity=4*units.count),
                Ingredient(name=u"Knäckebröd, skivor", quantity=2*units.kilogram),
                Ingredient(name=u"Ljust bröd, skivor", quantity=9*40*units.count),
                Ingredient(name=u"Mörkt bröd, skivor", quantity=40*units.count),
                Ingredient(name=u"Mariekex", quantity=600*units.count),
                Ingredient(name=u"Müsli", quantity=4*units.kilogram),
                Ingredient(name=u"Skorpor", quantity=6*units.kilogram),
                Ingredient(name=u"Tepåsar", quantity=150*units.count),
    ],variants={
                "hannah": [
                    Ingredient(name=u"Knäckebröd, glutenfritt, skivor", quantity=20 * units.count),
                    ],
                "laktosfri": [
                    Ingredient(name=u"Mjölk, laktosfri", quantity=1*units.liter),
                    Ingredient(name=u"Filmjölk, laktosfri", quantity=1*units.liter),
                    Ingredient(name=u"Yoghurt, laktosfri", quantity=1*units.liter),
                              ]
                }),
])

menu = [
    MenuItem(dish=dishes[u"Fänkål och kycklingsallad"], day=u"måndag", variants={"veg": 2}),
    MenuItem(dish=dishes[u"Pasta & köttfärssås"], day=u"måndag", variants={"glutenfri": 1, "veg": 2}),
    MenuItem(dish=dishes[u"Korv stroganoff"], day=u"tisdag", variants={"laktosfri": 2, "veg": 2}),
    MenuItem(dish=dishes[u"Lax"], day=u"tisdag", variants={"laktosfri": 2}),
    MenuItem(dish=dishes[u"2 x Indisk curry"], day=u"onsdag", variants={"hannah": 1}),
    MenuItem(dish=dishes[u"Porterstek"], day=u"onsdag", variants={"laktosfri": 2, "veg": 2}),
    MenuItem(dish=dishes[u"Kassler med potatissallad"], day=u"torsdag", variants={"veg": 2}),
    MenuItem(dish=dishes[u"Kycklinggryta med fetaost"], day=u"torsdag", variants={"veg": 2, "glutenfri": 1}),
    MenuItem(dish=dishes[u"Sill och potatis"], day=u"fredag", variants={"laktosfri": 2}),
    MenuItem(dish=dishes[u"Brunch"], day=u"lördag"),
    MenuItem(dish=dishes[u"Gulasch"], day=u"lördag", variants={"veg": 2}),
    MenuItem(dish=dishes[u"Pytt-i-panna"], day=u"söndag"),    
    MenuItem(dish=dishes[u"Frukost/fika"], day=None, variants={"laktosfri": 2, "hannah": 1}),
    MenuItem(dish=dishes[u"Extras"], day=None),
    MenuItem(dish=dishes[u"Chili"], day=None, variants={"hannah": 1}),
    ]

translations = [
    ("kilogram","kg"),
    ("count", "st"),
    ("deciliter", "dl"),
    ("gram", "g")
    ]

prebought = [
                Ingredient(name=u"Korvpålägg, skivor", quantity=50*units.count),
                Ingredient(name=u"Köttpålägg, skivor", quantity=175*units.count),
                Ingredient(name=u"Kycklingfilé", quantity=5*units.kilogram),
                Ingredient(name=u"Sill, burk, blandat",  quantity=8 * units.count),
                Ingredient(name=u"Vetemjöl",             quantity=3.75 * units.deciliters),
            ]

buy_later = [
                Ingredient(name=u"Ägg",                  quantity=90 * units.count),                
                Ingredient(name=u"Mjölk",                quantity=11 * units.liters),
                Ingredient(name=u"Bröd, ljust, skivor",  quantity=40 * units.count),                
                Ingredient(name=u"Lax",                  quantity=150 * 40 * units.gram),
             ]
