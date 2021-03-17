from django import template

register = template.Library()

@register.filter
def divide(value, arg):
    try:
        return int(value) / int(arg), True
    except (ValueError, ZeroDivisionError):
        return None
