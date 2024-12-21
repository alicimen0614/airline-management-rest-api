from django.db import models
import shortuuid
from django.core.validators import MinValueValidator

class Airplane(models.Model):
    """Database model for airplanes"""
    tail_number = models.CharField(max_length=10,null=False,blank=False)
    model = models.CharField(max_length=50,null=False,blank=False)
    capacity = models.PositiveIntegerField(null=False,blank=False)
    production_year = models.PositiveIntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        """Return the model as a string"""
        return f'{self.tail_number} - {self.model}' 


class Flight(models.Model):
    """Database model for flights"""
    flight_number=models.CharField(max_length=50,null=False,blank=False)
    departure = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey(Airplane,on_delete=models.CASCADE,related_name='flights')

    def __str__(self):
        """Return the model as a string"""
        return f"{self.flight_number}: {self.departure} to {self.destination}"
    
    
def generate_reservation_code():
    """Generate random reservation code with shortuuid package with low possibility of collision"""
    return shortuuid.ShortUUID().random(length=10)
    

class Reservation(models.Model):
    """Database model for reservations"""
    passenger_name = models.CharField(max_length=100,null=False,blank=False)
    passenger_email = models.EmailField(null=False,blank=False)
    reservation_code = models.CharField(max_length=10,unique=True,default=generate_reservation_code)
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE,related_name='reservations')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return f"{self.reservation_code} - {self.passenger_name}"
    
