from django.urls import path
from product.views import *


app_name = 'product'

urlpatterns = [
    
    path('<int:pk>/', ProductDV.as_view(), name='detail'),
    
]