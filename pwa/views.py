from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from pwa.defaults import get_app, get_pwa_config, get_service_worker

# Create your views here.


def manifest_json(request):
	return JsonResponse(get_pwa_config())


def sw_js(request):
	return HttpResponse(get_service_worker() , content_type='application/javascript')


def app_js(request):
	return HttpResponse(get_app() , content_type='application/javascript')
	

def offline(request):
	try:
		return render(request, 'pwa/offline.html')
	except:
		return render(request, 'pwa/pwa_offline.html')
