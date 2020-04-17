===================
django-robohash-svg
===================

.. image:: https://raw.githubusercontent.com/elapouya/django-robohash-svg/master/django_robohash.png
    :width: 100%
    :align: center

Django app for creating svg robots

The idea: from any string (username, first name and last name, etc...), obtain a unique svg robot to display. This is useful for creating avatars or for testing purposes.

Installation
------------

Install with pip::

    pip install django-robohash-svg

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

Then you can display image like this ::

    <img src="/robohash/{{ a_string }}/">

    or

    <img src="/robohash/{{ a_string }}/?width=120&height=120">


Default robots size is 300x300

You can generate the svg code by running this function::

    from django_robohash.robotmaker import make_robot_svg
    ...
    svg_code = make_robot_svg("my string", width=300, height=300)

