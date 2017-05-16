Django Wiretap
==============

Captures HTTP requests & responses for debugging.

This is an early release, and is **not** suitable for production use.

|CILink|_

.. |CILink| image:: https://travis-ci.org/nathforge/django-wiretap.svg?branch=master
.. _CILink: https://travis-ci.org/nathforge/django-wiretap


Screenshots
-----------

List
^^^^

    .. image:: https://raw.githubusercontent.com/nathforge/django-wiretap/master/screenshot-list.png

View
^^^^

    .. image:: https://raw.githubusercontent.com/nathforge/django-wiretap/master/screenshot-view.png


Usage:
------

- Install the package with ``pip install django-wiretap``

- Edit Django settings:

  - Add ``'wiretap'`` to ``INSTALLED_APPS``.

  - Add ``'wiretap.middleware.WiretapMiddleware'`` to your
    ``MIDDLEWARE_CLASSES``.

- Create models with ``./manage.py syncdb`` or ``./manage.py migrate wiretap``

- Go to Django admin, add a new ``Tap``.

  - This contains a path `regex <https://developers.google.com/edu/python/regular-expressions>`_,
    which is matched against the full path including the query string.

    - For example, to capture everything within the ``/api/`` path of your site,
      use ``'^/api/'``.

    - If you just want to test Wiretap, set it to ``'/'``.

HTTP request/responses will now be saved to the `Message` admin page.

Note that Wiretap will be disabled if Django is not in debug mode unless you have ``FORCE_WIRETAP=True`` in
your project settings file.
