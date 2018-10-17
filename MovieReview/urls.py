from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    path('signup/',views.signup, name = 'signup'),
    path('search/', views.search, name = 'search'),
]