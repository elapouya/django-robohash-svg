..
   Created : 2018-03-22

   @author: Eric Lapouyade

   django-robohash-svg documentation master file,

===================
django-robohash-svg
===================

Django app for creating svg robots

Installation
------------

Install with pip::

    pip install django_robohash

Then declare the app in your settings.py ::

    INSTALLED_APPS = [
    ...
        'django_robohash',
    ]



Usage
-----

If you want an inline image in your template use the robohash tag ::

    {% load robohash %}
    ...
    here is a robot:
    {% robohash "a string" %}
    a small one :
    {% robohash "a string" width=100 height=100 %}

If you want to serve robot images, edit your urls.py and use robohash view ::

    from django_robohash.views import robohash

    urlpatterns = [
        ...
        path('robohash/<string>/', robohash,
             name='robohash')
    ]

You can custom the url if you want, but keep "<string>".

The you can display image like this ::

    <img src="/robohash/{{ random }}/">

    or

    <img src="/robohash/{{ random }}/?width=120&height=120">


Default robots size is 300x300

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
