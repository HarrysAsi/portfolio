from django.template import Library
import datetime

register = Library()


@register.filter(expects_localtime=True)
def parse_date(value):
    return datetime.datetime.strptime(value, "%Y-%m-%d")
