from django.db import models
import shortuuid

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
    
    
def generate_reservation_code():
    """Generate random reservation code with shortuuid package with low possibility of collision"""
    return shortuuid.ShortUUID().random(length=10)
    

class Reservation(models.Model):
    """Database model for reservations"""
    passenger_name = models.CharField(max_length=255)
    passenger_email = models.CharField(max_length=255)
    reservation_code = models.CharField(max_length=10,unique=True,default=generate_reservation_code)
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.passenger_name
    
