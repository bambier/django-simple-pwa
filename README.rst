=====
PWA
=====


PWA
###

PWA is a simple Django app to develope and deploy a Progressive Web Application.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "pwa" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'pwa',
    ]

2. Include the pwa URLconf in your project urls.py like this::

    path('', include('pwa.urls')),

3. Run ``python manage.py collectstatic`` to get the PWA static files.

4. Load pwa & its meta files in index HTML file like as::


    {% load pwa %}
    {% pwa_meta_data %}
    {% pwa_meta_script %}

5. Start the development server on HTTPS or localhost to see installable app.




github: https://github.com/nimaes80/django-simple-pwa


documents: https://django-simple-pwa.readthedocs.io/fa/latest/



pypi: https://pypi.org/project/django-simple-pwa/