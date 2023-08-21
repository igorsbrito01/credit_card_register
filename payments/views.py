from rest_framework import viewsets, mixins, authentication, permissions

from .models import CreditCard
from .serializers import (
    CreditCardListSerializer,
    CreditCardCreateSerializer,
)


class CreditCardListCreateView(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = CreditCard.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreditCardCreateSerializer
        return CreditCardListSerializer


class CreditCardRetrieveView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CreditCardListSerializer
    queryset = CreditCard.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
