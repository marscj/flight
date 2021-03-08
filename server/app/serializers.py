from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . import models

class AppSerializer(serializers.ModelSerializer):

    type = serializers.CharField(max_length=16)

    name = serializers.CharField(max_length=64)

    version = serializers.CharField(max_length=64)

    code = serializers.CharField(max_length=64)

    redirect = serializers.URLField(required=False, allow_blank=True)

    enable_redirect = serializers.BooleanField(default=False)

    class Meta:
        model = models.App
        fields = '__all__'

    def validate(self, validate_data):
        enable_redirect = validate_data.get('enable_redirect', None)
        redirect = validate_data.get('redirect', None)
        
        if enable_redirect and redirect is None:
            raise serializers.ValidationError({'redirect': 'This field may not to null!'})
            
        return validate_data