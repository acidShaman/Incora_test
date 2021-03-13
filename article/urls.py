from django.urls import path

from article.views import ArticleView

urlpatterns = [
    path('', ArticleView.as_view())
]
