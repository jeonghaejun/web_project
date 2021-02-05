from django.shortcuts import render
from product.models import *
from django.views.generic import ListView, DetailView, FormView
from django.db.models import Q

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
    paginate_by = 6 # 페이지네이션, 페이지 당 문서 건 수

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

        maker_list = Maker_list.objects.all()
        context['maker_list'] = maker_list

        return context

# DetailView
class ProductDV(DetailView):
    model = Product
    context_object_name = 'product'

# search
def search(request):
    context = {}

    product_list = Product.objects.all().order_by('-id')
    maker_list = Maker_list.objects.all()

    q = request.POST.get('q', '') # 검색에서의 입력 값
    f = request.POST.getlist('f') # 체크박스 (제조사)

    if q: # 검색값이 있다면
        product_list = product_list.filter(Q(name__icontains=q) | Q(content__icontains=q))
    if f: #f(체크박스 필터)에서 값이 넘어왔다면
        query = Q()
        for i in f:
            print(i)
            query = query | Q(maker__icontains=i)
        product_list = product_list.filter(query)
    
    print(product_list)
    context['product_list'] = product_list
    context['maker_list'] = maker_list
    context['q'] = q
    context['f'] = f

    return render(request, 'product/product_search.html', context)

    