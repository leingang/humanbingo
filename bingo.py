#!/usr/bin/env python
"""Generate a bingo card for Icebreaking

Authors
=======

Derek Bruff and Matthew Leingang

Date
====
Created 2006-02-05.  Modified once or twice a year since then.

Usage
=====

Read event.xml file as argument, writes a bingo card to stdout.  If you want more than 
one, use the -n <number> option, and <number> files will be written.  They will have
file names of the form `card%02d.html` unless the -f/--format option is specified.
"""

import sys
import getopt
import re
import logging
import argparse
import random

from xml.sax import ContentHandler, parse, ErrorHandler


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
        pass

    def writeToFile(self, card, fileName):
        """Write card to file"""
        self.output = open(fileName, 'w')
        self.output.writelines(self.toString(card))

    def toString(self, card):
        """serialize card as string"""
        output = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
  <head>
    <title>Name Bingo</title>
    <style type="text/css">
      h1 p th td {
        font-family: Papyrus;
      }
      h1 {
        text-align: Center;
	font-family: "Comic Sans MS"
      }

      #bingoCard {
        margin-left:auto; margin-right:auto;
      }

      #bingoCard,tr,td {
        font-family: "Comic Sans MS";	
      }

      #bingoCard th, #bingoCard td {
        width: 20%;
      }
    </style>
  </head>
<body>
  <h1>Name Bingo</h1>
  
  <p>Find people in the class (other than yourself) who match the descriptions in each box; write their name in the box.</p>

  <p>Try to fill as many boxes as possible (one box per person). Five in a row wins!</p>

  <table border="2" cellspacing="0" cellpadding="4" align="center" id="bingoCard">
  
"""
        # top row is categories
        categories = card.categories
        output += "    <tr>\n"
        for category in categories:
            output += "      <th>%s</th>\n" % category
        output += "    </tr>\n"
        for row in card.cells:
            output += '    <tr>\n'
            for cell in row:
                output += '      <td width="120" height="120" align="center" valign="center">%s</td>\n' % cell
            output += "    </tr>\n"
        output += """  </table>
</body>
</html>
"""
        return output


def usage():
    print(main.__doc__)


def main():
    """Usage bingo.py [options]"""
    argparser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    argparser.add_argument('--verbose', help='be verbose',
                           action='store_const', const=logging.INFO, dest='debug_level',
                           default=logging.WARNING)
    argparser.add_argument('--debug', help='show debugging statements',
                           action='store_const', const=logging.DEBUG, dest='debug_level',
                           default=logging.WARNING)
    argparser.add_argument('-n', '--number', metavar='NUMBER', help='generate and save NUMBER cards',
                           action='store', dest='n', type=int)
    argparser.add_argument('eventfile', help='events XML file',
                           action='store',
                           default='events.xml')
    args = argparser.parse_args()
    logging.basicConfig(level=args.debug_level)
    handler = EventsParser(sys.stdout)
    parse(args.eventfile, handler, handler)
    cardwriter = BingoCardWriter()
    if args.n:
        for i in range(1, args.n + 1):
            outputFileName = "card%02d.html" % i
            card = BingoCard(handler.events)
            cardwriter.writeToFile(card, outputFileName)
    else:
        # just do one and print to stdout
        card = BingoCard(handler.events)
        print(cardwriter.toString(card))

if __name__ == "__main__":
    main()
