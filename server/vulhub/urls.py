from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='auth')),
    path('api/', include('environment.urls', namespace='environment'))
]
