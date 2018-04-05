===============================
Python simple arp table reader
===============================

.. image:: https://img.shields.io/travis/XayOn/python_arptable.svg
        :target: https://travis-ci.org/XayOn/python_arptable

.. image:: https://img.shields.io/pypi/v/python_arptable.svg
        :target: https://pypi.python.org/pypi/python_arptable


Python simple arp table reader

* Free software: BSD license
* Documentation: https://python_arptable.readthedocs.org.

Features
--------

* Export ARP Table on linux as a dictionary.

Usage
-----

arp_table exports two main things:

* ARPTABLE constant, as it was when the package was imported
* get_arp_table() function, returning latest arp table.

::

    >>> from arp_table import ARPTABLE
    >>> print(ARPTABLE)

    [{'Device': 'eth0',
      'Flags': '0x2',
      'HW address': '00:12:79:d2:b9:67',
      'HW type': '0x1',
      'IP address': '10.3.0.1',
      'Mask': '*'}]

    >>> from arp_table import get_arp_table
    >>> print(get_arp_table())

    [{'Device': 'eth0',
      'Flags': '0x2',
      'HW address': '00:12:79:d2:b9:67',
      'HW type': '0x1',
      'IP address': '10.3.0.1',
      'Mask': '*'}]

Disclaimer
----------

This is a small, simple yet quite useful library.
I've seen a lot of posts of people struggling with arp-table reading
in python.

With this library, you can just

::

    pip install python_arptable

and enjoy!
