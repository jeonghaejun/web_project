from django.views.generic import TemplateView, CreateView

# Homepage
class HomeView(TemplateView):
    template_name = 'index.html'