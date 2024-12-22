from rest_framework import serializers

from flights import models

from django.template.loader import render_to_string
from django.core.mail import send_mail

from dotenv import load_dotenv
import os

load_dotenv()
class AirplaneSerializer(serializers.ModelSerializer):
    """Serializes an airplane object"""

    class Meta:
        model = models.Airplane
        fields=('__all__')


class FlightSerializer(serializers.ModelSerializer):
    """Serializes a flight object"""

    class Meta:
        model = models.Flight
        fields=('__all__')

    def validate(self,data):
        """Basic validation for departure_time and arrival_time"""
        if(data['departure_time']>=data['arrival_time']):
            raise serializers.ValidationError("Departure time must be earlier than arrival time")
        
        return data


class ReservationSerializer(serializers.ModelSerializer):
    """Serializes a reservation object"""

    class Meta:
        model = models.Reservation
        fields = '__all__'
        read_only_fields = ('reservation_code',)

    def validate(self,data):
        """Validate reservation to check flight capacity"""
        flight = data.get('flight')

        current_reservations = models.Reservation.objects.filter(flight=flight)
        current_capacity = current_reservations.count()

        if current_capacity >= flight.airplane.capacity:
            raise serializers.ValidationError(f"Cannot make reservation. Flight {flight.flight_number} is fully booked.")
        return data
    
    def create(self, validated_data):
        reservation = models.Reservation.objects.create(**validated_data)
        subject = 'Reservation Confirmation'
        context = {
        'reservation': reservation,
        'departure_time':reservation.flight.departure_time.strftime('%d.%m.%Y %H:%M')
    }
        html_content = render_to_string('flights/reservation_email.html',context)
        from_email = f'Flight Support Team < {os.getenv("APP_EMAIL")} >'
        recipient_list = [reservation.passenger_email]
        
        send_mail(
            subject,
            "",
            from_email,
            recipient_list,
            fail_silently=False,
            html_message=html_content
        )
        
        return reservation