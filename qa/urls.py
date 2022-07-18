from django.urls import path
from .views import *

app_name = "qa"
urlpatterns = [
    path('', board_list, name='board_list'),
    path('board_list/', board_list, name='board_list'),
    path('board_detail/<int:id>/', board_detail, name='board_detail'),
]
