from __future__ import unicode_literals

from django.urls import path

from paypal.standard.ipn import views

urlpatterns = [
    path('', views.ipn, name="paypal-ipn"),
]
