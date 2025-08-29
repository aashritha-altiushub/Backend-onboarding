from django.urls import path
from .views import  SignInView, SignOutView, UserCreateView, UserDeleteView, UserDetailView, UserListView, UserUpdateView, CountryListCreateView, CountryRetrieveUpdateDestroyView,StateListCreateView, StateRetrieveUpdateDestroyView,CityListCreateView, CityRetrieveUpdateDestroyView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<uuid:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<uuid:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('auth/signin/', SignInView.as_view(), name='sign-in'),
    path('auth/signout/', SignOutView.as_view(), name='sign-out'),
    path('countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('countries/<uuid:pk>/', CountryRetrieveUpdateDestroyView.as_view(), name='country-detail'),
    path('states/', StateListCreateView.as_view(), name='state-list-create'),
    path('states/<uuid:pk>/', StateRetrieveUpdateDestroyView.as_view(), name='state-detail'),
    path('cities/', CityListCreateView.as_view(), name='city-list-create'),
    path('cities/<uuid:pk>/', CityRetrieveUpdateDestroyView.as_view(), name='city-detail'),
]
