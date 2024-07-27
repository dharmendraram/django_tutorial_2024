from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myapp_home(request):
    response ="""
    <h1>Hellow world </h1>
    <h2>Iam learning </h2>
    """
    return HttpResponse(response)

def root_page(request):
    return render(request,template_name="myapp/root_page.html")

def portfolio(request):
    return render(request,template_name="myapp/index.html")