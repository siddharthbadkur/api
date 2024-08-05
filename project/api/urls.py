
from django.urls import path
from api.views import Customer_list,Customer_details

urlpatterns = [
    # path('movie_list/',movie_list,name='movie_list'),
    # path('movie_details/<int:pk>',movie_details,name='movie_details')
    # path('list/',list,name='list')
    path('customer_list/',Customer_list.as_view()),
    path('customer_details/<int:pk>/',Customer_details.as_view())
]
