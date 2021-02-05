from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('', ProductLV.as_view(), name='list'),
    path('<int:pk>/', ProductDV.as_view(), name='detail'),
    path('search/', search, name='search'),
]

