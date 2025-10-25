from wordlist import wordlist
import random
import os

word = random.choice(wordlist)
guesses = []
correctletters = []
gogo = 'yes'
count = 0

hang = ['''
|---|
|
|
|
|_____''',
'''
|---|
|   O
|
|
|_____''',
'''
|---|
|   O
|  /
|
|_____''',
'''
|---|
|   O
|  / \\
|
|_____''',
'''
|---|
|   O
|  /|\\
|
|_____''',
'''
|---|
|   O
|  /|\\
|  /
|_____''',
'''
|---|
|   O
|  /|\\
|  / \\
|_____''',
]


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

clear()
print(hang[0])
print('')
for i in word:
  print('_',end=' ')

while gogo == 'yes':
  guess = input('\nGuess a letter: ')
  if guess not in word:
    count = count + 1
    if count < 6:
      clear()
      print(hang[count])
      print('')
    else:
      clear()
      print(hang[6])
      print('')
      print(f'YOU LOSE!\nThe word was: {word}')
      break
  else:
    clear()
    print(hang[count])
    print('')
  guesses.append(guess)
  for i in word:
    if i in guesses:
      print(i,end=' ')
      correctletters.append(i)
      if sorted(list(set(correctletters))) == sorted(set(word)):
        gogo = 'no'
    else:
      print('_',end=' ')

if gogo == 'no':
  print('\nYOU WIN!')
