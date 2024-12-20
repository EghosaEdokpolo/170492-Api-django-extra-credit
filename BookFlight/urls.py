from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, PassengerViewSet  

router = DefaultRouter()
router.register(r'flights', FlightViewSet, basename='flight')
router.register(r'passengers', PassengerViewSet, basename='passenger')

urlpatterns = [
    path('api/', include(router.urls)), 
]