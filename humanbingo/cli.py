# -*- coding: utf-8 -*-

"""Console script for humanbingo."""

import click
import logging
import sys

from humanbingo.application import Application

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
              default='yaml',
              help="Input file format")
@click.option('-F', '--output-format',
              type=click.Choice(['html', 'pdf']),
              default='pdf',
              help="Output file format")
def main(infile, number, input_format, output_format,
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
    generator = app.get_generator()
    writer = app.get_writer()
    for (i, card) in enumerate(generator.cards(spec), start=1):
        output = app.get_destination(i)
        writer.write(card, output)

if __name__ == "__main__":
    main()
