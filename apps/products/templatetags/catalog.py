from django import template
from apps.products.models import Brand

register = template.Library()


@register.inclusion_tag('brands.html', takes_context=True)
def brands(context):
    return {
        'brands': Brand.objects.order_by('title')[:10]
    }
