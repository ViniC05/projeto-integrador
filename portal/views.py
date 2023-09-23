from django.db.models import Q
from django.http import Http404
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from django.urls import reverse

from authors.forms import LoginForm
from portal.models import portal

from .forms import CommentForm
from .models import Comment, portal


def teste(request):
    return render(request, 'portal/pages/teste/mapa.html')

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

def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_create'),
    })



"""def add_comment_to_post(request, post_id):
    post = get_object_or_404(portal, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(reverse('portal:post', args=[str(post_id)]))
    else:
        form = CommentForm()

    return render(request, 'portal/partials/add_comment_to_post.html', {'form': form})"""


def add_comment_to_post(request, post_id):
    if request.method == 'POST':
        content = request.POST['content']
        # Obtem o usuário autenticado
        author = request.user 
        
        
        # Salvar o comentário no banco de dados
        Comment.objects.create(post_id=post_id, content=content, author=author)
        # Redirecionar de volta para a página do post
        return redirect(reverse('portal:post', args=[str(post_id)]))




