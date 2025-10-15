import time
import random
x = 'yes'

answers = ['Yes', 'No', 'Maybe', 'This is the way', 'I wouldn\'t count on it',
  'Could be', 'Fo sho!', 'don\'t ask me that..', 'In another world, yes',
  'nah', 'That\'s guna be a yikes from me dawg', 'Definitely', 'Definitely not']

def dotdotdot():
  print(f"\nthinking", end='', flush=True)
  for i in range(0,3):
    time.sleep(.5)
    print('.', end='', flush=True)
  print('\n')
  time.sleep(1.5)
  print(random.choice(answers), flush=True)
  time.sleep(1.0)

while x == 'yes':
  input('Ask the Magic 8 Ball anything:\n')
  dotdotdot()
  x = input('\nGo again? (yes/no) ')
