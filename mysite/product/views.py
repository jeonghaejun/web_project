
from product.models import *
from django.views.generic import DetailView

# Create your views here.

# def product(request):
#     products = Product.objects.all()
#     context = {'products' : products}
#     return render(request, 'product/product.html', context)


# DetailView
class ProductDV(DetailView):
    model = Product
    context_object_name = 'product'

