from django.shortcuts import render
from rest_framework import viewsets
from .models import Flight, Passenger
from .serializers import PassengerSerializer, FlightSerializer
from django.http import HttpResponse
from .models import Flight

# Create your views here.

# ViewSet for Flight
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# ViewSet for Passenger
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

def home(request):
    return HttpResponse(
        """
        <html>
            <body>
                <h1>Welcome and thank you for using our system! :)</h1>
                <p><a href="/admin/">click to use now!</a></p>
            </body>
        </html>
        
        """
    )
