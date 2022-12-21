from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', views.listings),
    path('about/', views.about),
    path('contact/', views.contact),
]
