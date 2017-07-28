# -*- coding: utf-8 -*-

"""Console script for humanbingo."""

import click
import logging
import sys

from humanbingo import EventsParser, BingoCard, BingoCardWriter
from xml.sax import parse


@click.command()
@click.argument('infile', type=click.File('rb'),
                metavar='CARDSETFILE')
@click.option('-d', '--debug',
              'loglevel',
              flag_value=logging.DEBUG,
              help='Print lots of debugging statements')
@click.option('-v', '--verbose',
              'loglevel',
              flag_value=logging.INFO,
              help='Be verbose')
@click.option('-n', '--number',
              metavar='NUMBER', type=int,
              help='generate and save NUMBER cards')
def main(infile, number, loglevel=logging.WARNING):
    """Console script for humanbingo."""
    logging.basicConfig(level=loglevel)
    handler = EventsParser(sys.stdout)
    logging.info("Parsing {} ...".format(infile))
    parse(infile, handler, handler)
    logging.info("... done parsing")
    cardwriter = BingoCardWriter()
    if number:
        for i in range(1, number + 1):
            outputFileName = "card%02d.html" % i
            card = BingoCard(handler.events)
            logging.info("Writing card {}.".format(outputFileName))
            cardwriter.writeToFile(card, outputFileName)
    else:
        # just do one and print to stdout
        card = BingoCard(handler.events)
        print(cardwriter.toString(card))

if __name__ == "__main__":
    main()
