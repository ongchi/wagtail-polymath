from django.conf import settings
from django.contrib.staticfiles import finders
from django.templatetags.static import static

from wagtail_polymath.blocks import MATHJAX_VERSION

MATHJAX_CONFIG = "TeX-MML-AM_CHTML"

DEFAULT_CONF = {
    "katex_js": "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js",
    "katex_css": "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css",
    "mathjax_js": f"https://cdnjs.cloudflare.com/ajax/libs/mathjax/{MATHJAX_VERSION}/MathJax.js?config={MATHJAX_CONFIG}",
}


def get_conf(key):
    try:
        conf = settings.WAGTAIL_POLYMATH
        value = conf[key]
    except:
        url = DEFAULT_CONF[key]
    else:
        url = value

    if finders.find(url):
        return static(url)
    else:
        return url
