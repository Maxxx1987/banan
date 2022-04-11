from django.views.generic import ListView, DetailView

from apps.catalog.models import Section
from apps.products.models import Product, Brand


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'slug' in self.kwargs:
            return queryset.filter(section__slug=self.kwargs['slug'])
        if 'brand' in self.request.GET:
            return queryset.filter(brand=self.request.GET['brand'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if 'slug' in self.kwargs:
            context['section'] = Section.objects.get(slug=self.kwargs['slug'])
        if 'brand' in self.request.GET:
            context['brand'] = Brand.objects.get(id=self.request.GET['brand'])
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class BrandListView(ListView):
    model = Brand
    template_name = 'category_list.html'
