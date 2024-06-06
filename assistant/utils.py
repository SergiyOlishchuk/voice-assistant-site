
from assistant.models import History

def get_user_history(request):
    if request.user.is_authenticated:
        return History.objects.filter(user=request.user).order_by('creating_timestamp')
    
    return None
