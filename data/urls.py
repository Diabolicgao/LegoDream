from django.urls import path
from . import views

urlpatterns = [
    path('', views.New_Post),
    path('new/', views.New_All, name = 'newAll'),
    path('<int:id>/', views.Detail, name = 'detail')
]