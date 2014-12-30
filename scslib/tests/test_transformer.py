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
        self.assertEqual(len(transformer.shortcodes), 8)


if __name__ == '__main__':
    unittest.main()
