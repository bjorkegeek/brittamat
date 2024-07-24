# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import Optional, Protocol, TypeVar, Iterable

from pint import Quantity, Unit


@dataclass(kw_only=True, order=True)
class IngredientType:
    name: str
    purchase_unit: Optional[Unit] = None
    category: str
    conversions: list[Quantity] = field(default_factory=list)


@dataclass(kw_only=True, order=True, frozen=True)
class Ingredient:
    name: str
    quantity: Optional[Quantity]


@dataclass(kw_only=True, order=True)
class Dish:
    name: str
    ingredients: list[Ingredient]
    variants: dict[str, list[Ingredient]] = field(default_factory=dict)
    pass


@dataclass(kw_only=True)
class MenuItem:
    dish: Dish
    day: Optional[str] = None
    variants: dict[str, int] = field(default_factory=dict)


@dataclass(kw_only=True, order=True)
class ShoppingListEntry:
    name: str
    category: str
    quantity: Optional[Quantity]
    sources: list[MenuItem] = field(default_factory=list)


class Named(Protocol):
    name: str


T = TypeVar("T", bound=Named)


class NameDict(dict[str, T]):
    """A dictionary whose constructor accepts an iterable of objects
    that has a name property. This name property becomes the keys in
    the dictionary. The objects are the values"""

    def __init__(self, iterable: Iterable[T] = ()):
        super().__init__(((x.name, x) for x in iterable))

    def append(self, obj: T):
        if obj.name in self:
            raise KeyError("%s already in dict" % obj.name)
        self[obj.name] = obj
