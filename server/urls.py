
from django.urls import re_path
from . import views
from exercise import viewz

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    re_path('workout', viewz.getworkout),
    re_path('update-profile', views.update_profile),
]
