from rest_framework import serializers

from flights import models

from django.template.loader import render_to_string
from django.core.mail import send_mail

from dotenv import load_dotenv
from django.utils.timezone import now
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
        if 'departure_time' in data and 'arrival_time' not in data:
            raise serializers.ValidationError("Arrival time must be provided with the departure time")
        
        if 'arrival_time' in data and 'departure_time' not in data:
            raise serializers.ValidationError("Departure time must be provided with arrival time")

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
        """Validate reservation to check flight capacity and flight departure time"""
        # Only perform flight validation if 'flight' field is being updated
        if 'flight' in data:
            flight = data['flight']
            current_reservations = models.Reservation.objects.filter(flight=flight)
            current_capacity = current_reservations.count()
            flight_departure_time = flight.departure_time
            current_time = now()
            
            if current_time >= flight_departure_time:
                raise serializers.ValidationError("Reservation cannot be made as the flight has already departed.")

            if current_capacity >= flight.airplane.capacity:
                raise serializers.ValidationError(f"Reservation cannot be made. Flight {flight.flight_number} is fully booked.")

        return data
    
    def create(self, validated_data):
        """Customize create function to send email after creating reservation"""
        reservation = models.Reservation.objects.create(**validated_data)
        subject = 'Reservation Confirmation'
        context = {
        'reservation': reservation,
        'departure_time':reservation.flight.departure_time.strftime('%d.%m.%Y %H:%M')}
        app_email = os.getenv("APP_EMAIL")
        app_password = os.getenv("APP_PASSWORD")
        email_host = os.getenv("APP_EMAIL_HOST")

        if app_email and app_password and email_host:
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