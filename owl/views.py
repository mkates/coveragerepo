from django.shortcuts import render_to_response
from owl.models import *
from django.template import RequestContext
from django.http import HttpResponse
from django.utils.html import escape
from django.utils import simplejson
from django.shortcuts import render

def index(request):
	#return HttpResponse("Hello, world. You're at the poll index.")
	return render_to_response('index.html',context_instance=RequestContext(request))
	