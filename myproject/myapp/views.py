from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def add(request, a, b):
    sum = a + b 
    return HttpResponse(sum)