# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import abc
import scslib
from bs4 import BeautifulSoup


class Transformer(object):
    def __init__(self, input_string=None, config=None):
        self.input_string = input_string
        self.soup = BeautifulSoup(input_string, 'html.parser')
        self.shortcodes = list()
        self.config = config or dict()

        # Default whitelisted shortcodes to all shortcodes available in the
        # registered bundles.
        whitelist = self.config.get('whitelist')
        if not whitelist and whitelist is None:
            self.config['whitelist'] = scslib.registered_shortcodes.keys()

    def run(self):
        """ Runs the transformer.
        """
        self.collect_shortcode_tokens()
        self.build_output()

    def collect_shortcode_tokens(self):
        """ Appends shortcodes from ``input_string`` to ``self.shortcodes``.

        Only shortcodes listed in the whitelist are processed. If no
        shortcode class is registered at `registered_shortcodes`
        the tag will be ignored.
        """
        whitelist = self.config.get('whitelist')
        matches = filter(lambda x: x.name in whitelist, self.soup.descendants)

        self.shortcodes = [
            self._instantiate_shortcode_class(sc)
            for sc in matches if sc.name in scslib.registered_shortcodes
        ]

        # TODO(sthzg) Notify users about whitelisted but unreg'ed descendants?

    def _instantiate_shortcode_class(self, shortcode):
        """ Instantiates an instance of a shortcode class.

        :param shortcode: beautiful soup ``Tag`` instance of the shortcode tag
        :type shortcode: bs4.element.Tag
        :returns: instance of shortcode class (descends from ``ShortcodeBase``)
        :rtype: ShortcodeBase
        """
        return scslib.registered_shortcodes[shortcode.name](
            shortcode,
            self.config.get('shortcodes', {}).get(shortcode.name)
        )

    def build_output(self):
        """ Apply transformations and replace with transformed output.
        """
        # TODO(sthzg) Will probably break with nested structures.
        for shortcode in self.shortcodes:
            if not shortcode: continue
            shortcode.transform()
            shortcode.token.replace_with(shortcode.output)


class ShortcodeBase(object):
    """ Abstract base class for shortcodes.

    Shortcode definition classes need to extend from `ShortcodeBase` to
    implement their behavior.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, token, config=None):
        self.token = token
        self.is_lookahead = False
        self.is_valid = False
        self.output = ''
        self.errors = list()
        self.config = config

    @abc.abstractmethod
    def validate(self):
        """ Abstract method `validate` must be implemented in subclass.

        Validation includes guarding the provided attributes
        a) in terms of type and range safety.
        b) in terms of completeness.

        Only when validation passes the shortcode is supposed to modify the
        input values to valid output.
        """

    @abc.abstractmethod
    def transform(self):
        """ Abstract method ``transform`` must be implemented in subclass.
        """


class ShortcodeConfigBase(object):
    """ Base class for shortcode configuration objects.
    """
    def __init__(self):
        pass
