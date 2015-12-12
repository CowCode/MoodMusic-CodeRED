from django import template 
import requests
import json
from django.template.defaultfilters import stringfilter
from django.template import Template, Context

register = template.Library()

@register.filter
@stringfilter
def combine(str1):
    temp = ''
    for i in range(len(str1)):
        if str1[i] == ' ':  
            temp += '+'
        else:   
            temp += str1[i]
    r = requests.get('https://api.spotify.com/v1/search?query=' + temp + '&type=track')
    json_object = json.loads(r.text)
    spot_id = json_object["tracks"]["items"][0]["id"]
    return "https://embed.spotify.com/?uri=spotify:track:" + spot_id
    