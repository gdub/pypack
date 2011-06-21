================================
python-package-template (pypack)
================================

Provides a command to easily create a standard Python package layout (i.e.
README, package directory, etc.), following the `Hitchhiker's Guide to
Packaging`_.

.. _Hitchhiker's Guide to Packaging: http://guide.python-distribute.org/


Features
========
* Creates a complete Python package template, ready for creating distribution
  files and uploading to the `Python package index (PyPI)`_.
* Uses Distribute by default.
* MANIFEST.in template, with inclusion of README and other standard files, as
  well as ignoring of ``dist/`` directory that gets created when building the
  the package's distribution files.
* No external dependencies, only relies on Python standard library.

.. _Python package index (PyPI): http://pypi.python.org/


Quickstart
==========
#. Run ``pypack``, specifying the name of your new package (optionally, use
   command line options to provide additional information, see ``pypack -h``).
   
   a) If you want to create a new Python package in an existing directory,
      just specify the desired Python package name::
      
          pypack mynewpackage
          
   b) If you want to specify different directory, you may optionally use the
      ``-t`` (or ``--target``) option to specify a target, non-existent
      directory::

          pypack mynewpackage -t /new/path

#. Review/edit the generated files
#. Add your code, documentation, etc.
#. Create distribution tarball::

       cd mynewpackage
       python setup.py sdist

#. Register project on PyPI::

       python setup.py register

#. Upload to PyPI::

       python setup.py sdist upload


Download
========
* PyPI: http://pypi.python.org/pypi/python-package-template/
* Source: https://bitbucket.org/gdub/python-package-template/


TODO
====
* Sphinx documentation layout, or at least an option to create a docs
  directory.
* Support for a license file, allowing selection from a list of common
  open-source license templates
* GitHub and Bitbucket compatibility for displaying readme file
* git/hg ignore files
* Allow use of config file to specify default options for author, license, etc.
* An interactive option that prompts for needed info.


Similar Projects
================
http://pypi.python.org/pypi/modern-package-template/
