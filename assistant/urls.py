from django.urls import path

from assistant import views

app_name = 'assistant'

urlpatterns = [
	path('', views.index, name='index'),
	path('exec-command/', views.exec_command, name='exec_command'),
	path('recognize-audio/', views.recognize_audio, name='recognize_audio'),
	path('audio/<str:filename>/', views.get_audio, name='get_audio'),
]
