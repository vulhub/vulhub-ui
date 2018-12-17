from django.urls import path, include
from . import views

app_name = 'environment'
urlpatterns = [
    path('environments/', views.EnvironmentList.as_view(), name='environment-list')
]
