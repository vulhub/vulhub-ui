from django.urls import path, include
from . import views

app_name = 'environment'
urlpatterns = [
    path('environments/', views.EnvironmentList.as_view(), name='environment-list'),
    path('environment/<path:path>/', views.EnvironmentDetail.as_view(), name='environment-detail'),
]
