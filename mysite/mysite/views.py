from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from product.models import *

# Homepage


class HomeView(ListView):
    model = Product
    template_name = 'product/product.html'  # 템플릿 파일명 변경 / 디폴트는 post_list
    context_object_name = 'products'  # 컨텍스트 객체 이름 변경 / 디폴트는 object_list
    paginate_by = 9  # 페이지네이션, 페이지 당 문서 건 수

    def get_queryset(self):

        products = Product.objects.all()

        sort = self.request.GET.get('sort', '')
        if sort == 'high_price':
            products = products.order_by('-price')
        elif sort == 'low_price':
            products = products.order_by('price')
        else:
            products = products.order_by('id')

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 페이지네이션
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(self.request.GET.get('page', 1))

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
        # context['number_of_maker_list'] = maker_list.count()

        cpu_list = Cpu_list.objects.all()
        context['cpu_list'] = cpu_list
        # context['number_of_cpu_list'] = cpu_list.count()

        ram_list = Ram_list.objects.all()
        context['ram_list'] = ram_list
        # context['number_of_ram_list'] = ram_list.count()

        gpu_list = Gpu_list.objects.all()
        context['gpu_list'] = gpu_list
        # context['number_of_gpu_list'] = gpu_list.count()

        ssd_list = Ssd_list.objects.all()
        context['ssd_list'] = ssd_list
        # context['number_of_ssd_list'] = ssd_list.count()

        os_list = Os_list.objects.all()
        context['os_list'] = os_list
        # context['number_of_os_list'] = os_list.count()

        display_list = Display_list.objects.all()
        context['display_list'] = display_list
        # context['number_of_Display_list'] = display_list.count()

        weight_list = Weight_list.objects.all()
        context['weight_list'] = weight_list

        # 노트북 총 몇 건
        number_of_product = Product.objects.all().count()
        context['number_of_product'] = number_of_product

        sort = self.request.GET.get('sort', '')
        context['sort'] = sort

        return context
    # --- User Creation


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            self.handle_no_permission

        return super().get(request, *args, **kwargs)
