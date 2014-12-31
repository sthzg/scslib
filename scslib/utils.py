# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import re


def camelize(value):
    """Converts the input string to camel case notation.

    Supports strings separated by hyphens (-) and underscores (_).

    Ex:

        camelize('foo')          # output: Foo
        camelize('foo-bar-bam')  # output: FooBarBam
        camelize('foo_bar_bam')  # output: FooBarBam

    :param value: string to convert to camel case
    :type value: str or unicode
    :returns: camel-case formatted string
    :rtype: str or unicode
    """
    # TODO(sthzg) Currently unused, but left in because it might become useful.
    camel = re.sub(r'(?!^)[-|_]([a-zA-Z])', lambda m: m.group(1).upper(), value)
    return ''.join([camel[0].upper(), camel[1:]])