# -*- coding: utf-8 -*-

"""The application object for dependency injection"""

import humanbingo.parsers
import humanbingo.writers


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
        """Produce a :class:`humanbingo.Parser` object customized
        by application configuration"""
        parser_classes = {'xml': humanbingo.parsers.XmlParser,
                          'yaml': humanbingo.parsers.YamlParser}
        parser_class = parser_classes[self.input_format]
        # TODO: Inject application into parser?
        # might be needed to customize the template at runtime
        return parser_class()

    def get_writer(self):
        """Produce a :class:`humanbingo.Writer` object customized
        by application configuration"""
        return humanbingo.writers.HtmlWriter()
