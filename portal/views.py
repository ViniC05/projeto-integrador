from django.shortcuts import render


def home(request):
    return render(request, 'portal/pages/home.html')

