from django.urls import path
from .views import upload_csv, aggregate

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),
    path('aggregate/', aggregate, name='aggregate'),
]