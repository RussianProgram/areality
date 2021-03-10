from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('objects/',views.objects, name='objects'),
    path('about_us/',views.about_us, name='about_us'),
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name='register'),
    path('edit/',views.edit,name='edit'),
]
