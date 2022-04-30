from django.views.generic import ListView, DetailView

from apps.catalog.models import Section
from apps.payments.forms import ProductOrderForm
from apps.payments.models import ProductOrder
from apps.products.models import Product, Brand, Event, ProductStore


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        params = {
            'product': self.object,
        }
        if self.request.user.is_authenticated:
            params['order__user'] = self.request.user
        else:
            params['order__session_key'] = self.request.session.session_key

        p_order = ProductOrder.objects.filter(**params).first()
        if not p_order:
            context['order_form'] = ProductOrderForm(initial={'product': self.object.id})

        # shop = Store.objects.get(title="Магазин")
        # context['productstore'] = ProductStore.objects.filter(product=self.object, store=shop)

        context['productstore_shop'] = ProductStore.objects.filter(product=self.object, store__title="Магазин").first()
        context['productstore_sklad'] = ProductStore.objects.filter(product=self.object, store__title="Склад").first()

        return context


class BrandListView(ListView):
    model = Brand
    template_name = 'category_list.html'


class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    paginate_by = 5


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'


