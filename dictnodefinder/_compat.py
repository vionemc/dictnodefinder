# This file is part of Dictnodefinder.
#
# Copyright (C) 2020, Aminah Nuraini.
#
# Dictnodefinder is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more
# details.

"""Python compatibility definitions."""

try:
    PY2 = True
    string_types = basestring,
    text_type = unicode
    num_types = int, long, float
except NameError:
    PY2 = False
    string_types = str,
    text_type = str
    num_types = int, float

if PY2:
    from collections import (
        MutableMapping, MutableSequence)
else:
    from collections.abc import (
        MutableMapping, MutableSequence)

