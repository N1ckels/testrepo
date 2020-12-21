from django.urls import path
from .views import (
    article_create_view,
    article_list_view,
    article_detail_view,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)
app_name = 'blog'
urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name="article-create"),
    path('<int:id>/', ArticleDetailView.as_view(), name="article-detail"),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name="article-update"),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name="article-delete"),
    path('', ArticleListView.as_view(), name="article-list")
]