from django.shortcuts import render_to_response
from owl.models import *
from django.template import RequestContext
from django.http import HttpResponse
from django.utils.html import escape
from django.utils import simplejson
from django.shortcuts import render

def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))
	
def about(request):
	return render_to_response('about.html',context_instance=RequestContext(request))
	
def terms(request):
	return render_to_response('terms.html',context_instance=RequestContext(request))

def privacy(request):
	return render_to_response('privacy.html',context_instance=RequestContext(request))


def auto(request):
	print request
	return render_to_response('auto.html',context_instance=RequestContext(request))