from setuptools import setup,find_packages
import os
import re


def read(*names):
    values = dict()
    for name in names:
        filename = name + '.rst'
        if os.path.isfile(filename):
            fd = open(filename)
            value = fd.read()
            fd.close()
        else:
            value = ''
        values[name] = value
    return values


long_description = """
%(README)s

News
====
%(CHANGES)s
""" % read('README', 'CHANGES')


def get_version(pkg):
    path = os.path.join(os.path.dirname(__file__), pkg, '__init__.py')
    with open(path) as fh:
        m = re.search(r'^__version__\s*=\s*[\'"]([^\'"]+)[\'"]', fh.read(), re.M)
    if m:
        return m.group(1)
    raise RuntimeError("Unable to find __version__ string in %s." % path)


setup(name='django-robohash-svg',
      version=get_version('django_robohash'),
      description='Library for creating svg robots',
      long_description=long_description,
      classifiers=[
          "Intended Audience :: Developers",
          "Development Status :: 4 - Beta",
          "Framework :: Django",
          "Framework :: Django :: 1.10",
          "Framework :: Django :: 1.11",
          "Framework :: Django :: 1.9",
          "Framework :: Django :: 2.0",
          "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
      ],
      keywords='robots, robohash, svg, hash',
      url='https://github.com/elapouya/django-robohash-svg',
      author='Eric Lapouyade',
      author_email='elapouya@gmail.com',
      license='LGPL 2.1',
      packages=find_packages(exclude=['tests.*','tests','docs.*','docs']),
      package_data={'': ['*.png',],},
      install_requires=['django>=2','Sphinx'],
      zip_safe=False)
