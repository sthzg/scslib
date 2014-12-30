# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import scslib
import unittest


class UtilsTestCase(unittest.TestCase):
    def test_camelize_simple(self):
        """Camel case conversion for one-word-token is built correctly."""
        cname = scslib.camelize('foo')
        self.assertEqual(cname, 'Foo')

    def test_camelize_hyphenated(self):
        """Camel case conversion for hyphenated token is built correctly."""
        cname = scslib.camelize('foo-bar-bam')
        self.assertEqual(cname, 'FooBarBam')

    def test_camelize_underscored(self):
        """Camel case conversion for underscored token is built correctly."""
        cname = scslib.camelize('foo_bar_bam')
        self.assertEqual(cname, 'FooBarBam')


if __name__ == '__main__':
    unittest.main()
