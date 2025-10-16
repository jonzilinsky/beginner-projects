import random

global humanscore, cpuscore
humanscore = 0
cpuscore = 0
options = ('r', 'p', 's')
ddict = {'r':'rock','p':'paper','s':'scissors'}
gogo = 'yes'

def score():
  return f'[Human Score: {humanscore} Computer Score: {cpuscore}]'

def play(z):
  global humanscore, cpuscore
  cpu = random.choice(options)
  print(f'Computer chooses: {ddict[cpu]} ', end='')
  if z == cpu:
    print('Tie!')
  elif ((z == 'r' and cpu == 's') or
    (z == 'p' and cpu == 'r') or
    (z == 's' and cpu == 'p')):
    humanscore += 1
    print(f'   Human wins! ', score())
  else:
    cpuscore += 1
    print(f'   Computer wins! ', score())

def main():
  global gogo
  human = input('Choose your move: r = rock, p = paper, s = scissors:\n')
  if human in options:
    play(human)
  else:
    print('\nMove not valid, try again? (yes/no)')
    gogo = input('')

while gogo == 'yes':
  main()

print(f'\nFinal:', score())
