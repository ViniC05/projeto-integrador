from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from portal.models import portal


def home(request):
    posts = portal.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'portal/pages/home.html', context={
        'posts': posts,
    })


def category(request, category_id):

    posts = get_list_or_404(
        portal.objects.filter(
            Category__id=category_id,
            is_published=True
            ).order_by('-id')
    )

    return render(request, 'portal/pages/category.html', context={
        'posts': posts,
        'title': f'{posts[0].Category.name} -  Categoria',
    })


def post_portal(request, id):

    post = portal.objects.filter(
        pk=id,
        is_published=True,
    ).order_by('-id').first()

    post = get_object_or_404(portal, pk=id, is_published=True,)

    return render(request, 'portal/pages/post-view.html', context={
        'post': post,
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    posts = portal.objects.filter(
        Q(
            Q(title__icontains=search_term) | 
            Q(description__icontains=search_term)
        ),
        is_published=True
    ).order_by('-id')
    

    return render(request, 'portal/pages/search.html', {
                  'page_title': f'Pesquisa por "{search_term}" - ',
                  'search_term': search_term,
                  'posts': posts,
                  })
