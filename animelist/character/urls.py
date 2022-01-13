from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views



urlpatterns = format_suffix_patterns ([
    path('character/', views.CharacterViewSet.as_view({'get': 'list'})),
    path('character/<int:pk>/', views.CharacterViewSet.as_view({'get': 'retrieve'})),
])