from django.shortcuts import render

from .models import Drug
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import  RequestContext
from django.contrib.auth.models import User

# Create your views here.
def addAPlan(request):
    pass

def dropAPlan(request):
    pass
