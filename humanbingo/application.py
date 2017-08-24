# -*- coding: utf-8 -*-

"""The application object for dependency injection"""

import sys

import humanbingo.parsers
import humanbingo.writers
import humanbingo.models


class Application(object):
    """The Human Bingo application"""
    
    def __init__(self, infile, log_level, input_format, output_format,
                 number):
        self.infile = infile
        self.log_level = log_level
        self.input_format = input_format
        self.output_format = output_format
        self.number = number

    def get_parser(self):
        """Produce a parser customized by application configuration
        
        Returns:
            :class:`humanbingo.parsers.Parser`
        """
        parser_classes = {'xml': humanbingo.parsers.XmlParser,
                          'yaml': humanbingo.parsers.YamlParser}
        parser_class = parser_classes[self.input_format]
        # TODO: Inject application into parser?
        # might be needed to customize the template at runtime
        return parser_class()

    def get_writer(self):
        """Produce a writer customized by application configuration
        
        Returns:
            :class:`humanbingo.writers.Writer`
        """
        writer_classes = {'html': humanbingo.writers.HtmlWriter,
                          'pdf': humanbingo.writers.PdfWriter}
        writer_class = writer_classes[self.output_format]
        # may need to pass some arguments to this constructor
        # at some point
        return writer_class()

    def get_generator(self):
        """Produce a card generator customized by application configuration
                    
        Returns:
            :class:`humanbingo.models.CardGenerator`
        """
        return humanbingo.models.CardGenerator(number=self.number)

    def get_destination(self, index=None):
        """Destination for a card, customized by application configuration.

        Args:
            index (int or None): index of the card in the sequence

        Returns:
            str or sys.stdout: the name of the file to be
            written, or sys.stdout if no file is to be written.
        """
        if self.number is None:
            return sys.stdout
        else:
            return "card%02d.%s" % (index, self.output_format)
