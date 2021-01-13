import json
from django.dispatch import receiver
from django.core import serializers
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models
from user.serializers import UserListSerializer

UserModel = get_user_model()

class CurrentUserDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.id

    def __repr__(self):
        return '%s()' % self.__class__.__name__

class ContentTypeField(serializers.Field):

    def to_representation(self, obj):
        return obj.model

    def to_internal_value(self, data):
        return ContentType.objects.get(model=data)

class UpLoadSerializer(serializers.ModelSerializer):

    content_type = ContentTypeField()

    author_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))

    name = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    class Meta:
        model = models.UpLoad
        fields = '__all__'

    def get_name(self, obj):
        return str(obj.file).split("/")[-1]

    def get_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.file.url)

class MessageSerializer(serializers.ModelSerializer):

    content_type = ContentTypeField()

    class Meta:
        model = models.Message
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    content_type = ContentTypeField()
    
    class Meta:
        model = models.Message
        fields = '__all__'

class ItinerarySerializer(serializers.ModelSerializer):
    serial_no = serializers.CharField(max_length=32)
    remark = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=1024)
    author_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))
    booking_id = serializers.IntegerField(required=True)
    author = serializers.StringRelatedField(read_only=True)
    ticket = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Itinerary
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
        model = models.Itinerary.history.model
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    serial_no = serializers.CharField(max_length=32)
    remark = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=1024)
    author_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))
    author = serializers.StringRelatedField(read_only=True)
    
    itinerary = ItinerarySerializer(read_only=True, many=False)
    itinerary_id = serializers.IntegerField(required=False, allow_null=True)
    

    messages = MessageSerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)
    uploads = UpLoadSerializer(read_only=True, many=True) 
   
    class Meta:
        model = models.Ticket
        fields = '__all__'

class TicketHistorySerializer(serializers.ModelSerializer):

    history_user = serializers.StringRelatedField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model =  models.Ticket.history.model
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=64)
    remark = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=1024)
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.IntegerField(default=serializers.CreateOnlyDefault(CurrentUserDefault()))

    messages = MessageSerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)
    uploads = UpLoadSerializer(read_only=True, many=True)
    itineraries = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Booking
        fields = '__all__'

    def get_itineraries(self, obj):
        query = None
        if self.context['request'].user.has_perm('ticket.view_itinerary'):
            query = obj.itineraries.all()
        else:
            query = obj.itineraries.filter(user_id=self.context['request'].user.id)

        serializer = ItinerarySerializer(instance=query, many=True)

        return serializer.data

class BookingHistorySerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    history_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = models.Booking.history.model
        fields = '__all__'

