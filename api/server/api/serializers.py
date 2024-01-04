from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

# class SessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Session
#         fields = "__all__"