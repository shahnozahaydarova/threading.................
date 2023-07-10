from django.shortcuts import render

def home(request):
    return render(request,'index.html')


def category(request):
    return render(request,'category.html')

def register(request):
    return render(request,'users/register.html')