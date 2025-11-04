import random
gogo = 'y'
deck = {'AH':1,'2H':2,'3H':3,'4H':4,'5H':5,'6H':6,'7H':7,
  '8H':8,'9H':9,'10H':10,'JH':10,'QH':10,'KH':10,
  'AC':1,'2C':2,'3C':3,'4C':4,'5C':5,'6C':6,'7C':7,
  '8C':8,'9C':9,'10C':10,'JC':10,'QC':10,'KC':10,
  'AS':1,'2S':2,'3S':3,'4S':4,'5S':5,'6S':6,'7S':7,
  '8S':8,'9S':9,'10S':10,'JS':10,'QS':10,'KS':10,
  'AD':1,'2D':2,'3D':3,'4D':4,'5D':5,'6D':6,'7D':7,
  '8D':8,'9D':9,'10D':10,'JD':10,'QD':10,'KD':10}
cards = []

def cardpull():
  card = random.choice(list(deck.keys()))
  if card in cards:
    return
  else:
    cards.append(card)
    print(card)

cardpull()
while gogo == 'y':
  cardpull()
  totalcards = []
  for i in cards:
    totalcards.append(deck[i])
  total = sum(totalcards)
  print(total)
  if total < 21:
    gogo = input('hit? (y/n): ')
  elif total == 21:
    print('You win!')
    break
  else:
    print('You lose.')
    break
