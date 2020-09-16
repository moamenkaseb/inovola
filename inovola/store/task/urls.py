from django.urls import path
from . import views

urlpatterns = [
    path('', views.machine_page, name='machine_page'),
    path('pods/' , views.pods_page , name = "pods_page")
]
