from django.urls import path
from . import  views
app_name='blog'
urlpatterns = [
    path('',views.show,name='index'),
    path('post/<int:pk>/',views.detail,name='detail')
]