from django import template
from core.models import *
register = template.Library()


@register.filter(name="isSuperUser")
def Brflen(value):
    return '企业超级用户' if value==1 else '企业普通用户'



@register.filter(name="Brflen")
def Brflen(value, arg):
    return value[:arg] + '...' if len(value) > 10 else value[:arg]
