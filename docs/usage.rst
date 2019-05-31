=====
Usage
=====

Command-line application
------------------------

First, create the cardset specification file.  The recommended format is YAML.

Here is an example such file:

.. code-block:: YAML

    name: Human Bingo
    instructions: |
        Find people in the class (other than yourself) who match the descriptions
        in each box; write their name in the box.

        Try to fill as many boxes as possible (one box per person). Five in a row wins!
    properties: !!omap
    # First-level item keys are the category names
    # Second-level items are the values for those categories
    - Origin:
        - New York City
        - New Jersey
        - US East Coast
        - US West Coast
        - US Midwest
        - US South
        # ...
    - Housing:
        # First Year Halls
        - Brittany Hall
        - Founders Hall
        - Goddard Hall
        # ...
    - Math:
        - thinks that math is cool
        - thinks that math is for losers
        - is required to take this class
        - is math anxious
        # ...
    - Interests:
        # ...
    - Potpourri:
        - has a blog
        - has a Windows Phone
        - has a fidget spinner
        # ...
    free_space_value: Wants to get an A in this class

The package was created to create icebreaker activities in an undergraduate
math class. That is why the categories are related to math, or college, or
things college students may like to do.

You must have five categories; more or fewer is not supported at this time.
For each category, you must have at least five values.  A regular bingo card
has fifteen possible values (numbers) in each category (letter).  Feel free
to have many more values in a category (especially if they form a complete
list), but don't be so obscure that a particular card becomes impossible to
fill.

Save this into a file called, for instance, :code:`spec.yml`.

To make a single card file as PDF, use

.. code-block:: bash

    $ humanbingo -n 1 spec.yml

This will result in a file :code:`card01.pdf` in the same directory.

It's more fun if different people have different cards, though. So if
you have 20-30 people in the room, use

.. code-block:: bash

    $ humanbingo -n 30 spec.yml

and you will get 30 PDFs named :code:`card01.pdf` through :code:`card30.pdf`.

You can print those files individually, or, if you have the pdftk_ utility
installed, you can concatenate them all into a single file:

.. code-block:: bash

    $ /path/to/pdftk card*.pdf cat output allcards.pdf

Then print the one file.

.. _`pdftk`: http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/


As a python package
-------------------

To use Human Bingo in a project:

.. code-block:: python

    import humanbingo

See the package modules documentation for the full API.