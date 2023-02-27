from django import template

register = template.Library()

@register.filter()
def formato_cantidad_producto(cantidad=1):
    return '{} {}'.format(cantidad, 'productos' if cantidad > 1 else 'producto')

@register.filter()
def agregar_formato_cantidad(cantidad=1):
    return '{} {}'.format(
        formato_cantidad_producto(cantidad),
        'agregados' if cantidad > 1 else 'agregado'
    )