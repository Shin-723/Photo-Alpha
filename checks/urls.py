# from django.urls import path,re_path
from . import views
from django.urls import re_path,path 

app_name = 'checks'

urlpatterns = [
    re_path('', views.check_list),
    re_path('create/', views.create_check),
    re_path('<int:check_pk>', views.check_detail),
]