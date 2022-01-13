from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views



urlpatterns = format_suffix_patterns ([
    path('author/', views.AuthorsViewSet.as_view({'get': 'list'})),
    path('author/<int:pk>/', views.AuthorsViewSet.as_view({'get': 'retrieve'})),
])