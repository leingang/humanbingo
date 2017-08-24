# -*- coding: utf-8 -*-

"""Objects to handle writing bingo cards to files."""

import io
import logging

import weasyprint


class CardWriter(object):
    """Abstract writer object"""

    def write(self, card, destination):
        """Write a single card.

        This abstract method must be implemented in descendants.

        Args:
            card (models.Card): card to be written
            destination (string or file-like object): where to write the card.
                If a string is passed, it will be treated as a path name and
                opened for writing.  To write to stdout, pass
                :obj:`sys.stdout`. To save output as a variable, pass an
                instance of :class:`io.StringIO`.

        Returns:
            None
        """
        raise NotImplementedError


class HtmlWriter(CardWriter):
    """Writer object for HTML files

    Uses Jinja2_ templating to generate HTML.
    The default template (minus CSS) looks something like this:

    .. code-block:: html

        <html>
        <head>
            <title>{{ title }}</title>
        </head>
        <body>
        <h1>{{ title }}</h1>
        
        {%- for para in instructions %}
        <p>{{ para }}</p>
        {%- endfor %}

        <table id="bingoCard">
            <tr>
                {%- for category in card.spec.categories %}
                <th>{{ category }}</th>
                {%- endfor %}
            </tr>
            {%- for row in card.cells %}
            <tr>
                {%- for cell in row %}
                <td>{{ cell }}</td>
                {%- endfor %}
            </tr>
            {%- endfor %}
        </table>
        </body>
        </html>

    .. _Jinja2: http://jinja.pocoo.org/docs/2.9/    
    """  # noqa

    _template = None

    def __init__(self, template_path='card_tpl.html'):
        """Constructor

        Args:
            template_path (string): Path to the template to be used.
                The default is in the package resources as
                :code:`templates/card_tpl.html`.  A user template can
                be specified; it should use the variable :code:`card`.
        """
        from jinja2 import Environment, PackageLoader, select_autoescape
        env = Environment(loader=PackageLoader('humanbingo', 'templates'),
                          autoescape=select_autoescape(['html', 'xml']))
        self._template = env.get_template(template_path)

    def write(self, card, destination):
        """Implementation of :meth:`CardWriter.write`"""
        template_vars = {
            'card': card,
            'title': card.spec.name,
            'instructions': card.spec.instructions.split('\n\n')
        }
        logging.debug('card: %s', card)
        html = self._template.render(template_vars)
        try:
            destination.write(html)
        except AttributeError:
            with open(destination, 'w') as f:
                f.write(html)


class PdfWriter(HtmlWriter):
    """Writer object for PDFs

    Uses Jinja2_ to create a temporary HTML object,
    then WeasyPrint_ to generate PDF.

    .. _WeasyPrint: http://weasyprint.org/
    """

    def write(self, card, destination):
        buf = io.StringIO()
        super(PdfWriter, self).write(card, buf)
        logging.debug('buf: %s', buf.getvalue())
        html = weasyprint.HTML(string=buf.getvalue())
        buf.close()
        html.write_pdf(destination)
