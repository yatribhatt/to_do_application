from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name = 'index'),
    path('del/<str:item_id>', views.remove, name= 'del'),
    path('update/<int:item_id>/', views.update_status, name='update'),
    path('edit/<int:pk>/', views.edit, name='edit'),

]

