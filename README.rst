================
 Dictnodefinder
================

About
=====

Dictnodefinder is a helper module that helps you to find keys in nested dictionary.


Installation
============

Dictnodefinder is on PyPI so all you need is: ::

    pip install dictnodefinder


Usage
============

	import dictnodefinder

	source = {'a':{'b':0}}
	
	key_to_find = 'b'

	print(dictnodefinder.findkeys(source, key_to_find))
