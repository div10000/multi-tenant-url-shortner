from django.urls import path
from .views import tenant_info

urlpatterns = [
    path('info/', tenant_info),
]
