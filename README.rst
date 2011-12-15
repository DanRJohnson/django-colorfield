Django Colorfield
---------------------

This module fills the need of having a 'colorfield' that's usable in both
django models and forms.

Makes use of http://jscolor.com/.

How to use:

Copy contents of colorfield into base level of your django project.

*** Make sure the contents of the static directory are in the directory you host your static files in. ***

example models.py:

from fields import ColorField

class TestColor(models.Model):
    name = models.TextField()
    color = ColorField(default="ffffff")

