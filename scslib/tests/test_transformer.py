# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
import scslib
from bs4 import BeautifulSoup
from scslib.tests.constants import *
from scslib.tests.shortcodes import TestShortcode


class TransformerTestCase(unittest.TestCase):
    def setUp(self):
        scslib.register_bundle('scslib.tests.shortcodes')
        scslib.register_shortcodes()

    def tearDown(self):
        pass

    def test_markup_in_soup(self):
        """Soup HTML in transformer is equal to source HTML."""
        soup = BeautifulSoup(TEST_STRING)
        transformer = scslib.Transformer(TEST_STRING)
        self.assertEqual(soup.prettify(), transformer.soup.prettify())

    def test_collect_shortcode_tokens(self):
        """Tags that are not on the whitelist are filtered from ``tokens``."""
        transformer = scslib.Transformer(TEST_STRING)
        transformer.collect_shortcode_tokens()
        self.assertEqual(len(transformer.shortcodes), 2)

    def test_overriding_whitelist_with_config(self):
        """Configuring an empty whitelist results in zero found shortcodes."""
        config = {'whitelist': list()}
        transformer = scslib.Transformer(TEST_STRING, config=config)
        transformer.collect_shortcode_tokens()
        self.assertEqual(len(transformer.shortcodes), 0)

    def test_build_output(self):
        """Output of test transformation is correct."""
        transformer = scslib.Transformer(TEST_STRING)
        transformer.collect_shortcode_tokens()
        transformer.build_output()
        expected = BeautifulSoup(TEST_STRING_RESULT).prettify()
        self.assertEqual(expected, transformer.soup.prettify())

    def test__instantiate_shortcode_class(self):
        """Method returns instance of appropriate shortcode class."""
        transformer = scslib.Transformer(TEST_STRING)
        transformer.collect_shortcode_tokens()
        shortcode = transformer.shortcodes[0].token
        sc_instance = transformer._instantiate_shortcode_class(shortcode)
        self.assertEqual(type(sc_instance), TestShortcode)

    def test__oc_shortcode(self):
        transformer = scslib.Transformer(TEST_OC_STRING)
        transformer.collect_shortcode_tokens()
        transformer.build_output()
        expected = BeautifulSoup(TEST_OC_STRING_RESULT).prettify()
        self.assertEqual(expected, transformer.soup.prettify())


if __name__ == '__main__':
    unittest.main()
