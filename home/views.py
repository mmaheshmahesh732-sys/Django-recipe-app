from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
 
def home(request):
    #return HttpResponse('<h1>Hey I am a Django Server.</h1>')
    peoples=[
        {"name":"mahesh","age":22},
        {"name":"anil","age":17},
        {"name":"rajesh","age":23},
        {"name":"raghu","age":21},
        {"name":"ajay","age":20}
        
    ]
    
    return render(request,"home/index.html" ,context={"page":"django" ,"peoples":peoples})

def about(request):
    context={"page":"About"}
    return render(request,"home/about.html")

def contact(request):
    contex={"page":"Contact"}
    return render(request,"home/contact.html")

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> this is a Success page</h1") 