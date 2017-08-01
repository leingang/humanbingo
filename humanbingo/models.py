# -*- coding: utf-8 -*-

"""Abstract models for Human Bingo."""
from collections import namedtuple


class Card(object):
    """A single bingo card"""

    cells = None
    """A 5x5 list of lists of bingo card cells.  Each list is one row."""
    
    def __init__(self, cells=None):
        """Constructor"""
        self.cells = cells


class CardSetSpec(namedtuple('CardSetSpec',
                             ['name', 'instructions', 'categories',
                              'category_values', 'free_space_value'])):
    """Specifications for a set of bingo cards.

    Objects of this class are *immutable.*

    Attributes:
        name (string): The title on the cards (e.g., 'Human Bingo')
        instructions (string): Instructions to go below the title and
            above the grid.
        categories (list): the names of the columns.
        category_values (dict of lists): the values that can appear in
            the cells below each column
        free_space_value (string): the value in the "free space" in the
            center of the card.
    """
    pass


def card(spec):
    """Create a card.

    Args:
        spec (CardSetSpec): the data describing the card

    Returns:
        Card: An instance of :class:`Card` with cells randomly
              populated.
    """
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
    return Card(cells=cells)
