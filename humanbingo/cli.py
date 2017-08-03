# -*- coding: utf-8 -*-

"""Console script for humanbingo."""

import click
import logging
import sys

from humanbingo.application import Application
from humanbingo.models import get_card


@click.command()
@click.argument('infile', type=click.File('rb'),
                metavar='CARDSETFILE')
@click.option('-d', '--debug',
              'log_level',
              flag_value=logging.DEBUG,
              help='Print lots of debugging statements')
@click.option('-v', '--verbose',
              'log_level',
              flag_value=logging.INFO,
              help='Be verbose')
@click.option('-n', '--number',
              metavar='NUMBER', type=int,
              help='generate and save NUMBER cards')
@click.option('-f', '--input-format',
              type=click.Choice(['xml', 'yaml']),
              default='xml',
              help="Input file format")
@click.option('-F', '--output-format',
              type=click.Choice(['html', 'pdf']),
              default='html',
              help="Output file format")
def main(infile, number, input_format, output_format='html',
         log_level=logging.WARNING):
    """Console script for humanbingo."""
    logging.basicConfig(level=log_level)
    app = Application(log_level=log_level,
                      number=number,
                      input_format=input_format,
                      output_format=output_format,
                      infile=infile)
    parser = app.get_parser()
    spec = parser.parse(infile)
    writer = app.get_writer()
    if number:
        for i in range(1, number + 1):
            output_path = "card%02d.html" % i
            card = get_card(spec)
            logging.info("Writing card {}.".format(output_path))
            writer.write(card, output_path)
    else:
        # just do one and print to stdout
        card = get_card(spec)
        writer.write(card, sys.stdout)


if __name__ == "__main__":
    main()
