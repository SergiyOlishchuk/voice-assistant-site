import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, JsonResponse
from django.template.loader import render_to_string
from django.conf import settings

import subprocess

from assistant_lib.execute_command import execute_command
from assistant_lib.recognize import recognize

from assistant.models import History

# Create your views here.
@login_required
def index(request):
    context = {'title' : 'Голосовий асистент'}
    
    return render(request, 'assistant/index.html', context)

def exec_command(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        
        History.objects.create(user=request.user, text=text, from_user=True)
        
        api_token = request.POST.get('api_token')
        
        audio_path = os.path.join(settings.BASE_DIR, 'media', 'audio', f'{request.user.username}_answer.wav')
        
        answer = execute_command(text, audio_path, api_token)
        History.objects.create(user=request.user, text=answer, from_user=False)
        
        audio_url = request.build_absolute_uri('/voice-assistant/audio/' + f'{request.user.username}_answer.wav')
        
        answer_html = render_to_string('assistant/user_part.html', {'user' : request.user, 'text' : text, 'answer' : answer})
        
        return JsonResponse({'success' : True, 'text' : answer_html, 'audio_path' : audio_url})
    
    return JsonResponse({'success' : False})
        
def recognize_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        save_path = os.path.join(settings.BASE_DIR, 'media', 'audio', f'{request.user.username}')
        wav_path = os.path.join(settings.BASE_DIR, 'media', 'audio', f'{request.user.username}_converted.wav')
        
        with open(save_path, 'wb') as file:
            for chunk in audio_file.chunks():
                file.write(chunk)
                
        subprocess.run(['ffmpeg', '-i', save_path, wav_path, '-y'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                
        return JsonResponse({'success' : True, 'text' : recognize(wav_path)})
    
    return JsonResponse({'success' : False, 'error' : 'No audio file received'})

def get_audio(request, filename):
    audio_path = os.path.join(settings.BASE_DIR, 'media', 'audio', filename)
    
    if os.path.exists(audio_path):
        return FileResponse(open(audio_path, 'rb'), content_type='audio/wav')
    
    return JsonResponse({'error' : 'Audio file not found'}, status=404)
