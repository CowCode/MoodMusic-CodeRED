from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render_to_response("../templates/index.html")
def results(request):
	return render_to_response("../templates/results.html")