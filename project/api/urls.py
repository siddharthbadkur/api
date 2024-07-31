
from django.urls import path
from .views import *

urlpatterns = [

    # path('stu_info/',stu_info,name='stu_info')
    # path('stu_detail/<int:pk>',stu_detail,name='stu_detail')
    path('list/',list,name='list')

    
]