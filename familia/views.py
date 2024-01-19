from django.shortcuts import render

# Create your views here.
def homePage(request):
    context = {}
    return render(request, 'template/base.html', context)

def truehomePage(request):
    context = {}
    return render(request, 'template/home.html', context)

def adminPage(request):
    context = {}
    return render(request, 'template/admin.html', context)

def memberPage(request):
    context = {}
    return render(request, 'template/members.html', context)