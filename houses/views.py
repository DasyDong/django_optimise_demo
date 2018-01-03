from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from houses.models import House, Country
from houses.serializers import HouseSerializer
from utils.hash import Hasher


class HouseListAPIView(ListAPIView):
    model = House
    serializer_class = HouseSerializer
    country = None

    def get_queryset(self):

        if self.country:
            country = get_object_or_404(Country, pk=self.country)
            queryset = self.model.objects.filter(country=country)
        else:
            queryset = self.model.objects.all()[:self.count]
        return queryset

    def list(self, request, *args, **kwargs):
        # Validation code to check for `country` param should be here
        self.country = self.request.GET.get("country")
        self.count = self.request.GET.get("count") or 100

        if self.country:
            self.country = Hasher.to_object_pk(self.country)
        queryset = self.get_queryset()

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)