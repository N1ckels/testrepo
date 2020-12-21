from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Article
from .forms import ArticleForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.

class ArticleListView(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    # queryset = Article.objects.filter(id__gt=1)
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    template_name = 'article_create.html'
    queryset = Article.objects.all()
    form_class = ArticleForm
    #success_url = '/blog/'  #where to go after create

class ArticleUpdateView(UpdateView):
    template_name = 'article_update.html'
    queryset = Article.objects.all()
    form_class = ArticleForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    def get_success_url(self):
        return reverse('blog:article-list')

def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "article_create.html", context)

def article_detail_view(request, article_id):
    obj = get_object_or_404(Article, id=article_id)
    context = {
        "object": obj
    }
    return render(request, 'article_detail.html', context)

def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "article_list.html", context)