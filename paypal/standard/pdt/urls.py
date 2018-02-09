from __future__ import unicode_literals

from django.urls import path

from paypal.standard.pdt import views

urlpatterns = [
    path('', views.pdt, name="paypal-pdt"),

]
