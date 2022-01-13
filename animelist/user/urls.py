from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('users/', views.ProfileList.as_view()),
    path('users/<int:pk>/', views.ProfileDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)