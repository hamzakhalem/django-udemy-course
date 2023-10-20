from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import newForm
# Create your views here.
def home(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def imagepage(request):
    return render(request, 'imagepage.html')

def myform(request):
    return render(request, 'myform.html')

def error(request, exception):
    print("inside")
    return render(request, '404page.html')

def newform(request):
    if(request.method == "POST"):
        form = newForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            print(title)
            print(subject)
            form = newForm()
            context = {'form':form, 'success': True, 'successmsg': "sucess" }
            return render(request, 'newform.html', context=context) 
        else:
            form = newForm()
            context = {'form':form, 'success': False, 'successmsg': "error" }
            return render(request, 'newform.html', context={'form':form})
    elif(request.method == "GET"):
        form = newForm()
        return render(request, 'newform.html', context={'form':form})
    

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