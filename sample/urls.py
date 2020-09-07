from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='sampleapp-home'), # the home page is rep by '' and the view home will handle the logic
    path('about/',views.about,name='sampleapp-about'),
]
