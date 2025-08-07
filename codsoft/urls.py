from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Project app routes
    path('titanic/', include('titanic_app.urls')),
    path('', include('home_app.urls')),  # Homepage
    path('movie/', include('movie_app.urls')),
    path('iris/', include('iris_app.urls')),
    path('sales/', include('sales_app.urls')),
    path('fraud/', include('fraud_app.urls')),
    path('', include('home_app.urls')),  # homepage at /
]
