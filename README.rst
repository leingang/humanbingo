===========
Human Bingo
===========


.. image:: https://img.shields.io/pypi/v/humanbingo.svg
        :target: https://pypi.python.org/pypi/humanbingo

.. image:: https://img.shields.io/travis/leingang/humanbingo.svg
        :target: https://travis-ci.org/leingang/humanbingo

.. image:: https://readthedocs.org/projects/humanbingo/badge/?version=latest
        :target: https://human-bingo.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/leingang/humanbingo/shield.svg
     :target: https://pyup.io/repos/github/leingang/humanbingo/
     :alt: Updates


Create cards for the "Human Bingo" icebreaker game, with customizable 
properties and templating.

Synopsis
--------

This is an icebreaker game to play on the first day of class.  See 
`About.com`_ or `WikiHow`_ for references.

.. _`About.com`: http://adulted.about.com/od/icebreakers/qt/peoplebingo.htm
.. _`WikiHow`: http://www.wikihow.com/Play-Human-Bingo

Features
--------

* Read XML and YAML files
* Write HTML and PDF files


Usage
-----

The package includes a script :code:`humanbingo`.  Call it like this::

    $ humanbingo [-n|--number NUM]
        [-v|--verbose]
        [-d|--debug]
        [-o|--output] OUTPUTFILE        
        [-f|--input-format] (xml|yaml) 
        [-F|--output-format] (html)
        INPUTFILE

Read properties file as its sole argument.  If neither :code:`-n` or 
:code:`--number` option is not specified, write one bingo card.  
If :code:`-n NUMBER` or :code:`--number=NUMBER` is 
specified, writes NUMBER cards to separate files.

To easily print these cards, they can be converted to PDF and concatenated.  
The `wkpdf`_ command-line utility can be used for the form and `pdftk`_ 
for the latter::

    $ for file in `ls card*.html`; do
      /path/to/wkpdf --source=$file --output=`basename $file .html`.pdf
    done
    $ /path/to/pdftk card*.pdf cat output allcards.pdf

.. _`wkpdf`: http://plessl.github.com/wkpdf/
.. _`pdftk`: http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/

Eventually a PDF writer will be included, to be specified in the 
:code:`--output-format` option.

* Free software: MIT license
* Documentation: https://human-bingo.readthedocs.io.

TODO
----

* Write YAML parser
* Write PDF writer

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

