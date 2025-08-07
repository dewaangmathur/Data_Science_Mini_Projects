from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sales_home'),
    path('predict/', views.predict, name='sales_predict'),
]
