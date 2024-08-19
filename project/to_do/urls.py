from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.adding,name='add'),
    path('delete/<int:id>',views.deleting,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    
]
