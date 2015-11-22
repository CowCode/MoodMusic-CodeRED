import indicoio
indicoio.config.api_key = 'a894b47f344116b3d32d12de039bf690'
text_input = input('Tell me about your day: ')
print(indicoio.sentiment_hq(text_input))
#0<SUPERSAD<.25<SAD<.45<NEUTRAL<.6<HAPPY<.8<SUPERHAPPY<1
if 