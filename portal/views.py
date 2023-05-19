from django.shortcuts import render

from portal.models import portal
from utils.portal.factory import make_recipe


def home(request):
    posts = portal.objects.all().order_by('-id')
    return render(request, 'portal/pages/home.html', context={
        'posts': posts,
    })


def contato(request, id):
    return render(request, 'portal/pages/post-view.html', context={
        'post': make_recipe(),
        'is_detail_page': True,
    })

