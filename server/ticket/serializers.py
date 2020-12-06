from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *

class CurrentUserDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.id

    def __repr__(self):
        return '%s()' % self.__class__.__name__

class BookingSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=64)

    remark = serializers.CharField(allow_blank=True, allow_null=True, max_length=1024)

    author_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))
    
    class Meta:
        model = Booking
        fields = '__all__'

class BookingHistorySerializer(serializers.ModelSerializer):

    history_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Booking.history.model
        fields = '__all__'

class ItinerarySerializer(serializers.ModelSerializer):
    serial_no = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=Itinerary.objects.all())])
    author_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))
    booking_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Itinerary
        fields = '__all__'

    def update(self, instance, validated_data):
        if not instance.has_perm('itinerary.lock_itinerary'):
            validated_data.pop('is_lock', None)

        return super().update(instance, validated_data)

class TicketSerializer(serializers.ModelSerializer):

    author_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))

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