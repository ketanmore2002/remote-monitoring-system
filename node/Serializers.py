
from rest_framework import routers, serializers, viewsets
from .models import *
from django.contrib.auth.models import User

class WaterTakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = water_tank
        # fields = ('id', 'machine', 'location', 'sub_location', 'humidity','tempreture','tempreture_low','tempreture_high','battery','user_name','delete_status','uuid','_uuid',"humidity_low","humidity_high","CO2_high","CO2_low","CO2",'updated_at','email')
        fields = '__all__' 



class WaterTankTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = water_tank_times
        # fields = ('id', 'machine', 'location', 'sub_location', 'humidity','tempreture','tempreture_low','tempreture_high','battery','user_name','delete_status','uuid','_uuid',"humidity_low","humidity_high","CO2_high","CO2_low","CO2",'updated_at','email')
        fields = '__all__'



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user