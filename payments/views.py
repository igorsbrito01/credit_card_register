from rest_framework import viewsets, mixins
from .serializers import (
    CreditCardCreateListSerializer,
    CreditCardCreateSerializer,
)
from .models import CreditCard


class CreditCardListCreateView(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = CreditCard.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreditCardCreateSerializer
        return CreditCardCreateListSerializer
