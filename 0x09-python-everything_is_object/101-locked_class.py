#!/usr/bin/python3
"""locked class"""


class LockedClass:
    """
    that prevent the user from instantiating new LockedClass attributes
    for anything but attributes called first_name
    """
    __slots__ = ["first_name"]
