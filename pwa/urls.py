from django.urls import path
from pwa.views import manifest_json, sw_js, app_js, offline

app_name = 'pwa'

urlpatterns = [
	path('sw.js' , sw_js, name="sw.js"),
	path('manifest.json' , manifest_json, name="manifest.json"),
	path('app.js', app_js, name="app.js"),
	
	path('offline' , offline, name="offline"),
	
	
]

