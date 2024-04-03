from django.urls import path 

from .views import PostVIew, PostListView, CommentView, LikeView

urlpatterns = [
    
    path('post/', PostVIew.as_view()),
    path('post/<int:pk>/', PostVIew.as_view()),
    path('posts/', PostListView.as_view()),
    
    path('post/<int:pk>/comments/',CommentView.as_view()),
    path('post/<int:pk>/likes/', LikeView.as_view())
    
]
