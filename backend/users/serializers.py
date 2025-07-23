from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_photo', 'password']
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
        return super().update(instance, validated_data)
        

        # fields = ['id', 'user_name', 'birthdate', 'email', 'password', 'created_at', 'updated_at']