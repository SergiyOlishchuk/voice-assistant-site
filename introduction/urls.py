from django.urls import path

from introduction import views

app_name = 'introduction'

urlpatterns = [
    path('', views.index, name='index'),
]
