from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views



urlpatterns = format_suffix_patterns ([
    path('rating/', views.AddStarRatingViewSet.as_view({'post': 'create'})),
])