emotion = str(input("Please enter an emotion: "))
color = ('white')
if emotion == ('sad'):
    color = ('00aced')
elif emotion == ('happy'):
    color = ('fffc00')
elif emotion == ('angry'):
    color = ('bb0000')
elif emotion == ('jealous'):
	color = ('4dc247')
elif emotion == ('excited'):
	color = ('ff0084')
else:
    color = ('white')
print (color)