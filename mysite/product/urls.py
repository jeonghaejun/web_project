from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('', ProductLV.as_view(), name='list'),
    path('<int:pk>/', ProductDV.as_view(), name='detail'),
    path('search/', SearchLView.as_view(), name='search'),
    # Example: /product/tag/
    path('tag/', TagCloudTV.as_view(), name='tag_cloud'),
    # Example: /product/tag/tagname/
    path('tag/<str:tag>/', TaggedObjectLV.as_view(), name='tagged_object_list'),
]
