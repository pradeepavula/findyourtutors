import re
from app.models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import UserType
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'

    def validate_first_name(self,value):
        if value:
            if len(value)>5 :
                pass
            else:
                msg ="{0} should be more than 5 charecters".format(value)
                raise serializers.ValidationError(msg)
        return value
    def validate_last_name(self,value):
        if value:
            if len(value)>5 :
                pass
            else:
                msg ="{0} should be more than 5 charecters".format(value)
                raise serializers.ValidationError(msg)
        return value
    def validate_email(self,value):
        if value:
            obj = User.objects.filter(email=value)
            if obj:
                msg ="{0} aldreay exists!!!!!!".format(value)
                raise serializers.ValidationError(msg)
            else:
                pass
        return value
    def validate_password(self,value):
        if value:
            if not re.findall('\d', value):
                raise serializers.ValidationError(
                "The password must contain at least 1 digit, 0-9.")
            if not re.findall('[A-Z]', value):
                raise serializers.ValidationError(
                "The password must contain at least 1 uppercase letter, A-Z.")
            if not re.findall('[a-z]', value):
                raise serializers.ValidationError(
                "The password must contain at least 1 lowercase letter, a-z.")
        return value


