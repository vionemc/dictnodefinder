# This file is part of dictnodefinder.
#
# Copyright (C) 2020 Aminah Nuraini.
#
# dictnodefinder is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dictnodefinder is a helper module to find child keys in nested dictionaries."""

from copy import deepcopy

from ._compat import (PY2, MutableMapping, MutableSequence, string_types)
from .version import __version__

__all__ = ('findkeys', '__version__')

DICT_TYPES = (MutableMapping, )
LIST_TYPES = (MutableSequence, )
SET_TYPES = (tuple, )

def findkeys(source, key_to_find, dot_notation=True):
    """Find keys in a nested dictionary

    Return an iterator dictionary path

    >>> from dictnodefinder import findkeys
    >>> list(findkeys({'a': {'x': 1}}, {'a': {'x': 2}}))
    ['a.x']

    You can also use dot notation, but as long as all of the keys are strings

    >>> list(findkeys({'a': {'x': 1}}, {'a': {'x': 2}},
    ... dot_notation=False))
    [['a', 'x']]

    :param source: The target dictionary, ``list``, or ``set``
    :param key_to_find: A string of the dictionary key to find
    :param dot_notation: Boolean to toggle dot notation on and off.

    """

    def dotted(node, default_type=list):
        """Return dotted notation."""
        if dot_notation and \
            all(map(lambda x: isinstance(x, string_types) and '.' not in x,
                node)):
            return '.'.join(node)
        else:
            return default_type(node)

    def _find_recursive(_source, _key_to_find, _node=[]):        

        if isinstance(_source, (LIST_TYPES, SET_TYPES)):
            # Check what is inside the list or set if there is a dictionary.

            i = 0
            for item in _source:
                if isinstance(item, (DICT_TYPES, LIST_TYPES, SET_TYPES)):
                    recurred = _find_recursive(
                        _source[i], _key_to_find,
                        _node=_node + [i],
                    )

                    for found in recurred:
                        yield found
        elif isinstance(_source, DICT_TYPES):
            # Compare if object is a dictionary or list.
            #
            # Call again the parent function as recursive if dictionary have
            # child objects.  
            for key in _source.keys():
                if key == _key_to_find: yield dotted(_node + [key])
                recurred = _find_recursive(
                    _source[key], _key_to_find,
                    _node=_node + [key],
                )

                for found in recurred:
                    yield found

        elif not _node:
            # If the type is not a nested dictionary
            yield from []

    return list(_find_recursive(source, key_to_find))
