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

* Read cardset specifications as XML and YAML files.  The YAML specification is
  newer, more flexible, and easier to write.  The XML specification is older,
  and seemed like a good idea at the time.

* Write HTML and PDF files.  Since it's more likely the cards will be printed
  onto paper, the default is writing PDF.  Originally, only HTML files were 
  created, and PDF conversion was done by a third-party utility (wkhtmltopdf_).
  In version 3 the PDF writer was baked in. Since the PDF writer internally
  creates HTML first, the HTML feature is still maintained.

  .. _wkhtmltopdf: https://wkhtmltopdf.org/ 

Usage
-----

Installing the package exposes a script :code:`humanbingo`.  Call it like this::

    $ humanbingo [-n|--number NUM]
        [-v|--verbose]
        [-d|--debug]
        [-o|--output] OUTPUTFILE        
        [-f|--input-format] (yaml|xml) 
        [-F|--output-format] (pdf|html)
        INPUTFILE

Read properties file as its sole argument.  If neither :code:`-n` or 
:code:`--number` option is not specified, write one bingo card to stdout.  
If :code:`-n NUMBER` or :code:`--number=NUMBER` is 
specified, writes NUMBER cards to separate files.

.. warning::

    At this time writing PDF to stdout is not supported.  But you probably
    don't want to do that anyway.



To easily print the PDF cards, they can be concatenated with `pdftk`_::

    $ /path/to/pdftk card*.pdf cat output allcards.pdf

.. _`pdftk`: http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/

Documentation
-------------

See https://human-bingo.readthedocs.io.

License
-------

Free software: MIT license

Credits
-------

Human bingo relies on a lot of big python packages, heartily endorsed.

* Jinja2_ for templating
* Click_ for publishing command-line applications
* WeasyPrint_ for converting HTML to PDF

.. _Jinja2: http://jinja.pocoo.org/
.. _Click: http://click.pocoo.org/
.. _WeasyPrint: http://weasyprint.org/

We also use ruamel.yaml_ over PyYaml since it supports a few more features (notably,
the :code:`!!omap` sequence declaration).

.. _ruamel.yaml: https://yaml.readthedocs.io/en/latest/

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

