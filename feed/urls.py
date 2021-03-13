from django.urls import path

from feed.views import FeedView, DeleteFeedView, CreateFeedView

urlpatterns = [
    path('', FeedView.as_view()),
    path('new/', CreateFeedView.as_view()),
    path('<int:id>/delete/', DeleteFeedView.as_view()),
]
