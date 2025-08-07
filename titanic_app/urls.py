from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='titanic_home'),
    path('predict/', views.predict, name='titanic_predict'),
]
