from rest_framework import serializers

import models

class AppSerializer(serializers.ModelSerializer):

    type = serializers.CharField(max_length=16)

    name = serializers.CharField(max_length=64)

    version = serializers.CharField(max_length=64)

    code = serializers.CharField(max_length=64)

    file = serializers.FileField()

    class Meta:
        mode = models.App
        fields = '__all__'