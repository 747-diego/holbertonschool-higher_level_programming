#!/usr/bin/python3
"""Write a class LockedClass with no class or object attribute."""


class LockedClass:
    """

    If defined in a class, __slots__ reserves space for the declared variables.

    AND prevents the automatic creation of

    __dict__ and __weakref__ for each instance.

    """

    __slots__ = "first_name"
