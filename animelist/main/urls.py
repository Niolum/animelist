from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns ([
    path('anime/', views.AnimeViewSet.as_view({'get': 'list'})),
    path('anime/<int:pk>/', views.AnimeViewSet.as_view({'get': 'retrieve'})),
    path('manga/', views.MangaViewSet.as_view({'get': 'list'})),
    path('manga/<int:pk>/', views.MangaViewSet.as_view({'get': 'retrieve'})),
    path('ranobe/', views.RanobeViewSet.as_view({'get': 'list'})),
    path('ranobe/<int:pk>/', views.RanobeViewSet.as_view({'get': 'retrieve'})),
])

