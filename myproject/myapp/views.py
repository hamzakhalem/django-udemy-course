from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def imagepage(request):
    return render(request, 'imagepage.html')

def myform(request):
    return render(request, 'myform.html')

def submitform(request):
    if(request.method == "POST"):
        mytext = request.POST['mytext']
        mytextarea = request.POST['mytextarea']
        print(mytext)
        print(mytextarea)
    return render(request, 'myform.html')

def add(request, a, b):
    sum = a + b 
    return HttpResponse(sum)