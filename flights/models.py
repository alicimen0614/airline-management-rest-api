from django.db import models

class Airplane(models.Model):
    """Database model for airplanes"""
    tail_number = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    capacity = models.IntegerField()
    production_year = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        """Return the model as a string"""
        return self.tail_number


class Flight(models.Model):
    """Database model for flights"""
    flight_number=models.CharField(max_length=255)
    departure = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey(Airplane,on_delete=models.CASCADE)

    def __str__(self):
        """Return the model as a string"""
        return self.flight_number
    

class Reservation(models.Model):
    """Database model for reservations"""
    passenger_name = models.CharField(max_length=255)
    passenger_email = models.CharField(max_length=255)
    reservation_code = models.CharField(max_length=255,unique=True,auto_created=True)
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.passenger_name
