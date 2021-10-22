from django import template
import json
from bson import json_util
from datetime import datetime

register = template.Library()

@register.filter(name='get')
def get(d, k):
    return d['_id']

@register.filter(name='to_json')
def to_json(value):
    # print("to",value[5])
    value = list(value)
    value[6] = str(value[6])
    value[7] = str(value[7])
    value = json.dumps(value)
    return value