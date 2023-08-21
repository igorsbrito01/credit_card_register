from django.urls import path
from .views import CreditCardListCreateView, CreditCardRetrieveView

urlpatterns = [
    path(
        "credit-card",
        CreditCardListCreateView.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "credit-card/<int:pk>",
        CreditCardRetrieveView.as_view({"get": "retrieve"}),
    ),
]
