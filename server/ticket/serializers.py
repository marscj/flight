from rest_framework import serializers

from .models import *

class ApplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Apply
        fiels = '__all__'

class ItinerarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Itinerary
        fiels = '__all__'

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fiels = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fiels = '__all__'

class UpLoadSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpLoad
        fiels = '__all__'