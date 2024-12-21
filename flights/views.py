from flights import serializers
from flights import models

from rest_framework import viewsets
from rest_framework.decorators import action


class AirplaneViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating airplanes"""
    serializer_class = serializers.AirplaneSerializer
    queryset = models.Airplane.objects.all()


class FlightViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating flights"""
    serializer_class = serializers.FlightSerializer
    queryset = models.Flight.objects.all()

    
class ReservationViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating reservations"""
    serializer_class = serializers.ReservationSerializer
    queryset = models.Reservation.objects.all()
