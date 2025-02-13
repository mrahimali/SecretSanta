
from django.urls import path, include
from .views import SecretSantaView

urlpatterns = [
    path('', SecretSantaView.as_view(), name='home' ),
]