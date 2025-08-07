from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movie_home'),
    path('predict/', views.predict, name='movie_predict'),
]
