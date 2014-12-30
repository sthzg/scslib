# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from bs4 import BeautifulSoup
import scslib

BUNDLE_NAME = "test_bundle"


class TestShortcode(scslib.ShortcodeBase):
    """A dummy shortcode implementation for basic testing."""
    def __init__(self, *args, **kwargs):
        super(TestShortcode, self).__init__(*args, **kwargs)

    def validate(self):
        self.is_valid = True
        return self

    def transform(self):
        new_soup = BeautifulSoup('')
        new_tag = new_soup.new_tag('b')
        new_tag.string = 'Test transformed.'

        self.output = new_tag
        return self
