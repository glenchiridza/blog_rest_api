from django.urls import path
from .views import PostCreateView, PostUpdateView, PostDeleteView, GetSinglePostView

urlpatterns = [
    path('post/<int:pk>', GetSinglePostView.as_view(), name="get-single-post"),
    path('post/', PostCreateView.as_view(), name="post"),
    path('update/<int:pk>', PostUpdateView.as_view(), name="update-post"),
    path('delete/<int:pk>', PostDeleteView.as_view(), name="delete-post")
]
