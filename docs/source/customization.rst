.. _customization:

شخصی سازی
==================

ساختار پیش فرض
---------------------

DSP از یک ساختار پیشفرض برای تولید ``manifest.json`` استفاده می‌کند.


.. code-block:: python
	:linenos:

	#<pwa/defaults.py>

	DEFAULT_CONFIG = {
		"name": "Progressive Web Application",
		"short_name": "PWA",
		"theme_color": "#7820f5",
		"background_color": "#7820f5",
		"display": "standalone",
		"orientation": "portrait",
		"scope": "/",
		"start_url": "/",
		"icons": [
			{
				"src": "/static/pwa/icons/72x72.png",
				"type": "image/png",
				"sizes": "72x72"
			},
			{
				"src": "/static/pwa/icons/96x96.png",
				"type": "image/png",
				"sizes": "96x96"
			},
			{
				"src": "/static/pwa/icons/128x128.png",
				"type": "image/png",
				"sizes": "128x128"
			},
			{
				"src": "/static/pwa/icons/144x144.png",
				"type": "image/png",
				"sizes": "144x144"
			},
			{
				"src": "/static/pwa/icons/152x152.png",
				"type": "image/png",
				"sizes": "152x152"
			},
			{
				"src": "/static/pwa/icons/192x192.png",
				"type": "image/png",
				"sizes": "192x192"
			},
			{
				"src": "/static/pwa/icons/384x384.png",
				"type": "image/png",
				"sizes": "384x384"
			},
			{
				"src": "/static/pwa/icons/512x512.png",
				"type": "image/png",
				"sizes": "512x512"
			}
			],
		"lang": "en",
		"dir": "ltr",
		"description": "Progressive Web app powerd by Django",
		"version": "1.",
		"manifest_version": "1.0",
		"permissions": [
			"notifications",
			"webRequest"
		],
		"author": "PWA-django"
	}



تغییر پیش فرض
-----------------------
برای شخصی‌سازی فایل  ``manifest.json`` ``app.js`` ``sw.js`` کافیست متغیر ``PWA_CONFIG`` ``PWA_SW`` ``PWA_APP`` را در فایل ``settings.py`` تعریف کنید.


.. code-block:: python
	:linenos:

	#<my_project/settings.py>

	PWA_CONFIG = {
	# ...
	"name": "Progressive Web Application"
	# ...
	}
	PWA_APP = """// js code here"""
	PWA_SW = """// js code here"""


.. warning::
	توجه داشته باشید که هیچ یک از دو آیکون شما دارای سایز برابر نباشند.

	برای مثال ساختار زیر باعث ایجاد خطا در برنامه میشود.
	

	.. code-block:: python
		:linenos:
		:emphasize-lines: 4,9


		{
			"src": "/static/pwa/icons/144x144.png",
			"type": "image/png",
			"sizes": "144x144"
		},
		{
			"src": "/static/pwa/icons/144x144.ico",
			"type": "image/x-icon",
			"sizes": "144x144"
		},
	
	
.. note::
	این بدین معنی است که لزوما تغییر فرمت موجب جلوگیری از خطا نمی‌شود.

.. note::
	همچنین ما توصیه نمی‌کنیم که ``PWA_APP`` و ``PWA_SW`` را دوباره تعریف کنید مگر آنکه بدانید واقعا چه می‌کنید.


شما میتوانید آیکون‌های خود را در سایزهای مختلف با فرمت‌های دلخواه خود به صورت فوق تعریف کنید اما ما توصیه میکنیم از فرمت .ico استفاده کنید.


تغییر ``manifest.json``
##########################

برای این کار ``PWA_CONFIG`` را به ``settings.py`` اضافه کنید.

.. code-block:: python
	:linenos:

	#<my_project/settings.py>

	PWA_CONFIG = {
		"name": "My Costum Name",
		"short_name": "MCN",
		"theme_color": "#fff",
		"background_color": "#f0f0f0",
		"display": "standalone",
		"orientation": "portrait",
		"scope": "/",
		"start_url": "/",
		"icons": [
			{
				"src": "/static/pwa/icons/72x72.png",
				"type": "image/png",
				"sizes": "72x72"
			},
			{
				"src": "/static/pwa/icons/96x96.png",
				"type": "image/png",
				"sizes": "96x96"
			},
			{
				"src": "/static/pwa/icons/128x128.png",
				"type": "image/png",
				"sizes": "128x128"
			},
			{
				"src": "/static/pwa/icons/144x144.png",
				"type": "image/png",
				"sizes": "144x144"
			},
			{
				"src": "/static/pwa/icons/152x152.png",
				"type": "image/png",
				"sizes": "152x152"
			},
			{
				"src": "/static/pwa/icons/192x192.png",
				"type": "image/png",
				"sizes": "192x192"
			},
			{
				"src": "/static/pwa/icons/384x384.png",
				"type": "image/png",
				"sizes": "384x384"
			},
			{
				"src": "/static/pwa/icons/512x512.png",
				"type": "image/png",
				"sizes": "512x512"
			}
			],
		"lang": "en",
		"dir": "ltr",
		"description": "Progressive Web app powerd by Django",
		"version": "1.",
		"manifest_version": "1.0",
		"permissions": [
			"notifications",
			"webRequest"
		],
		"author": "PWA-django"
	}



