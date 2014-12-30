# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import abc
import scslib
from bs4 import BeautifulSoup


class Transformer(object):
    def __init__(self, input_string=None):
        self.input_string = input_string
        self.soup = BeautifulSoup(input_string, 'html.parser')
        self.shortcodes = list()

    def run(self):
        """Runs the transformer."""
        self.collect_shortcode_tokens()
        self.build_output()

    def collect_shortcode_tokens(self):
        """Appends shortcodes from ``input_string`` to ``self.shortcodes``.

        Only shortcodes provided by the whitelist are processed. If no
        shortcode class is registered at ``registered_shortcodes``
        None is appended and the shortcode tag will be ignored.
        """
        for child in self.soup.descendants:
            if child.name in scslib.get_tag_names_on_whitelist():
                try:
                    cname = '{}Shortcode'.format(scslib.camelize(child.name))
                    self.shortcodes.append(
                        scslib.registered_shortcodes[cname](child))
                except KeyError:
                    self.shortcodes.append(None)

    def build_output(self):
        """Apply transformations and replace with transformed output."""
        # TODO(sthzg) Will probably break with nested structures.
        for shortcode in self.shortcodes:
            if not shortcode: continue
            shortcode.transform()
            shortcode.token.replace_with(shortcode.output)

class ShortcodeBase():
    """Abstract base class for shortcodes.

    Shortcode definition classes need to extend from ``ShortcodeBase`` to
    implement their behavior.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, token):
        self.token = token
        self.is_lookahead = False
        self.is_valid = False
        self.output = ''
        self.errors = list()

    @abc.abstractmethod
    def validate(self):
        """Abstract method ``validate`` must be implemented in subclass.

        Validation includes guarding the provided attributes
        a) in terms of type and range safety.
        b) in terms of completeness.

        Only when validation passes the shortcode is supposed to modify the
        input values to valid output.
        """

    @abc.abstractmethod
    def transform(self):
        """Abstract method ``transform`` must be implemented in subclass."""
