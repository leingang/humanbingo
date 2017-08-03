# -*- coding: utf-8 -*-

"""Objects to handle writing bingo cards to files."""

import logging


class CardWriter(object):
    """Abstract writer object"""

    def write(self, card, destination):
        """Write a single card.

        Args:
            card (models.Card): card to be written
            destination (string or file-like object): file to be written.
                If a string is passed, it will be treated as a path name and
                opened for writing.  To write to stdout, pass
                :code:`sys.stdout`. To save output as a variable, pass an
                instance of :py:class:`StringIO`.

        Returns:
            void
        """
        raise NotImplementedError


class HtmlWriter(CardWriter):
    """Writer object for HTML files

    Uses Jinja2 templating to generate HTML.
    """

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
