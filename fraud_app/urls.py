from django.urls import path
from . import views

urlpatterns = [
    path('', views.fraud_view, name='fraud_home'),
    path('predict/', views.fraud_predict, name='fraud_predict'),
]
