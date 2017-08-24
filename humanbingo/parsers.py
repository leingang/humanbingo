# -*- coding: utf-8 -*-

"""Parsers for Human Bingo."""

import logging
import xml.sax

from humanbingo.models import CardSetSpec


class CardSetSpecParser(object):
    """Parses a file to produce a :class:`CardSetSpec`"""

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
    an XML file, such as (abbreviated):

    .. code-block:: xml

        <?xml version="1.0"?>
        <events xmlns="http://www.math.harvard.edu/~leingang/2007/06/25/S-1ab/Icebreaker">
        <category name="Origin">
            <event>United States midwest</event>
            <event>United States east coast</event>
            <event>United States west coast</event>
            <!-- ... -->
        </category>
        <category name="Housing">
            <event>Founders Hall</event>
            <event>Goddard</event>
            <event>Hayden Hall</event>
            <!-- ... -->
        </category>
        <category name="Math">
            <event>has taken AP Calculus BC</event>
            <event>took calculus more than one year ago</event>
            <event>is math anxious</event>
            <event>thinks math is cool</event>
            <!-- ... -->
        </category>
        <!-- ... -->
        </events>

    In version 2.1 extra properties are to be added to allow more
    customization within the specification file.  To preserve backwards
    compatibility, values which were originally hardcoded will be supplied as
    defaults.
    """  # noqa
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
        "Handle an XML end tag"
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

    *New in version 2.1* To make card sets easier to specify, a YAML
    format is implememented.  In addition, new specification properties
    are added which allow all data to be kept in the specification file.

    Example YAML file (abbreviated):

    .. code-block:: yaml

        name: Human Bingo
        instructions: |
          Find people in the class (other than yourself) who match the descriptions
          in each box; write their name in the box.

          Try to fill as many boxes as possible (one box per person). Five in a row wins!
        properties: !!omap
        # First-level item keys are the category names
        # Second-level items are the values for those categories
        - Origin:
            - New York City
            - New Jersey
            - US East Coast
            - US West Coast
            - US Midwest
            - US South
            # ...
        - Housing:
            # First Year Halls
            - Brittany Hall
            - Founders Hall
            - Goddard Hall
            # ...
        - Math:
            - thinks that math is cool
            - thinks that math is for losers
            - is required to take this class
            - is math anxious
            # ...
        - Interests:
            # ...
        - Potpourri:
            - has a blog
            - has a Windows Phone
            - has a fidget spinner
            # ...
        free_space_value: Wants to get an A in this class

    The :code:`|` allows for multi-line instructions, separated by double-newlines.
    Notice also the :code:`!!omap` declaration and syntax. 
    This allows for the columns (categories) to be unambigiously ordered
    and keys for the :code:`category_values` property of the
    :class:`CardSetSpec` record.
    """  # noqa
    def parse(self, file):
        """YAML implementation of the abstract method :func:`CardSetSpecParser.parse`
        """
        from ruamel.yaml import YAML
        yaml = YAML()
        rec = yaml.load(file)
        logging.debug("rec: %s", rec)
        categories = rec['properties'].keys()
        category_values = dict(rec['properties'])
        return CardSetSpec(
            name=rec['name'],
            instructions=rec['instructions'],
            categories=categories,
            category_values=category_values,
            free_space_value=rec['free_space_value']
        )
        
