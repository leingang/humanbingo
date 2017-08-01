# -*- coding: utf-8 -*-

"""Parsers for Human Bingo."""


class CardSetSpecParser(object):
    """Parses a file to produce a :obj:`CardSetSpec`"""

    def __init__(self):
        pass

    def parse(self, file):
        """Parse a file.

        Args:
            file (string or file-like object): the file to be parsed

        Returns:
            CardSetSpec: the parsed specification
        """
        raise NotImplementedError


class XMLParser(CardSetSpecParser):
    """Parse an XML file.

    Up to version 2.0 the only way to specify card sets was through
    an XML file.  See :code:`events-121.xml` etc. for examples.

    In version 2.x extra properties are to be added to allow more
    customization within the specification file.  Values which were
    originally hardcoded will be supplied as defaults.
    """
    pass


class YAMLParser(CardSetSpecParser):
    """Parse a YAML file.

    New in version 2.x: To make card sets easier to specify, a YAML
    format is implememented.  In addition, new specification properties
    are added which allow all data to be kept in the specification file.
    """
    pass
