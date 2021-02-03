from django.shortcuts import render
from product.models import *
from django.views.generic import ListView, DetailView

# Create your views here.

# def product(request):
#     products = Product.objects.all()
#     context = {'products' : products}
#     return render(request, 'product/product.html', context)

# ListView
class ProductLV(ListView):
    model = Product
    template_name = 'product/product.html' # 템플릿 파일명 변경 / 디폴트는 post_list
    context_object_name = 'products' # 컨텍스트 객체 이름 변경 / 디폴트는 object_list
    paginate_by = 3 # 페이지네이션, 페이지 당 문서 건 수

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page-1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range

        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context

# DetailView
class ProductDV(DetailView):
    model = Product
    context_object_name = 'product'

def search(request):
    products = Product.objects.all().order_by('-id')

    q = request.POST.get('q', "") 

    if q:
        products = products.filter(name__icontains=q)
        return render(request, 'search.html', {'products' : products, 'q' : q})
    
    else:
        return render(request, 'search.html')