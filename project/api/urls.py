
from django.urls import path
from api.views import *

urlpatterns = [

    # path('userlist/',userList,name='userlist'),
    path('userdetails/<int:pk>',userDetails,name='userdetails')
    # path('list/',list,name='list')

    
]