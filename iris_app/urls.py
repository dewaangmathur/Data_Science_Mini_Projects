from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='iris_home'),
    path('predict/', views.predict, name='iris_predict'),
]
