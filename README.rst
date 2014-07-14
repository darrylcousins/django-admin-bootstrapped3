django-admin-bootstrapped
=========================

A Django admin theme using Twitter Bootstrap. It doesn't need any kind
of modification on your side, just add it to the installed apps.

Credits
-------

This package is a fork of
`django-admin-bootstrapped <https://github.com/django-admin-bootstrapped/django-admin-bootstrapped>`_. All
credit goes to `Riccardo Forina <https://riccardo.forina.me/>`_ and the other
contributors. A good deal of the this readme comes from the original repostory.

Requirements
------------

-  Django ``>=1.7.x``.
-  Python ``3``
-  `django-bootstrap3`_

Installation
------------

Simple install into a virtualenv::

    $ pip install git+https://github.com/darrylcousins/django-admin-bootstrapped3.git

Add ``'django_admin_bootstrapped'`` into the ``INSTALLED_APPS`` list **before**
``'django.contrib.admin'``

Build and Run Test Project
--------------------------

Get the test project from github::

    $ git clone https://github.com/darrylcousins/django-project.git
    $ cd django-project
    $ python setup.py develop

The test project uses django-bootstrap3_ and bootstrapped3_ admin.  these extra
packages can be installed with::

    $ pip install -r requirements.txt

The test project has some tests::

    $ python manage.py test project

The tables and sample data can be installed with::

    $ python manage.py migrate
    $ python manage.py loaddata project/fixtures/project.json

And can be run with::

    $ python manage.py runserver 9000

There are no urls beyond the admin screens and api json views. It attempts to
demonstrate the autocomplete widgets.

Included
--------

Autocomplete Widgets
~~~~~~~~~~~~~~~~~~~~

See `django-autocomplete`_.

Translate/change an application name with a template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a file named ``admin_app_name.html`` into the application's
template folder. Eg: ``project/templates/admin_app_name.html``. You can also change the
default Django Administration title, just add a ``admin_title.html``
file into your ``project/templates/admin/`` folder.

Add custom html to the list view or change form of any model with a template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can inject custom html on top of any change form creating a template
named ``admin_model_MODELNAME_change_form.html`` into the application's
template folder. Likewise the title of the model list view can be changed by adding a template called
``admin_model_MODELNAME_title.html`` into the application's template folder.

Inline sortable
~~~~~~~~~~~~~~~

You can add drag&drop sorting capability to any inline with a couple of
changes to your code.

First, add a ``position`` field in your model (and sort your model
accordingly), for example:

::

    class TestSortable(models.Model):
        that = models.ForeignKey(TestMe)
        position = models.PositiveSmallIntegerField("Position")
        test_char = models.CharField(max_length=5)

        class Meta:
            ordering = ('position', )

Then in your admin.py create a class to handle the inline using the
``django_admin_bootstrapped.admin.models.SortableInline`` mixin, like
this:

::

    from django_admin_bootstrapped.admin.models import SortableInline
    from models import TestSortable

    class TestSortable(admin.StackedInline, SortableInline):
        model = TestSortable
        extra = 0

This feature was brought to you by `Kyle
Bock <https://github.com/kwbock>`_. Thank you Kyle!

.. _bootstrapped3: <https://github.com/darrylcousins/django-admin-bootstrapped3>
.. _django-autocomplete: <https://github.com/darrylcousins/django-autocomplete>
.. _django-bootstrap3: <https://github.com/dyve/django-bootstrap3>
