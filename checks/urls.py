from django.urls import path,re_path
from . import views
from django.urls import re_path as url

app_name = 'checks'

urlpatterns = [
    path('', views.check_list),
    path('create/', views.create_check),
    path('<int:check_pk>', views.check_detail),
]