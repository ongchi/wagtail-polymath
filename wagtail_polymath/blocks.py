from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.forms import Widget, CharField
from wagtail.blocks import FieldBlock
#from wagtail.core.telepath import register
#from wagtail.core.widget_adapters import WidgetAdapter
from django.forms.widgets import HiddenInput

MATHJAX_VERSION = '2.7.9'


class MathJaxWidget(HiddenInput):
    class Media:
        js = (
            f'https://cdnjs.cloudflare.com/ajax/libs/mathjax/{MATHJAX_VERSION}/MathJax.js?config=TeX-MML-AM_HTMLorMML',
            'wagtail_polymath/js/streamfield.js'
        )

    template_name = "wagtail_polymath/streamfield.html"

    def get_context(self, name, value, attrs):
        context = {'widget': {
            'name': name,
            'is_hidden': self.is_hidden,
            'required': self.is_required,
            'value': value,
            'attrs': self.build_attrs(attrs),
            'template_name': self.template_name,
        }}
        return context

    def render(self, name, value, attrs=None, renderer=None):
        # id gets set, but I dont know where.
        # We need it removed so the JS will work correctly
        # attrs.pop('id')
        context = self.get_context(name, value, attrs)
        return mark_safe(render_to_string(self.template_name, context))


class MathBlock(FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = CharField(required=required, help_text=help_text, widget=MathJaxWidget())
        super(MathBlock, self).__init__(**kwargs)

    def value_from_form(self, value):
        return value


#class MathJaxWidgetAdapter(WidgetAdapter):
#    js_constructor = 'wagtail_polymath.blocks.MathJaxWidget'
#
#    def js_args(self, widget):
#        return [
#            widget.options,
#        ]


#register(MathJaxWidgetAdapter(), MathJaxWidget)
