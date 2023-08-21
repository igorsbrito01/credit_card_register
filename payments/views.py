from rest_framework import viewsets, mixins
from .serializers import (
    CreditCardListSerializer,
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
        return CreditCardListSerializer


class CreditCardRetrieveView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CreditCardListSerializer
    queryset = CreditCard.objects.all()
