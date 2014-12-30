# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
import scslib
from scslib.tests.constants import *


class TransformerTestCase(unittest.TestCase):
    def test_collect_shortcode_tokens(self):
        """Tags that are not on the whitelist are filtered from ``tokens``."""
        transformer = scslib.Transformer(TEST_STRING)
        transformer.collect_shortcode_tokens()
        self.assertEqual(len(transformer.shortcodes), 6)

    def test_build_shortcode_class_name_simple(self):
        """Class name for one word shortcode tag is built correctly."""
        cname = scslib.Transformer.build_shortcode_class_name('foo')
        self.assertEqual(cname, 'FooShortcode')

    def test_build_shortcode_class_name_hyphenated(self):
        """Class name for hyphenated shortcode tag is built correctly."""
        cname = scslib.Transformer.build_shortcode_class_name('foo-bar-bam')
        self.assertEqual(cname, 'FooBarBamShortcode')

    def test_build_shortcode_class_name_underscored(self):
        """Class name for underscored shortcode tag is built correctly."""
        cname = scslib.Transformer.build_shortcode_class_name('foo_bar_bam')
        self.assertEqual(cname, 'FooBarBamShortcode')


if __name__ == '__main__':
    unittest.main()
