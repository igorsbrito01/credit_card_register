from django.urls import path
from .views import CreditCardListCreateView

urlpatterns = [
    path(
        "credit_card",
        CreditCardListCreateView.as_view({"get": "list", "post": "create"}),
    )
]
