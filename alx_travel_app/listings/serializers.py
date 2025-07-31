from rest_framework import serializers
from .models import Listing, Host, Booking

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['id', 'name', 'email']

class ListingSerializer(serializers.ModelSerializer):
    host = HostSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'price_per_night',
            'location',
            'available_from',
            'available_to',
            'host'
        ]

class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id',
            'user',
            'listing',
            'check_in',
            'check_out',
