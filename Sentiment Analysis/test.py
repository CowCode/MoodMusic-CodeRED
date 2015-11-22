import indicoio
indicoio.config.api_key = 'a894b47f344116b3d32d12de039bf690'
text_input = input('Tell me about your day: ')
sentiment = indicoio.sentiment_hq(text_input)
print(sentiment)
#0<SUPERSAD<.25<SAD<.45<NEUTRAL<.6<HAPPY<.8<SUPERHAPPY<1
if sentiment < .15:
    print ("SUPERSAD")
else:
    if sentiment < .35:
        print ("SAD")
    else:
        if sentiment < .65:
            print ("NEUTRAL")
        else:
            if sentiment <.9:
                print ("HAPPY")
            else:
                print ("SUPERHAPPY")