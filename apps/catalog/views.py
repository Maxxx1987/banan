from django.views.generic import TemplateView, ListView

from apps.catalog.models import Category, Section
from apps.products.models import Brand


class IndexView(TemplateView):
    template_name = 'index.html'


class CategoryListView(ListView):
    queryset = Category.objects.filter(is_active=True)
    template_name = 'category_list.html'


class SectionListView(ListView):
    model = Section
    template_name = 'section_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['category'] = Category.objects.get(slug = self.kwargs['slug'])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True, category__slug = self.kwargs['slug'])
