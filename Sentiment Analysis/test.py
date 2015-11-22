import indicoio
import random

#song lists created using radio billboard list and indicoio algorithm on song lyrics

list1 = ["Sorry", "What do you mean", "Same Old Love", "Here", "Hit The Quan", "Good For You"]
list2 = ["Focus", "Where Ya At", "Hello", "Locked Away", "Lean On", "Confident"]
list3 = ["Jumpman", "Trap Queen", "Renegades", "White Iverson", "Shut Up and Dance", "Hotline Bling"]
list4 = ["Drag Me Down", "Downtown", "Perfect", "Again", "Stitches", "679"] 
list5 = ["My Way", "Ex's & Oh's", "Antidote", "Like I'm gonna lose you", "Tennessee Whiskey", "See You Again", "Watch Me", "On My Mind", "I'll Show You",
"Cheerleader", "The Hills", "Uptown Funk!", "Die a Happy Man", "How Deep Is Your Love", "Photograph", "Can't feel my face"]

indicoio.config.api_key = 'a894b47f344116b3d32d12de039bf690'
text_input = input('Tell me about your day: ')
sentiment = indicoio.sentiment_hq(text_input)
songTitle = ""
dayDescription = ""
print(sentiment)
#0<SUPERSAD<.25<SAD<.45<NEUTRAL<.6<HAPPY<.8<SUPERHAPPY<1
if sentiment < .15:
    dayDescription = ("Your day was: AWFUL")
    songTitle = (list1[(int)(random.random()*len(list1))])
else:
    if sentiment < .35:
        dayDescription = ("Your day was: BAD")
        songTitle = (list2[(int)(random.random()*len(list2))])
    else:
        if sentiment < .65:
            dayDescription = ("Your day was: OK")
            songTitle = (list3[(int)(random.random()*len(list3))])
        else:
            if sentiment <.9:
                dayDescription = ("Your day was: GOOD")
                songTitle = (list4[(int)(random.random()*len(list4))])
            else:
                dayDescription = ("Your day was: AWESOME")
                songTitle = (list5[(int)(random.random()*len(list5))])
print(dayDescription)
print(songTitle)