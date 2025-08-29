from django.urls import path
from .views import UserCreateView, UserDeleteView, UserDetailView, UserListView, UserUpdateView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<uuid:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<uuid:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
