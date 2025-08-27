from django.urls import path
from . import views

urlpatterns = [
    path('', views.SikayetListView.as_view(), name='sikayet_list'),
    path('yeni/', views.SikayetCreateView.as_view(), name='sikayet_create'),
    path('<int:pk>/', views.sikayet_detay, name='sikayet_detail'),
]
