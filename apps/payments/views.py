from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from apps.payments.forms import ProductOrderForm, ProductOrderUpdateForm
from apps.payments.models import ProductOrder, Order

from django.http import HttpResponseRedirect


class ProductOrderCreateView(CreateView):
    model = ProductOrder
    form_class = ProductOrderForm

    def get_success_url(self):
        return self.object.product.get_absolute_url()

    def form_valid(self, form):
        params = {
            'status': 'active',
        }
        if self.request.user.is_authenticated:
            params['user'] = self.request.user
        else:
            if not self.request.session.session_key:
                self.request.session.create()
            params['session_key'] = self.request.session.session_key

        user_active_order, created = Order.objects.get_or_create(**params)
        form.instance.order = user_active_order
        return super().form_valid(form)


class ProductOrderListView(ListView):
    model = ProductOrder
    context_object_name = 'productorder_list'
    template_name = 'productorder_list.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.order = Order.objects.filter(user=self.request.user, status='active').first()
        else:
            self.order = Order.objects.filter(session_key=self.request.session.session_key, status='active').first()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.order:
            return queryset.filter(order=self.order)
        return queryset.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.order:
            context['identifier'] = self.order.identifier

        order_sum = 0
        for item in context['productorder_list']:
            item.form = ProductOrderUpdateForm(instance=item)
            order_sum += item.count * item.product.price
        context['order_sum'] = order_sum

        return context


class ProductOrderUpdateView(UpdateView):
    model = ProductOrder
    form_class = ProductOrderUpdateForm
    success_url = '/order/list/'


class ProductOrderDeleteView(DeleteView):
    model = ProductOrder
    success_url = '/order/list/'
