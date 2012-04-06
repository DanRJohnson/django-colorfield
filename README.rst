Django Colorfield
=================

A Django app that exports a field with a color picker.

Makes use of http://jscolor.com/.

How to use
***********

1. Add the project somewhere in your python path, e.g. via pip::

    pip install -e git+git://github.com/mbi/django-colorfield.git#egg=django-colorfield

2. Add ``colorfield`` to your ``INSTALLED_APPS``

3. Run ``manage.py collectstatic`` (in production) to collect static files from the app

4. Add a ``ColorField`` in your models::


    from colorfield.fields import ColorField

    class TestColor(models.Model):
        name = models.TextField()
        color = ColorField(default="ffffff")

