from rest_framework import serializers
from .models import Flight, Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'flight']

class FlightSerializer(serializers.ModelSerializer):
    passengers = PassengerSerializer(many=True, read_only=True) 

    class Meta:
        model = Flight
        fields = ['id', 'flight_number', 'departure', 'arrival', 'origin', 'destination', 'capacity', 'passengers']
