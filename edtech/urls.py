from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("live_stt/", views.live_stt_view, name="live_stt_view")
]