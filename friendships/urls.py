from django.urls import path                                             

from .views import (UserListView, RequestView,
                    RequestListView, AcceptView,
                    FriendsListView)



urlpatterns = [
    
    path('user-list/', UserListView.as_view()),
    path('request/', RequestView.as_view()),
    path('request-lists/', RequestListView.as_view()),
    path('accept/', AcceptView.as_view()),
    path('friends/', FriendsListView.as_view())
]