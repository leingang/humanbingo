# -*- coding: utf-8 -*-

"""Abstract models for Human Bingo."""
from collections import namedtuple
import random


class Card(object):
    """A single bingo card
    
    Attributes:
        spec (CardSetSpec): a card set specification record
        cells (list): A 5x5 list of lists of bingo card cells.
            Each list is one row
    """

    def __init__(self, spec, cells=None):
        """Constructor"""
        self.spec = spec
        self.cells = cells

    def __repr__(self):
        return "<humanbingo.models.Card object spec={}, cells={}>"\
            .format(self.spec, self.cells)


class CardSetSpec(namedtuple('CardSetSpec',
                             ['name', 'instructions', 'categories',
                              'category_values', 'free_space_value'])):
    """Specifications for a set of bingo cards.

    Objects of this class are *immutable.*

    Attributes:
        name (string): The title on the cards (e.g., 'Human Bingo')
        instructions (string): Instructions to go below the title and
            above the grid.Paragraphs can be separated by double-newlines
        categories (list): the names of the columns.
        category_values (dict of lists): the values that can appear in
            the cells below each column
        free_space_value (string): the value in the "free space" in the
            center of the card.
    """
    pass


class CardGenerator(object):
    """Generates an iterable of cards

    Attributes:
        spec (CardSetSpec): the data describing the cardset
        number (int): the number of cards to be generated
    """

    def __init__(self, number=None):
        if number is None:
            number = 1
        self.number = number

    def cards(self, spec):
        """generate the cards

        Args:
            spec (CardSetSpec): the data describing the card

        Yields:
            :class:`humanbingo.models.Card`: cards with cells randomly populated
        """
        for i in range(1, self.number+1):
            cells = []
            cellst = []
            for category in spec.categories:
                cellst.append(random.sample(spec.category_values[category], 5))
            # transpose cells
            for i in range(0, 5):
                cells.append([None, None, None, None, None])
                for j in range(0, 5):
                    cells[i][j] = cellst[j][i]
            # free space
            cells[2][2] = spec.free_space_value
            yield Card(spec, cells)
