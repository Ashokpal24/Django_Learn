from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required


@login_required
def create_article(request):
    if request.method == 'POST':
        print(request.POST)
        form = ArticleForm(request.POST, user=request.user)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            return redirect('article-list')
    else:
        form = ArticleForm(user=request.user)

    return render(request, 'article/create.html', {'form': form})


@login_required
def list_article(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'article/list.html', {"articles": articles})


@login_required
def list_all_article(request):
    articles = Article.objects.all()
    return render(request, 'main/home.html', {"articles": articles})


@login_required
def detail_article(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'article/detail.html', {"article": article})

# add instance parameter of you want to update same object from model
@login_required
def update_article(request, id):
    article = get_object_or_404(Article, pk=id)
    print(article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article, user=request.user)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            return redirect('article-detail', id=article.id)
    else:
        form = ArticleForm(instance=article, user=request.user)

    return render(request, 'article/update.html', {'form': form})


@login_required
def delete_article(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'POST':
        article.delete()
        return redirect('article-list')
    return render(request, 'article/delete.html', {"article": article})
