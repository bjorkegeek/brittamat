from typing import cast

from pint import UnitRegistry, Unit


class WrappedUnitRegistry:
    """Properly typed version of UnitRegistry with the units that we use"""

    def __init__(self):
        self._backend = UnitRegistry()
        self.kilogram = cast(Unit, self._backend.kilogram)
        self.kilograms = cast(Unit, self._backend.kilograms)
        self.meters = cast(Unit, self._backend.meters)
        self.liters = cast(Unit, self._backend.liters)
        self.liter = cast(Unit, self._backend.liter)
        self.litres = cast(Unit, self._backend.litres)
        self.litre = cast(Unit, self._backend.litre)
        self.deciliters = cast(Unit, self._backend.deciliters)
        self.deciliter = cast(Unit, self._backend.deciliter)
        self.decilitres = cast(Unit, self._backend.decilitres)
        self.decilitre = cast(Unit, self._backend.decilitre)
        self.centiliters = cast(Unit, self._backend.centiliters)
        self.centiliter = cast(Unit, self._backend.centiliter)
        self.centilitres = cast(Unit, self._backend.centilitres)
        self.centilitre = cast(Unit, self._backend.centilitre)
        self.milliliters = cast(Unit, self._backend.milliliters)
        self.milliliter = cast(Unit, self._backend.milliliter)
        self.millilitres = cast(Unit, self._backend.millilitres)
        self.millilitre = cast(Unit, self._backend.millilitre)
        self.meter = cast(Unit, self._backend.meter)
        self.cups = cast(Unit, self._backend.cups)
        self.ounce = cast(Unit, self._backend.ounce)
        self.ounces = cast(Unit, self._backend.ounces)
        self.tablespoon = cast(Unit, self._backend.tablespoon)
        self.tablespoons = cast(Unit, self._backend.tablespoons)
        self.gram = cast(Unit, self._backend.gram)
        self.grams = cast(Unit, self._backend.grams)
        self.count = cast(Unit, self._backend.count)
        self.cm = cast(Unit, self._backend.cm)
