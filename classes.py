# -*- coding: utf-8 -*-
from functools import total_ordering


@total_ordering
class DataObject(object):
    def __init__(self, base=None, **kwargs):
        self.__notkeys = set(self.__dict__.keys())
        self.__notkeys.add("_DataObject__notkeys")
        self.__dict__.update(self.__class__.defaults)
        if not base is None:
            self.__dict__.update(base._items())
        self.__dict__.update(kwargs)

    def __str__(self):
        return (
            self.__class__.__name__
            + "("
            + ",".join(["%s=%r" % i for i in self._items()])
            + ")"
        )

    def __repr__(self):
        return (
            self.__class__.__name__
            + "("
            + ",".join(["%s=%r" % i for i in self._items()])
            + ")"
        )

    def __lt__(self, other):
        if (
            not isinstance(other, DataObject)
            or self.__class__.sort_by != other.__class__.sort_by
        ):
            raise TypeError(f"Cannot compare {self.__class__ and other.__class__}")

    def __eq__(self, other):
        if (
            not isinstance(other, DataObject)
            or self.__class__.sort_by != other.__class__.sort_by
        ):
            raise TypeError(f"Cannot compare {self.__class__ and other.__class__}")
        sort_by = self.__class__.sort_by
        return getattr(self, sort_by) != getattr(other, sort_by)

    def _items(self):
        for k, v in self.__dict__.items():
            if k not in self.__notkeys:
                yield k, v

    defaults = {}


class Ingredient(DataObject):
    sort_by = "name"
    pass


class Dish(DataObject):
    defaults = {"variants": {}}
    pass


class MenuItem(DataObject):
    defaults = {"variants": {}}


class NameDict(dict):
    """A dictionary whose constructor accepts an iterable of objects
    that has a name property. This name property becomes the keys in
    the dictionary. The objects are the values"""

    def __init__(self, iterable=[]):
        dict.__init__(self, ((x.name, x) for x in iterable))

    def append(self, obj):
        if obj.name in self:
            raise KeyError("%s already in dict" % obj.name)
        self[obj.name] = obj
