from rest_framework import viewsets
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

from .models import DonatorsData, DonationsData, DonatsSourcesData
from .serializers import DonationsSerializer
from .schemas import DonationsSchema


class TopTenDonationsViewSet(ListModelMixin, viewsets.GenericViewSet):
    renderer_classes = (JSONRenderer,)
    serializer_class = DonationsSerializer
    schema = DonationsSchema()
    # authentication_classes = IsAuthenticated

    def get_queryset(self):
        return DonationsData.objects.order_by('-summ')[:10]


class DonationsDataViewSet(ListModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    renderer_classes = (JSONRenderer,)
    serializer_class = DonationsSerializer
    schema = DonationsSchema()
    # authentication_classes = IsAuthenticated

    def get_queryset(self):
        return DonationsData.objects.all()
