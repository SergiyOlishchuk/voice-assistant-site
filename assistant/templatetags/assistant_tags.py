from django import template

from assistant.utils import get_user_history

register = template.Library()

@register.simple_tag()
def user_history(request):
    return get_user_history(request)
