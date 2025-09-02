from rest_framework import serializers
from .models import User,Country, State, City

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'country_code', 'curr_symbol', 'phone_code','my_user']


class StateSerializer(serializers.ModelSerializer):
    my_country__name = serializers.SerializerMethodField()
    my_country__my_user__email = serializers.SerializerMethodField()

    class Meta:
        model = State
        fields = ['id', 'name', 'state_code', 'gst_code', 'country', 'my_country__name', 'my_country__my_user__email']

    def get_my_country__name(self, obj):
        return obj.country.name

    def get_my_country__my_user__email(self, obj):
        return obj.country.my_user.email


class CitySerializer(serializers.ModelSerializer):
    my_state__name = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = [
            'id', 'name', 'city_code', 'phone_code', 'population',
            'avg_age', 'num_of_adult_males', 'num_of_adult_females',
            'state', 'my_state__name'
        ]

    def get_my_state__name(self, obj):
        return obj.state.name
