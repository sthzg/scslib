# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
from scslib import registry
from types import ModuleType


class RegistryTestCase(unittest.TestCase):
    def test_register_bundle_is_of_module_type(self):
        """Imported bundles are of ``ModuleType``."""
        registry.register_bundle('scslib.tests.shortcodes')
        test_bundle = registry.registered_bundles.get('test_bundle')
        self.assertEqual(isinstance(test_bundle, ModuleType), True)

    def test_register_bundle_raises_type_error(self):
        """Registration raises ``TypeError`` when module is no bundle."""
        with self.assertRaises(TypeError):
            registry.register_bundle('re')

    def test_register_shortcodes(self):
        """All shortcodes are registered in ``registered_shortcodes``."""
        registry.register_bundle('scslib.tests.shortcodes')
        registry.register_shortcodes()
        self.assertEqual(len(registry.registered_shortcodes), 1)
        self.assertEqual('TestShortcode' in registry.registered_shortcodes.keys(), True)


if __name__ == '__main__':
    unittest.main()
