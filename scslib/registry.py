# -*- coding: utf-8 -*-
"""
The registry module provides a singleton data store that can be used to
register shortcodes and shortcode bundles to the ``scslib``.
"""
from __future__ import absolute_import, unicode_literals
from collections import OrderedDict
import importlib
import inspect


ERR_BUNDLE_MODULE_TYPE = 'Shortcode bundle modules must provide a ' \
                         'BUNDLE_NAME variable.'


registered_bundles = OrderedDict()
registered_shortcodes = OrderedDict()


def register_bundle(path):
    """Appends bundle at ``path`` to the bundle registry.

    The key value is taken from the bundle module's ``NAME`` variable.
    If a bundle is already present the registry remains unchanged.

    :param path: python path to bundle module.
    :type path: str or unicode
    :raises: TypeError
    """
    bundle = importlib.import_module(path)

    if not hasattr(bundle, 'BUNDLE_NAME'):
        raise TypeError(ERR_BUNDLE_MODULE_TYPE)

    if bundle.BUNDLE_NAME not in registered_bundles.keys():
        registered_bundles[bundle.BUNDLE_NAME] = bundle


def register_shortcodes():
    """Extracts all shortcodes from registered bundles."""
    for bundle in registered_bundles:
        for name, obj in inspect.getmembers(registered_bundles[bundle]):
            cond1 = inspect.isclass(obj)
            cond2 = name.endswith('Shortcode')
            cond3 = name not in registered_shortcodes
            if cond1 and cond2 and cond3:
                registered_shortcodes[obj.shortcode] = obj
