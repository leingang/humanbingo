# -*- coding: utf-8 -*-

"""Top-level package for Human Bingo."""

import argparse
import getopt
import logging
import os.path
import random
from pkg_resources import resource_filename
import re
import sys

from jinja2 import Environment, PackageLoader, select_autoescape
from xml.sax import ContentHandler, parse, ErrorHandler

__author__ = """Matthew Leingang"""
__email__ = 'mleingang@gmail.com'
__version__ = '2.0.0'


class EventsParser(ContentHandler):

    def __init__(self, stream):
        self.stream = stream
        self.events = {}
        self.events['Categories'] = []
        self.currentText = ""
        self.currentCategory = ""

    def startElement(self, name, attrs):
        self.context = name
        if (name == "category"):
            self.currentCategory = attrs['name']
            self.events['Categories'].append(self.currentCategory)
            self.events[self.currentCategory] = []

    def characters(self, text):
        self.currentText += text

    def endElement(self, name):
        if (name == "event"):
            self.events[self.currentCategory].append(stripWS(self.currentText))
        self.currentText = ""


def stripWS(text):
    text = re.sub(re.compile(r"^\s*"), "", text)
    text = re.sub(re.compile(r"\s*$"), "", text)
    return text


class BingoCard:

    def __init__(self, events):
        """Constructor"""
        self.events = events
        self.categories = self.events['Categories']
        self.cells = []
        cellst = []
        for category in self.categories:
            cellst.append(random.sample(self.events[category], 5))
        # transpose cells
        for i in range(0, 5):
            self.cells.append([None, None, None, None, None])
            for j in range(0, 5):
                self.cells[i][j] = cellst[j][i]
        self.cells[2][2] = "wants to get an A in this class"


class BingoCardWriter:
    """Class to write Card to File"""

    def __init__(self):
        env = Environment(loader=PackageLoader('humanbingo', 'templates'),
                          autoescape=select_autoescape(['html', 'xml']))
        tpl_path = 'card_tpl.html'
        logging.debug("tpl_path: %s", tpl_path)
        self.template = env.get_template(tpl_path)
        pass

    def writeToFile(self, card, fileName):
        """Write card to file"""
        self.output = open(fileName, 'w')
        self.output.writelines(self.toString(card))

    def toString(self, card):
        """serialize card as HTML string"""
        template_vars = {
            'card': card
        }
        return self.template.render(template_vars)

