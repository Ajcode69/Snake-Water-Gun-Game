import random
def game(a,b):
  if a=="S" :
    if b=="W":
      return 'Player lost'
    elif b=="G":
      return 'Player won'
    else:
      return 'tie'
  if a=="W" :
    if b=="G":
      return 'Player lost'
    elif b=="S":
      return 'Player won'
    else:
      return 'tie'
  if a=="G" :
    if b=="S":
      return 'Player lost'
    elif b=="W":
      return 'Player won'
    else:
      return 'tie'
  
  
  



f=random.randrange(0,3)
if f==1:
  comp='S'
elif f==2:
  comp="W"
else:
  comp="G"
Player=input("Player's Input ")
print(comp)
print(game(comp,Player))
