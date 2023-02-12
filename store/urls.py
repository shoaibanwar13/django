from django.urls import path
from .import views

urlpatterns = [
    path('',views.store,name='store-page'),
    path('maine/',views.maine,name='store-page'),
    path('ecom/',views.ecom,name='store-page'),
]