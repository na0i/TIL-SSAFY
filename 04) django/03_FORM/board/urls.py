from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
    path('<int:reservation_pk>/', views.detail, name='detail'),
    path('<int:reservation_pk>/edit/', views.edit, name='edit'),
    path('<int:reservation_pk>/delete/', views.delete, name='delete')
]
