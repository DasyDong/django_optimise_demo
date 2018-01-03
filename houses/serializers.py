from rest_framework import serializers

from houses.models import House, Country
from utils.hash import Hasher


class HouseSerializer(serializers.ModelSerializer):
    """Serialize a `houses.House` instance."""

    id = serializers.IntegerField(source="hash", read_only=True)
    country = serializers.IntegerField(source="country.hash", read_only=True)

    class Meta:
        model = House
        fields = (
            'id',
            'address',
            'country',
            'sq_meters',
            'price'
        )
