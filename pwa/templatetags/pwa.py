from django import template

from pwa.defaults import get_pwa_config

register = template.Library()


@register.inclusion_tag('pwa/metadata.html')
def pwa_meta_data():
	PWA_CONFIG = get_pwa_config()
	try:
		ICONS = PWA_CONFIG.get('icons')
		THEME_COLOR = PWA_CONFIG.get('theme_color')
	except:
		ICONS = None
		THEME_COLOR = None

	return {'ICONS':ICONS, 'THEME_COLOR':THEME_COLOR}


@register.inclusion_tag('pwa/meta_script.html')
def pwa_meta_script():
	return {}
