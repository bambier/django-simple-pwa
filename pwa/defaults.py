from django.conf import settings
from django.utils.translation import gettext_lazy as _


def get_pwa_config():
    DEFAULT_CONFIG = {
        "name": _("Progressive Web Application"),
        "short_name": _("PWA"),
        "theme_color": "#7820f5",
        "background_color": "#7820f5",
        "display": "standalone",
        "orientation": "portrait",
        "scope": "/",
        "start_url": "/",
        "icons": [
            {
                "src": "/static/pwa/images/icons/72x72.png",
                "type": "image/png",
                            "sizes": "72x72"
            },
            {
                "src": "/static/pwa/images/icons/96x96.png",
                "type": "image/png",
                "sizes": "96x96"
            },
            {
                "src": "/static/pwa/images/icons/128x128.png",
                "type": "image/png",
                "sizes": "128x128"
            },
            {
                "src": "/static/pwa/images/icons/144x144.png",
                "type": "image/png",
                "sizes": "144x144"
            },
            {
                "src": "/static/pwa/images/icons/152x152.png",
                "type": "image/png",
                "sizes": "152x152"
            },
            {
                "src": "/static/pwa/images/icons/192x192.png",
                "type": "image/png",
                "sizes": "192x192"
            },
            {
                "src": "/static/pwa/images/icons/384x384.png",
                "type": "image/png",
                "sizes": "384x384"
            },
            {
                "src": "/static/pwa/images/icons/512x512.png",
                "type": "image/png",
                "sizes": "512x512"
            }
        ],
        "lang": "en",
        "dir": "ltr",
        "description": _("Progressive Web app powered by Django"),
        "version": "1.",
        "manifest_version": "1.0",
        "permissions": [
            "notifications",
            "webRequest"
        ],
        "author": _("PWA-django"),
    }
    try:
        if settings.PWA_CONFIG and settings.PWA_CONFIG != {}:
            return settings.PWA_CONFIG
    except:
        return DEFAULT_CONFIG


def get_service_worker():
    SERVICE_WORKER = """
var CACHE_NAME = 'pwa-cache-v1';
var urlsToCache = [
	'/',
	'/sw.js',
	'/app.js',
	'/manifest.json',
	'/offline',
	'/static/pwa/images/dino.gif',

	'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css',
	'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js',

	];
const self = this;

// Install SW
self.addEventListener('install', (event) =>{
	event.waitUntil(
		caches.open(CACHE_NAME)
		.then((cache) => {
			console.log('%s');
			return cache.addAll(urlsToCache);
		})
	)
});

// Listen For requests
self.addEventListener('fetch', (event) =>{
	event.respondWith(
		caches.match(event.request)
		.then(() => {
			return fetch(event.request)
			.catch(() => caches.match('/offline'))
		})
	)
});

// Activate
self.addEventListener('activate', (event) =>{
	const cacheWhitelist = [];
	cacheWhitelist.push(CACHE_NAME);
	event.waitUntil(
		caches.keys().then((cacheNames) => Promise.all(
			cacheNames.map((cacheName) => {
				if (!cacheWhitelist.includes(cacheName)) {
					return caches.delete(cacheName);
					}
				})
			))
		)
});
	""" % (
        _("Cache Opend."),

    )
    try:
        if settings.PWA_SW and settings.PWA_SW != {}:
            return settings.PWA_SW
    except:
        return SERVICE_WORKER


def get_app():
    APP = """
if ("serviceWorker" in navigator) {
	window.addEventListener("load", () => {
		navigator.serviceWorker
		.register("/sw.js")
		.then(res => console.log("%s"))
		.catch(err => console.log("%s", err));
	});
} else {
	console.log(`%s`);
};
	""" % (
        _("Service worker registered!"),
        _("Your browser supports serviceWorker, but the service worker is not registered."),
        _("Your browser doesn't support serviceWorker, so you can't install the PWA."),
    )
    try:
        if settings.PWA_APP and settings.PWA_APP != {}:
            return settings.PWA_APP
    except:
        return APP




PERMISSION_LIST = """
activeTab
background
bookmarks
browserSettings
clipboardRead
clipboardWrite
contentSettings
contextMenus
cookies
debugger
declarativeNetRequestFeedback
downloads
downloads.open
find
geolocation
history
idle
management
nativeMessaging
notifications
pageCapture
privacy
scripting
tabHide
tabs
topSites
webNavigation
webRequest
webRequestBlocking
webRequestFilterResponse
webRequestFilterResponse.serviceWorkerScript"""