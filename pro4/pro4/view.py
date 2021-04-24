from django.http import HttpResponse

def sample(request):
    return HttpResponse("Hello World")

def sample1(request):
    return HttpResponse("Python Django project4 ")

def index(request):
    return HttpResponse("index function")

def index1(request):
    return HttpResponse("Django project creating view file")

def sample2(request):
    return HttpResponse("<h1> This is the Header Tag and sample 2 function</h1>")