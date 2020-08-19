==========
Dictnodefinder
==========
.. currentmodule:: dictnodefinder

Dictnodefinder is a helper module that helps you to diff and patch
dictionaries.

Installation
============

Dictnodefinder is on PyPI so all you need is:

.. code-block:: console

    $ pip install dictnodefinder


Usage
=====

Let's start with an example on how to find a key in a nested
dictionarie using :func:`.findkeys` method:

.. code-block:: python

    from dictnodefinder import findkeys

    source = {
        "title": "hello",
        "fork_count": 20,
        "stargazers": ["/users/20", "/users/30"],
        "settings": {
            "assignees": [100, 101, 201],
        }
    }

    result = findkeys(source, "assignees")

    assert result == [['settings','assignees']]

API
===

.. include:: ../CHANGES

License
=======

.. include:: ../LICENSE

.. include:: ../AUTHORS
