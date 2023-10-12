.. image:: https://github.com/icemac/icemac.wsgi.wsgiref/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/icemac/icemac.wsgi.wsgiref/actions/workflows/tests.yml

.. image:: https://coveralls.io/repos/github/icemac/icemac.wsgi.wsgiref/badge.svg?branch=master
   :target: https://coveralls.io/github/icemac/icemac.wsgi.wsgiref?branch=master

.. image:: https://readthedocs.org/projects/icemacwsgiwsgiref/badge/?version=latest
   :target: https://icemacwsgiwsgiref.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/icemac.wsgi.wsgiref.svg
   :target: https://pypi.org/project/icemac.wsgi.wsgiref/
   :alt: Current version on PyPI

.. image:: https://img.shields.io/pypi/pyversions/icemac.wsgi.wsgiref.svg
   :target: https://pypi.org/project/icemac.wsgi.wsgiref/
   :alt: Supported Python versions


=====================
 icemac.wsgi.wsgiref
=====================

This package provides a PasteDeploy-compatible entry point to easily integrate
the `wsgiref WSGI server <https://docs.python.org/3/library/wsgiref.html>`_
into an environment that uses PasteDeploy-style ``.ini`` files to compose a
WSGI application.

It also includes a script to create a basic WSGI configuration file for Zope,
similar to Zope's own ``mkwsgiinstance``, but specifying ``wsgiref`` instead of
``waitress`` as WSGI server.
