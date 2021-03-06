"""
A class which allows a human-readable value in DB yet can be compared if one is
previous/post process of the another.

When an enum (of int) is used for a process status sotred in DB, this may allows
easier comparison check if the current status is previous status of another, yet
data is not understandable to whom having no access to enum definition. However,
by using this class, DB values can be human-readable yet can check the process
order of the current status.

For example,
```
class SomeChoices(OrderedChoices):
    READY = OrderedChoiceItem('ready', 0)
    SET = OrderedChoiceItem('set', 1)
    GO = OrderedChoiceItem('go', 2)
```
would make the values stored at DB being one of a string `ready`, `set`, 
or `go`, yet you can check if `current_status <= SomeChoices.go`.
"""
from typing import List, Tuple

from static_attr_object import StaticAttrObject


class OrderedChoiceItem:
    """Class for values in OrderedChoices class attributes
    """
    value = None

    def __init__(self, value):
        self.value = value


class _OrderedChoicesMetaClass(type):
    """Metaclass of OrderedChoices

    Automatically assign a str representation of each class attribute and store
    the order of those attributes.
    """
    pass


# TODO: remove StaticAttrObject inheritance
class OrderedChoices(StaticAttrObject, metaclass=_OrderedChoicesMetaClass):
    """Enum like data structure where the written order of members is used as a
    comparison factor
    
    Characteristics of this class:
        - value of each member is str representation of the member's name
        - the written order of members is used as the factor for a comparision
    """
    @classmethod
    def get_django_choices_input(cls) -> List[Tuple[str]]:
        """Return a list that can be used as an input of `choice` parameter of
        CharField in Django.
        """
        return list((attribute_name, ) for attribute_name in cls._get_attr_names())
