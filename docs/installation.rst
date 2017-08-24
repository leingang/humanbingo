.. highlight:: shell

============
Installation
============

Environment
-----------

When installing software, you typically have two choices: install as root,
or install as user in your own user space.  You may only have one choice
if you don't have root privileges on your machine.

If you want to install :code:`humanbingo` in the system's executable domain,
you will probably need to preface any command below with :code:`sudo`.
If you already know what that means, proceed with caution.  If you don't,
consider one of the alternatives, which are designed to prevent you from
wrecking your system unintentionally.

To install in user space, you will need to add :code:`--user` to the
installation commands.  The install scripts will put the files in the 
places within your user directory that will automatically be searched.

But :code:`humanbingo` relies on other python packages to run correctly.
Installing :code:`humanbingo` will automatically download and install those
packages as well.  This can be trouble if you have other versions of
those packages already installed, and different modules require different
versions.

So as an alternative, python has *virtual environments.*  This is a way
to set up a complete python sandbox with packages and executables.  Here
is how to do that.

You should have a :code:`virtualenv` executable on your system.  Run 
it and give it the name of a directory, in which the environment will
reside:

.. code-block:: console

    $ virtualenv ~/Library/virtualenv/humanbingo

or, from another unix:

.. code-block:: console

    $ virtualenv ~/lib/virtualenv/humanbingo

Not sure of the best place for Windows.
This will give you a shiny new python installation that is independent 
from any others on your machine.  To activate it, change into the 
directory specified above and run:

.. code-block:: console

    $ source bin/activate
    (humanbingo)$ which python
    ...

Notice how the prompt changes to indicate the active virtual environment.
Your :code:`which` command should return the directory of your virtual 
environment, with :code:`bin/python` attached.

You can learn more about this from the `Virtualenv user guide`_.
Trust me, it's worth it.

.. _Virtualenv user guide: https://virtualenv.pypa.io/en/stable/userguide/


Stable release
--------------

To install Human Bingo, run this command in your terminal:

.. code-block:: console

    $ pip install humanbingo

Along with using a virtual environment as above, is the preferred method to 
install Human Bingo, as it will always install the most recent stable release. 

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for Human Bingo can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/leingang/humanbingo

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/leingang/humanbingo/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/leingang/humanbingo
.. _tarball: https://github.com/leingang/humanbingo/tarball/master
