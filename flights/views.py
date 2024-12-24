from django.shortcuts import get_object_or_404

from flights import serializers
from flights import models

from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend


class AirplaneViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating airplanes"""
    serializer_class = serializers.AirplaneSerializer
    queryset = models.Airplane.objects.all()

    @action(detail=True, methods=['GET'])
    def flights(self, request, pk=None):
        """Custom action to retrieve flights of a specific airplane"""
        airplane = get_object_or_404(models.Airplane, pk=pk)
        flights = airplane.flights.all()
        serializer = serializers.FlightSerializer(flights, many=True)

        return Response(serializer.data)


class FlightViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating flights"""
    serializer_class = serializers.FlightSerializer
    queryset = models.Flight.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['departure','destination','departure_time','arrival_time']
    search_fields = ['departure','destination','departure_time','arrival_time']
    ordering_fields = ['departure','destination','departure_time','arrival_time']
    ordering = ['departure_time']
    

    @action(detail=True, methods=['GET'])
    def reservations(self, request, pk=None):
        """Custom action to retrieve reservations of a specific flight"""
        flight = get_object_or_404(models.Flight, pk=pk)
        reservations = flight.reservations.all()
        serializer = serializers.ReservationSerializer(reservations, many=True)

        return Response(serializer.data)
    

class ReservationViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating reservations"""
    serializer_class = serializers.ReservationSerializer
    queryset = models.Reservation.objects.all()
