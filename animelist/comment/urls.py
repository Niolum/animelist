from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views



urlpatterns = format_suffix_patterns ([
    path('comment/', views.CommentCreateViewSet.as_view({'post': 'create'})),
])