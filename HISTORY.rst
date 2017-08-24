=======
History
=======

Version 3.0.1 (August 24, 2017)
-------------------------------

Updated history file for version 3.0.0.

Version 3.0.0 (August 24, 2017)
-------------------------------

Added the PDF writer.  Pass :code:`-F pdf` to explicitly write PDF files.

Backwards-incompatible changes: YAML input and PDF output are now default.

Improved refactoring and documentation.

Version 2.1.0 (August 4, 2017)
------------------------------

Added the ability to specify card sets with a YAML file instead of the
old XML format.  Pass :code:`-f yaml` to :code:`humanbingo`.

Lots of improvements to documentation.

Version 2.0.2 (August 3, 2017)
------------------------------

Pretty big refactoring into separate modules, in order to facilitate 
extensibility, practice dependency injections, etc.  But no functional
change yet.

Version 2.0.1 (July 28, 2017)
-----------------------------

Flesh out history file.

Version 2.0.0 (July 28, 2017)
-----------------------------

Name change: "Name Bingo" to "Human Bingo".  The latter sounds
more interesting and seems to be the more popular term.

Morphing this script into a bona fide python package to upload to PyPI.
Using the pypackage_ cookiecutter, add a :code:`setup.py` script so 
that it can be installed with pip_.

.. _pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _pip: https://pypi.python.org/pypi/pip

Now :code:`pip install` will install an executable file :code:`humanbingo`,
and the original :code:`bingo.py` module/script is gone.  So this is a
backwards-incompatible change.

Version 1.1.0 (July 26, 2017)
-----------------------------

* Port from Python 2.7 to 3.5
* Use the shell environment's python instead of a hardcoded one


Version 1.0.0 (January 27, 2013)
--------------------------------

* parse script arguments with argparse_
* get closer to POSIX compliant interface (print to stdout when only
  one card is needed)
* add a README
* upload to github

.. _argparse: https://docs.python.org/2/library/argparse.html#module-argparse

2007
----

MPL converted the ColdFusion script to python as an exercise.

2006
----

Derek Bruff wrote the original "Name Bingo" script in ColdFusion.
