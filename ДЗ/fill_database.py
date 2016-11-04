from main_app.models import *
import os
from django.utils import timezone
import random

def fill_db () :
    FILENAME_PATH = 'rand_text.txt'
    IMAGES_PATH = r'main_app\static'
    WHERE_MAX_WORDS_COUNT = 6
    DESCRIPTION_MAX_WORDS_COUNT = 200
    MAX_EVENTS_COUNT = 1000
    
    
    keys =  open( FILENAME_PATH, "r", encoding='utf-8').read().split(' ')

    # print(keys)
    
    (root, dirs, files) = next(os.walk( IMAGES_PATH ))
    images = list (filter ( lambda x : '.jpg' in x, files))
    # print (images)

    for j in range(MAX_EVENTS_COUNT):
        ev = Event()
        ev.img = random.choice(images)
        ev.name = "Мероприятие : " + random.choice(keys).title()
        ev.where = " ".join ( random.choice(keys).lower() for i in range(random.randint(0, WHERE_MAX_WORDS_COUNT)))
        ev.description = " ".join (random.choice(keys).lower() for i in range( random.randint(0, DESCRIPTION_MAX_WORDS_COUNT)))
        ev.when = timezone.now()
        ev.save()