UltraHeat 50
============

UltraHeat 50 is a lightweight `WSGI`_ web application framework.

Installing
----------

Install and update using `poetry`_:

.. code-block:: text

    $ poetry build




Linting
-------

Linting using `poetry`_:

.. code-block:: text

    $ poetry run black uh50
    $ poetry run pylint uh50
    $ poetry run pflake8 uh50
    $ poetry run black tests
    $ poetry run pylint tests
    $ poetry run pflake8 tests


testing
-------

Test using `poetry`_:

.. code-block:: text

    $ poetry run pytest
    $ poetry run coverage run -m pytest
    $ poetry run coverage report


Running
-------

Run using `poetry`_:

.. code-block:: text

    $ poetry run python uh50

Autolinter
-------

Run using `precommit`_:

.. code-block:: text

    $ poetry run pre-commit install
    $ poetry run pre-commit run --all-files


.. _poetry: https://python-poetry.org/docs/
.. _WSGI: https://wsgi.readthedocs.io/en/latest/what.html
.. _precommit: https://pre-commit.com/