import random
cpu = random.choice(range(1,101))
guess = ''
count = 0

while True:
  try:
    guess = int(input('Guess: '))
  except ValueError:
    print('Input number 1 - 100')
    continue
  if guess == cpu:
    print(f'Congrats you win! It took {count} guesses')
    yes = input('Go again? (yes/no) ')
    if yes == 'yes':
      count = 0
      cpu = random.choice(range(1,101))
    else:
      break
  elif guess > cpu:
    print('Number is lower')
    count += 1
  elif guess < cpu:
    print('Number is higher')
    count += 1
