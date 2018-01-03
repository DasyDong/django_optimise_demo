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


class HousePlainSerializer(object):

    """

    Serializes a House queryset consisting of dicts with

    the following keys: 'id', 'address', 'country',

    'sq_meters', 'price'.

    """


    @staticmethod

    def serialize_data(queryset):

        """

        Return a list of hashed objects from the given queryset.

        """

        return [

            {

                'id': entry.hash,

                'address': entry.address,

                'country': entry.country.hash,

                'sq_meters': entry.sq_meters,

                'price': entry.price

            } for entry in queryset

        ]