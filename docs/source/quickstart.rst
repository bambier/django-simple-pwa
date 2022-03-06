.. _quickstart:

شروع سریع
====================


نصب
-------
ابتدا DSP (django-simple-pwa) را با دستور زیر نصب کنید


.. code-block:: bash
	:linenos:

	pip install django-simple-pwa


حال DSP را به اپ‌های نصب شده اضافه کنید.

.. code-block:: python
	:linenos:
	:emphasize-lines: 5

	#<my_project/settings.py>

	INSTALLED_APPS = [
		#...
		'pwa',
		#...
	]

تنظیمات
--------
حال urlهای DSP را به ``urls.py`` که در کنار ``setting.py`` واقع است به شکل زیر اضافه کنید.


.. code-block:: python
	:linenos:
	:emphasize-lines: 6

	#<my_project/urls.py>

	from django.urls import path, include
	urlpatterns = [
		#...
		path('', include('pwa.urls')), 
		#...
	]


مهم است که محل فایل‌های استاتیک را در تنظمیات خود معرفی کنید.

.. code-block:: python
	:linenos:

	#<my_project/settings.py>

	from os.path import join

	STATIC_URL = '/static/'
	STATIC_ROOT = str(join(BASE_DIR, 'static'))
	STATICFILES_DIRS = ( str(join(BASE_DIR, 'static_files')), )

همچنین فرمان ``./manage.py collectstatic`` را اجرا کنید.



اجرا در لوکال هاست
---------------------

در صورتی که پروژه‌ را در لوکال هاست خود اجرا می‌کنید، مطمئن شوید که فایل‌های استاتیک به درستی لود شده‌اند.


.. code-block:: python
	:linenos:
	:emphasize-lines: 5

	#<my_project/urls.py>
	from django.conf.urls.static import static
	from django.conf import settings

	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




لود کردن فایل‌های ضروری
--------------------------

حال در فایل html اصلی خود که عموما به نام ``index.html`` شناخته می‌شود، متا دیتا‌های اپ را لود کنید.

.. code-block:: html
	:linenos:
	:emphasize-lines: 3,7
	
	{% load pwa %} 
	<head>
		{% pwa_meta_data %}
	</head>
	<body>

		{% pwa_meta_script %}
	</body>



.. note::
	همچین می‌توانید این تنظیمات را در تمام صفحات اعمال کنید تا از طریق همه آن‌ها pwa در دسترس باشد.



اگر همه مراحل را به درستی انجام داده باشید میتوانید اکنون سایت خود را بر روی دستگاه خود به صورت pwa نصب کنید.


