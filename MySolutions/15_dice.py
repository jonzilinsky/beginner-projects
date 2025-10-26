import random

stats = {}
gogo = 'yes'

while gogo == 'yes':
  try:
    sides = int(input('How many sides does will the dice have? '))
    rolls = int(input('How many times would you like to roll the dice? '))
  except ValueError:
      print('Please type integers for sides and rolls.')
      continue
  for i in range(rolls):
    choice = (random.choice(range(1,sides + 1)))
    stats[choice] = stats.get(choice, 0) + 1

  statssort = dict(sorted(stats.items()))

  for key, value in statssort.items():
    print(f'Number {key} rolled {value} times ({round(value/rolls*100)}%)')
  gogo = input('Would you like to go again? ')

