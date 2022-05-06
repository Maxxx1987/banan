from django.urls import path

from apps.catalog.views import CategoryListView, SectionListView
from apps.products.views import ProductListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('<slug:slug>/', SectionListView.as_view()),
    path('<slug:cat_slug>/<slug:slug>/', ProductListView.as_view())
]

# /catalog/                                - список категорий
# /catalog/<category_slug>/                - одна категория (список подкатегорий)
# /catalog/<category_slug>/<sub_cat_slug>/ - одна подкатегория (список продуктов)
