Django-MathJax
==============

Django-mathjax is an application to easy include MathJax in your django
projects as dependency, and easy configure directly from django settings.

Installation and configuration
------------------------------

To install django-mathjax you can use pip::

  pip install Django-MathJax

Then you have to add :code:`django_mathjax` app to your :code:`INSTALLED_APPS`
and add a :code:`MATHJAX_ENABLED=True` to your settings file.

Then you can put in any template the MathJax javascript using the template tag
mathjax_scripts. Example::

  {% load mathjax %}
  <html>
    <head>
        <title></title>
        {% mathjax_scripts %}
    </head>
    <body>
      $$1+1=2$$
    </body>
  </html>

django-mathjax use the CDN mathjax version, if you want to have your own copy
of MathJax, you have to download and put it in your static directory, and
add the :code:`MATHJAX_LOCAL_PATH` with the path of MathJax on static to your
settings. Example::

  MATHJAX_LOCAL_PATH = 'js/libs/mathjax/'

You can force the usage of mathjax https CDN version enabling the template tag
https parameter :code:`{% mathjax_scripts True %}` and you can force the usage
of mathjax http CDN version disabling the template tag https parameter
:code:`{% mathjax_scripts False %}`.

Settings parameters
-------------------

MATHJAX_ENABLED
~~~~~~~~~~~~~~~

Allow to enable/disable the mathjax app.

MATHJAX_LOCAL_PATH
~~~~~~~~~~~~~~~~~~

Use a local path of MathJax Library instead of the CDN. Example::

  MATHJAX_LOCAL_PATH = 'js/libs/mathjax/'

MATHJAX_CONFIG_FILE
~~~~~~~~~~~~~~~~~~~

Allow to configure the config file used by mathjax. Example::

  MATHJAX_CONFIG_FILE = "TeX-AMS-MML_HTMLorMML"

MATHJAX_CONFIG_DATA
~~~~~~~~~~~~~~~~~~~

Allow to configure the mathjax directly by a python dictionary. Example::

  MATHJAX_CONFIG_DATA = {
    "tex2jax": {
      "inlineMath":
        [
            ['$','$'],
            ['\\(','\\)']
        ]
    }
  }
