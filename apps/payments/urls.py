from django.urls import path

from apps.payments.views import (
    ProductOrderCreateView,
    ProductOrderListView,
    ProductOrderDeleteView,
    ProductOrderUpdateView,
)

urlpatterns = [
    path('', ProductOrderCreateView.as_view()),
    path('list/', ProductOrderListView.as_view()),
    path('<int:pk>/delete/', ProductOrderDeleteView.as_view()),
    path('<int:pk>/update/', ProductOrderUpdateView.as_view()),
]
