# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import abc
import re
import scslib
import sys
from bs4 import BeautifulSoup


class Transformer(object):
    def __init__(self, input_string=None):
        self.input_string = input_string
        self.soup = BeautifulSoup(input_string, 'html.parser')
        self.shortcodes = list()

    def collect_shortcode_tokens(self):
        """Creates list with all shortcodes from ``input_string``."""
        mod = sys.modules[__name__]
        for child in self.soup.descendants:
            if child.name in scslib.get_tag_names_on_whitelist():
                try:
                    cname = self.build_shortcode_class_name(child.name)
                    self.shortcodes.append(getattr(mod, cname)(child))
                except AttributeError:
                    self.shortcodes.append(None)

    @staticmethod
    def build_shortcode_class_name(tag_name):
        """Builds class name for shortcode class based on its tag name.

        :param tag_name: tag name of shortcode tag
        :type tag_name: str
        :returns: camel-case formatted string
        :rtype: str or unicode
        """
        camel = re.sub(r'(?!^)-([a-zA-Z])',
                       lambda m: m.group(1).upper(), tag_name)
        cname = '{}Shortcode'
        return cname.format(''.join([camel[0].upper(), camel[1:]]))


class ShortcodeBase():
    """Abstract base class for shortcodes."""
    __metaclass__ = abc.ABCMeta

    def __init__(self, token):
        self.token = token
        self.is_lookahead = False
        self.is_valid = False
        self.output = ''

    @abc.abstractmethod
    def validate(self):
        """Abstract ``validate`` that must be implemented in subclass."""

    @abc.abstractmethod
    def transform(self):
        """Abstract ``transform`` that must be implemented in subclass."""