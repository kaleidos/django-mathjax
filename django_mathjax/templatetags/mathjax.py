import json

from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def mathjax_scripts(https=None):
    if not getattr(settings, 'MATHJAX_ENABLED', False):
        return ''

    mathjax_local_path = getattr(settings, 'MATHJAX_LOCAL_PATH', None)
    if mathjax_local_path:
        mathjax_js_url = static('%s/MathJax.js' % mathjax_local_path)
    elif https:
        mathjax_js_url = 'https://c328740.ssl.cf1.rackcdn.com/mathjax/latest/MathJax.js'
    else:
        mathjax_js_url = 'http://cdn.mathjax.org/mathjax/latest/MathJax.js'

    mathjax_config_file = getattr(settings, 'MATHJAX_CONFIG_FILE', None)
    url = mathjax_js_url
    if mathjax_config_file:
        url += "?config=%s" % mathjax_config_file
    load_script_tag = '<script type="text/javascript" src="%s"></script>' % url

    mathjax_config_data = getattr(settings, 'MATHJAX_CONFIG_DATA', None)
    config_script_tag = ''
    if mathjax_config_data:
        config_script_tag = '<script type="text/javascript">'
        config_script_tag += 'MathJax.Hub.Config('
        config_script_tag += json.dumps(mathjax_config_data)
        config_script_tag += ');'
        config_script_tag += '</script>'

    return load_script_tag + config_script_tag
