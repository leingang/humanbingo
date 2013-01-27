namebingo
=========

Make "Name Bingo" cards

Synopsis
--------

This is an icebreaker game to play on the first day of class.  See [About.com](http://adulted.about.com/od/icebreakers/qt/peoplebingo.htm)
for a reference.

History
-------

Derek Bruff wrote a ColdFusion script to create bingo pages as HTML in 2006.  I (MPL)
used it as an excuse to learn python.  I have been using it since 2007, and finally uploaded to github in 2013.

Usage
-----

Read events XML file as argument.  If the `-n` or `--number` option is not specified, 
writes one bingo card as HTML to stdout.  If `-n NUMBER` or `--number=NUMBER` is 
specified, writes NUMBER cards to separate HTML files.

To easily print these cards, they can be converted to PDF and concatenated.  The [`wkdpdf`](http://plessl.github.com/wkpdf/)
command-line utility can be used for the form and [`pdftk`](http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) for the latter:

    $ for file in `ls card*.html`; do
      /path/to/wkpdf --source=$file --output=`basename $file .html`.pdf
    done
    $ /path/to/pdftk card*.pdf cat output allcards.pdf


TODO
----

* Template HTML file
* customize file name format

