from django.shortcuts import render
from product.models import *
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.

# ListView


class ProductLV(ListView):
    model = Product
    template_name = 'product/product.html'  # 템플릿 파일명 변경 / 디폴트는 post_list
    context_object_name = 'products'  # 컨텍스트 객체 이름 변경 / 디폴트는 object_list
    paginate_by = 6  # 페이지네이션, 페이지 당 문서 건 수

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 페이지네이션
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page-1) /
                          page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range

        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        # 검색 필터 목록
        maker_list = Maker_list.objects.all()
        context['maker_list'] = maker_list
        context['number_of_maker_list'] = maker_list.count()

        cpu_list = Cpu_list.objects.all()
        context['cpu_list'] = cpu_list
        context['number_of_cpu_list'] = cpu_list.count()

        ram_list = Ram_list.objects.all()
        context['ram_list'] = ram_list
        context['number_of_ram_list'] = ram_list.count()

        return context

# DetailView


class ProductDV(DetailView):
    model = Product
    context_object_name = 'product'

# 검색 (클래스형)


class SearchLView(ListView):
    template_name = 'product/product_search.html'
    model = Product
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # context value들을 담는 컨테이너

        # 페이지네이션
        paginator = context['paginator']
        page_number_range = 5  # 페이지그룹에 속한 페이지 수
        current_page = int(self.request.GET.get('page', 1))

        # 시작/끝 index 조회
        start_index = int((current_page-1)/page_number_range)*page_number_range
        end_index = start_index + page_number_range

        # 현재 페이지가 속한 페이지 그룹의 범위
        current_page_group_range = paginator.page_range[start_index: end_index]

        start_page = paginator.page(current_page_group_range[0])
        end_page = paginator.page(current_page_group_range[-1])

        has_previous_page = start_page.has_previous()
        has_next_page = end_page.has_next()

        context['current_page_group_range'] = current_page_group_range
        if has_previous_page:  # 이전페이지 그룹이 있다면
            context['has_previous_page'] = has_previous_page
            context['previous_page'] = start_page.previous_page_number

        if has_next_page:  # 다음 페이지 그룹이 있다면
            context['has_next_page'] = has_next_page
            context['next_page'] = end_page.next_page_number

        # 검색 필터 목록
        maker_list = Maker_list.objects.all()
        context['maker_list'] = maker_list
        context['number_of_maker_list'] = maker_list.count()

        cpu_list = Cpu_list.objects.all()
        context['cpu_list'] = cpu_list
        context['number_of_cpu_list'] = cpu_list.count()

        ram_list = Ram_list.objects.all()
        context['ram_list'] = ram_list
        context['number_of_ram_list'] = ram_list.count()

        get_full_path = self.request.get_full_path()

        if get_full_path.split('&')[-1].startswith('page'):
            get_full_path = ('&').join(get_full_path.split('&')[:-1])

        if get_full_path.split('?')[0] == get_full_path.split('?')[1]:
            get_full_path = get_full_path[17:]

        print('주소창')
        print(get_full_path)
        print()
        context['get_full_path'] = get_full_path

        return context

    def get_queryset(self):

        product_list = Product.objects.all()
        q = self.request.GET.get('q', '')  # 검색에서 입력한 값이 넘어옴

        # Maker 체크박스 입력한 데이터 값들이 넘어옴(getlist -> 여러개 받을 수 있음)
        f_maker = self.request.GET.getlist('f_maker')
        # CPU 체크박스 입력한 데이터 값들이 넘어옴(getlist -> 여러개 받을 수 있음)
        f_cpu = self.request.GET.getlist('f_cpu')
        # RAM 체크박스 입력한 데이터 값들이 넘어옴(getlist -> 여러개 받을 수 있음)
        f_ram = self.request.GET.getlist('f_ram')

        if q:  # b(검색창)에서 값이 넘어왔다면
            product_list = product_list.filter(
                Q(name__icontains=q) | Q(content__icontains=q))

        if f_maker:  # f(체크박스 필터)에서 값이 넘어왔다면
            query = Q()
            for i in f_maker:
                query = (query | Q(maker__icontains=i))
            product_list = product_list.filter(query)

        if f_cpu:  # f(체크박스 필터)에서 값이 넘어왔다면
            query = Q()
            for i in f_cpu:
                query = (query | Q(cpu__icontains=i))
            product_list = product_list.filter(query)

        if f_ram:  # f(체크박스 필터)에서 값이 넘어왔다면
            query = Q()
            for i in f_ram:
                query = (query | Q(ram__icontains=i))
            product_list = product_list.filter(query)

        print()
        print()
        get_full_path = self.request.get_full_path

        return product_list


