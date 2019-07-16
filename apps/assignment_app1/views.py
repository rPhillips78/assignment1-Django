from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    print("************************")
    print("This is the index function")
    return HttpResponse("Placholder to later display a list of all blogs")

def new(request):
    print('******************************')
    print('This is the new function')
    return HttpResponse('Placeholder to later display a new form to create a new blog')

def create(request):
    print('****************************')
    print('This is the create function')
    return redirect('/')

def show(request, number):
    print('*******************************')
    print('This is the show function')
    return HttpResponse(f'Placeholder to display blog number {number}')

def edit(request, number):
    print('*****************************')
    print('This is the edit function')
    return HttpResponse(f'Placeholder to edit blog {number}')

def destroy(request, number):
    print('*****************************')
    print('This is the destroy function')
    return redirect('/')