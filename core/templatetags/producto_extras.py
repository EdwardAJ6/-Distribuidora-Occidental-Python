from django import template

register = template.Library()

@register.filter()
def formato_precio(value):
    return '${0:2f}'.format(value)