# --- Tag View
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_product_list.html'
    model = Product

    def get_queryset(self):
        return Product.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

# 함수형 search
# def search(request):
#     context = {}

#     product_list = Product.objects.all().order_by('-id')
#     maker_list = Maker_list.objects.all()

#     q = request.GET.get('q', '') # 검색에서의 입력 값
#     f = request.GET.getlist('f') # 체크박스 (제조사)

#     if q: # 검색값이 있다면
#         product_list = product_list.filter(Q(name__icontains=q) | Q(content__icontains=q))
#     if f: #f(체크박스 필터)에서 값이 넘어왔다면
#         query = Q()
#         for i in f:
#             print(i)
#             query = query | Q(maker__icontains=i)
#         product_list = product_list.filter(query)

#     context['maker_list'] = maker_list
#     context['q'] = q
#     context['f'] = f

#     # 페이지네이션
#     paginate_by = 6
#     page_number_range = 5
#     context['is_paginated'] = True

#     paginator = Paginator(product_list, paginate_by)
#     current_page = int(request.GET.get('page', 1))
#     context['current_page'] = current_page

#     start_index = int((current_page-1)/page_number_range)*page_number_range
#     end_index = start_index + page_number_range

#     current_page_group_range = paginator.page_range[start_index : end_index]

#     start_page = paginator.page(current_page_group_range[0])
#     end_page = paginator.page(current_page_group_range[-1])

#     has_previous_page = start_page.has_previous()
#     has_next_page = end_page.has_next()

#     context['current_page_group_range'] = current_page_group_range
#     if has_previous_page: #이전페이지 그룹이 있다면
#         context['has_previous_page'] = has_previous_page
#         context['previous_page'] = start_page.previous_page_number

#     if has_next_page: #다음 페이지 그룹이 있다면
#         context['has_next_page'] = has_next_page
#         context['next_page'] = end_page.next_page_number

#     e = paginate_by * current_page
#     s = e - paginate_by

#     product_list = product_list[s:e]
#     context['product_list'] = product_list

#     return render(request, 'product/product_search.html', context)

# def search(request):
#     context = {}

#     product_list = Product.objects.all().order_by('-id')
#     maker_list = Maker_list.objects.all()

#     q = request.GET.get('q', '') # 검색에서의 입력 값
#     f = request.GET.getlist('f') # 체크박스 (제조사)

#     if q: # 검색값이 있다면
#         product_list = product_list.filter(Q(name__icontains=q) | Q(content__icontains=q))
#     if f: #f(체크박스 필터)에서 값이 넘어왔다면
#         query = Q()
#         for i in f:
#             print(i)
#             query = query | Q(maker__icontains=i)
#         product_list = product_list.filter(query)

#     context['product_list'] = product_list
#     context['maker_list'] = maker_list
#     context['q'] = q
#     context['f'] = f

#     # 페이지네이션
#     paginate_by = 6
#     paginator = Paginator(product_list, paginate_by)
#     page_numbers_range = 5
#     max_index = len(paginator.page_range)

#     page = request.GET.get('page')
#     current_page = int(page) if page else 1

#     start_index = int((current_page-1) / page_numbers_range) * page_numbers_range
#     end_index = start_index + page_numbers_range

#     if end_index >= max_index:
#         end_index = max_index

#     page_range = paginator.page_range[start_index:end_index]
#     context['page_range'] = page_range

#     return render(request, 'product/product_search.html', context)
