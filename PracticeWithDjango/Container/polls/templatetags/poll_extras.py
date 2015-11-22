from django import template 
import requests
import json
from django.template.defaultfilters import stringfilter
from django.template import Template, Context

register = template.Library()

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
	url = "https://embed.spotify.com/?uri=https://open.spotify.com/track/" + spot_id
    return url 

register.filter('combine', combine)