# -*- coding: utf-8 -*-

"""Parsers for Human Bingo."""

from humanbingo.models import CardSetSpec
import xml.sax


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


class XmlParser(CardSetSpecParser, xml.sax.ContentHandler):
    """Parse an XML file.

    Up to version 2.0 the only way to specify card sets was through
    an XML file.  See :code:`events-121.xml` etc. for examples.

    In version 2.x extra properties are to be added to allow more
    customization within the specification file.  Values which were
    originally hardcoded will be supplied as defaults.
    """
    _categories = []
    """list of category names"""

    _events = {}
    """dict of lists of category values, indexed by category name"""

    _current_text = ""
    """text buffer for the current category value"""

    _current_category = ""
    """register of the current category being appended to."""

    def startElement(self, name, attrs):
        "Handle an XML start tag"
        self.context = name
        if (name == "category"):
            self._current_category = attrs['name']
            self._categories.append(self._current_category)
            self._events[self._current_category] = []

    def characters(self, text):
        "Handle XML character data"
        self._current_text += text

    def endElement(self, name):
        "Hand an XML end tag"
        if (name == "event"):
            value = self._current_text.strip()
            self._events[self._current_category].append(value)
        self._current_text = ""

    def parse(self, file):
        """Parse a file.

        Args:
            file (string or file-like object): the file to be parsed

        Returns:
            CardSetSpec: the parsed specification
        """
        xml.sax.parse(file, self)
        return CardSetSpec(name="Human Bingo",
                           instructions="""Find people in the class (other than
                           yourself) who match the descriptions in each box;
                           write their name in the box.

                           Try to fill as many boxes as possible (one box per
                           person). Five in a row wins!
                           """,
                           categories=self._categories,
                           category_values=self._events,
                           free_space_value="Wants to get an A in this class")


class YamlParser(CardSetSpecParser):
    """Parse a YAML file.

    New in version 2.x: To make card sets easier to specify, a YAML
    format is implememented.  In addition, new specification properties
    are added which allow all data to be kept in the specification file.
    """
    pass