مقادیر قابل قبول ``manifest.json``
______________________________________
ما در اینجا برخی از مواردی که یک PWA میتواند در فایل ``manifest.json`` خود داشته باشد را به صورت پیشفرض برای اپ خود تعریف کرده‌ایم 
و در ادامه به تعریف مقادیری که میتوانید برای آن‌ها لحاظ کنید می‌پردازیم.


.. code-block:: javascript
	:linenos:

	{
	"name": 'The name of application',
	"short_name": "Short name; Can be same with name",
	"theme_color": "The hex color for app theme",
	"background_color": "The hex color for app background color",
	"display": "fullscreen [OR] standalone [OR] minimal-ui [OR] browser",
	"orientation": "any [OR] natural [OR] landscape [OR] landscape-primary [OR] landscape-secondary [OR] portrait [OR] portrait-primary [OR] portrait-secondary",
	"scope": "/app/ [OR] https://example.com/ [OR] https://example.com/subdirectory/",
	"start_url": "/ [OR] https://example.com [OR] ../startpoint.html",
	"icons": "the list of dictionery that contains **src** and **sizes** and **type**"
	"lang": "langueage code like fa [OR] en [OR] tu [OR] fn [OR] ge [OR] ...",
	"dir": "rtl [OR] ltr [OR] auto",
	"description": "Description pf your app",
	"version": "app version",
	"manifest_version": "manifest.json file vertion if change on updating app",
	"permissions": `list here <https://developer.chrome.com/docs/extensions/mv2/declare_permissions/>`_
	"author": "author name or title of app"

	}




.. note::
	برای اطلاعات بیشتر می‌توانید به برخی مستندات آن که در لیست زیر فراهم کردیم بپردازید:

	* `developer.mozilla.org <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json>`_
	* `developer.chrome.com <https://developer.chrome.com/docs/extensions/mv3/manifest/>`_
	* `web.dev <https://web.dev/add-manifest/>`_



تغییر ``ServiceWorker.js``
#############################

برای این کار ``PWA_SW`` را در ``settings.py`` به یکی از دو روش زیر تعریف کنید.


.. code-block:: python
	:linenos:

	PWA_SW = """// js code here """


.. code-block:: python
	:linenos:

	SW = open('/path/to/ServiceWorker.js', "r")
	PWA_SW = SW.read()
	SW.close()


.. note::
	برای اطلاعات بیشتر نسبت به نحوه‌ی کارکرد ``ServiceWorker.js`` می‌توانید از منابع زیر استفاده کنید.

	* `developer.mozilla.org <https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API>`_
	* `developers.google.com <https://developers.google.com/web/fundamentals/primers/service-workers>`_
	* `docs.microsoft.com <https://docs.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/service-workers>`_





تغییر ``app.js``
########################

برای این کار کافیست متغییر ``PWA_APP`` را در فایل ``settings.py`` تعریف کنید.


.. code-block:: python
	:linenos:

	PWA_SW = """// js code here """


.. code-block:: python
	:linenos:

	APP = open('/path/to/app.js', "r")
	PWA_SW = APP.read()
	APP.close()




.. note::
	همچنان توصیه نمی‌کنیم که ``PWA_APP`` و ``PWA_SW`` را دوباره تعریف کنید مگر آن که بدانید واقعا چه می‌کنید.



تغییر محتوای صفحه‌ی آفلاین
################################
ما از ساختاری مشابه ساختار جنگو برای تغییر صفحه‌ی آفلاین استفاده می‌کنیم.
به طوری که برای تغییر آن می‌بایست ابتدا در مسیر ``<templates-dir>/pwa/`` یک فایل با نام ``offline.html`` ایجاد کنید و
سپس آن را در مسیر ``pwa/pwa_offline.html`` اکستند کنید.

.. code-block:: html
	:linenos:

	<!-- <templates-dir/pwa/offline.html> -->

	{% extend 'pwa/pwa_offline.html' %}

	{% block title %} title {% endblock title %}
	{% block main %} something {% endblock main %}


.. note::
	ما به طور پیش‌فرض از `بوت‌استرپ <https://getbootstrap.com/>`_ در قسمت آفلاین سایت استفاده می‌کنیم با این حال
	میتوانید به صورت زیر فایل‌های css و js خود را در آن بارگذاری کنید.

	.. code-block:: html
		:linenos:

		{% block extrastyles %} <!-- your css here --> {% endblock extrastyles %}

		{% block extrascripts %} <!-- your js here --> {% endblock extrascripts %}

	.. warning::
		توجه داشته باشید با اعمال قطعه کد بالا دیگر بوت استرپ در صفحه اعمال نخواهد شد.

	درضمن هرگونه تغییر در فایل آفلاین باید با تغییر کش در ``ServiceWorker.js`` همراه باشد.
	بنابراین در صورتی که فایل آفلاین را تغییر دادید نیاز است که ``PWA_SW``  را نیز تعریف کنید هرچند
	ممکن است بدون این کار هم برنامه کار بکند ولی بهتر است که ``ServiceWorker.js`` باز نویسی شود.