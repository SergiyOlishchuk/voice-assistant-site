from .assistant import find_in_google, find_video, weather

DATA_SET = {
    'знайди в інтернеті' : 'find_in_google', 
    'пошукай в інтернеті' : 'find_in_google', 
    'можеш знайти в інтернеті' : 'find_in_google', 
    'можеш пошукати в інтернеті' : 'find_in_google', 
    'чи можеш знайти в інтернеті' : 'find_in_google', 
    'знайди будь ласка в інтернеті' : 'find_in_google', 
    'пошукай будь ласка в інтернеті' : 'find_in_google', 
    'можеш будь ласка знайти в інтернеті' : 'find_in_google', 
    'можеш будь ласка пошукати в інтернеті' : 'find_in_google', 
    
    'знайди відео' : 'find_video', 
    'пошукай відео' : 'find_video', 
    'можеш знайти відео' : 'find_video', 
    'можеш пошукати відео' : 'find_video', 
    'чи можеш знайти відео' : 'find_video', 
    'знайди будь ласка відео' : 'find_video', 
    'пошукай будь ласка відео' : 'find_video', 
    'можеш будь ласка знайти відео' : 'find_video', 
    'можеш пошукати будь ласка відео' : 'find_video',
    
    'знайди на ютубі' : 'find_video', 
    'пошукай на ютубі' : 'find_video', 
    'можеш знайти на ютубі' : 'find_video', 
    'можеш пошукати на ютубі' : 'find_video', 
    'чи можеш знайти на ютубі' : 'find_video', 
    'знайди будь ласка на ютубі' : 'find_video', 
    'пошукай будь ласка на ютубі' : 'find_video', 
    'можеш будь ласка знайти на ютубі' : 'find_video', 
    'можеш пошукати будь ласка на ютубі' : 'find_video',
    
    'знайди в ютубі' : 'find_video', 
    'пошукай в ютубі' : 'find_video', 
    'можеш знайти в ютубі' : 'find_video', 
    'можеш пошукати в ютубі' : 'find_video', 
    'чи можеш знайти в ютубі' : 'find_video', 
    'знайди будь ласка в ютубі' : 'find_video', 
    'пошукай будь ласка в ютубі' : 'find_video', 
    'можеш будь ласка знайти в ютубі' : 'find_video', 
    'можеш пошукати будь ласка в ютубі' : 'find_video',
    
    'яка погода зараз в' : 'weather', 
    'яка погода в' : 'weather', 
    'яка температура зараз в' : 'weather', 
    'що по погоді в' : 'weather', 
    'погода' : 'weather', 
}

TO_FUNC = {
    'find_in_google' : find_in_google,
    'find_video' : find_video,
    'weather' : weather
}
