from rest_framework import serializers

from .models import *

class BookingSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=64)

    remark = serializers.CharField(required=False, max_length=1024)
    class Meta:
        model = Booking
        fields = '__all__'

class ItinerarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Itinerary
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fiels = '__all__'

class UpLoadSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpLoad
        fields = '__all__'