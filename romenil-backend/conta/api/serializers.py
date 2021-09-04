from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'], 
            last_name = validated_data['last_name'], 
            email = validated_data['email'], 
        )

        user.set_password(validated_data['password']) 
        user.save()

        return user
