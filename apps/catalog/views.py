from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

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


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('categories')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('categories')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy ('categories')


def logout_user(request):
    logout(request)
    return redirect('categories')
