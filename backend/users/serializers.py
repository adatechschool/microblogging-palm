from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'email', 'password']
        

        # fields = ['id', 'user_name', 'birthdate', 'email', 'password', 'created_at', 'updated_at']