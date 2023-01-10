from django.shortcuts import render, loader
from django.http import HttpResponse 

def members(request):
  template = loader.get_template('OurBlog.html')
  return HttpResponse(template.render())