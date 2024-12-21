from django.urls import path,include
from rest_framework.routers import DefaultRouter
from flights import views

router = DefaultRouter()
router.register('airplanes',views.AirplaneViewSet)
router.register('flights',views.FlightViewSet)
router.register('reservations',views.ReservationViewSet)

urlpatterns = [
    path('', include(router.urls))
]

