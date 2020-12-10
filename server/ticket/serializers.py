from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *

UserModel = get_user_model()

class CurrentUserDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.id

    def __repr__(self):
        return '%s()' % self.__class__.__name__

class BookingSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=64)

    remark = serializers.CharField(allow_blank=True, allow_null=True, max_length=1024)

    author = serializers.StringRelatedField(read_only=True)

    author_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))
    
    class Meta:
        model = Booking
        fields = '__all__'

class BookingHistorySerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    history_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Booking.history.model
        fields = '__all__'

class ItinerarySerializer(serializers.ModelSerializer):
    serial_no = serializers.CharField(max_length=32)
    author_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))
    booking_id = serializers.IntegerField(write_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Itinerary
        fields = '__all__'

    def validate(self, validate_data):
        email = validate_data.get('email', None)

        if email:
            try:
                user = UserModel.objects.get(email=email)
                validate_data['user_id'] = user.id
            except UserModel.DoesNotExist:
                raise serializers.ValidationError({'email': 'No user for such email'})

        return validate_data

    def create(self, validated_data):
        if not self.context['request'].user.has_perm('ticket.lock_itinerary'):
            validated_data['is_lock'] = True
        
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if not self.context['request'].user.has_perm('ticket.lock_itinerary'):
            validated_data.pop('is_lock', None)

        return super().update(instance, validated_data)

class ItineraryHistorySerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField(read_only=True)
    history_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Itinerary.history.model
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    serial_no = serializers.CharField(max_length=32)
    
    author_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))
    author = serializers.StringRelatedField(read_only=True)

    user_id = serializers.IntegerField(write_only=True)
    user = serializers.StringRelatedField(read_only=True)

    itineraries_id = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Itinerary.objects.all())

    class Meta:
        model = Ticket
        fields = '__all__'

class TicketHistorySerializer(serializers.ModelSerializer):

    history_user = serializers.StringRelatedField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model =  Ticket.history.model
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fiels = '__all__'

class UpLoadSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpLoad
        fields = '__all__'