# -*- coding: utf-8 -*-
class DataObject(object):
    def __init__(self, base=None, **kwargs):
        self.__notkeys = set(self.__dict__.iterkeys())
        self.__notkeys.add("_DataObject__notkeys")
        self.__dict__.update(self.__class__.defaults)
        if not base is None:
            self.__dict__.update(base._items())
        self.__dict__.update(kwargs)

    def __str__(self):
        return self.__class__.__name__ + \
            "(" + ",".join(["%s=%r" % i for i in self._items()]) + ")"

    def __repr__(self):
        return self.__class__.__name__ + \
            "(" + ",".join(["%s=%r" % i for i in self._items()]) + ")"

    def __cmp__(self,o):
        sort_by = self.__class__.sort_by
        return cmp(getattr(self, sort_by), getattr(o, sort_by))

    def _items(self):
        for k,v in self.__dict__.iteritems():
            if k not in self.__notkeys:
                yield k,v
    
    defaults = {}

class Ingredient(DataObject):
    sort_by = "name"
    pass

class Dish(DataObject):
    defaults = { "variants": {} }    
    pass

class MenuItem(DataObject):
    defaults = { "variants": {} }

class NameDict(dict):
    """A dictionary whose constructor accepts an iterable of objects
    that has a name property. This name property becomes the keys in
    the dictionary. The objects are the values"""

    def __init__(self,iterable=[]):
        dict.__init__(self, ((x.name,x) for x in iterable))

    def append(self,obj):
        if obj.name in self:
            raise KeyError("%s already in dict" % obj.name)
        self[obj.name] = obj

