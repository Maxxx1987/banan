from django.urls import path

from apps.products.views import BrandListView, ProductDetailView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('brands/', BrandListView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),


]
