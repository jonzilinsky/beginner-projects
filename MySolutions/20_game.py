import os, time, random

userhp = 100
cpuhp = 100

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def userjab():
  global cpuhp
  hit = random.choice(range(18,25))
  clear()
  print(f'User jabbed CPU for {hit} HP\n')
  cpuhp = cpuhp - hit

def userswing():
  global cpuhp
  hit = random.choice(range(0,51))
  clear()
  print(f'User swing hits CPU for {hit} HP\n')
  cpuhp = cpuhp - hit

def userheal():
  global userhp
  hit = random.choice(range(15,35))
  clear()
  print(f'User for {hit} HP\n')
  userhp = userhp + hit

def cpujab():
  global userhp
  hit = random.choice(range(18,25))
  clear()
  print(f'CPU jabbed User for {hit} HP\n')
  userhp = userhp - hit

def cpuswing():
  global userhp
  hit = random.choice(range(0,51))
  print(f'CPU swing hits user for {hit} HP\n')
  userhp = userhp - hit

def cpuheal():
  global cpuhp
  hit = random.choice(range(15,35))
  print(f'CPU healed for {hit} HP\n')
  cpuhp = cpuhp + hit

def cpumove():
  global cpuhp
  llist = [1,2,3]
  if cpuhp > 35:
    cpuchoice = random.choice(llist)
    if cpuchoice == 1:
      cpujab()
    elif cpuchoice == 2:
      cpuswing()
    elif cpuchoice == 3:
      cpuheal()
  else:
    cpuchoice = random.choices((llist), weights=[20,20,60])

def stats():
  print(f'User HP: {userhp}      CPU HP: {cpuhp}\n')

def showmoves():
  print('1. Jab   2. Swing   3. Heal\n')

while userhp>1 and cpuhp>1:
  clear()
  stats()
  showmoves()
  move = input('Choose a move; 1, 2, or 3:  ')
  if move == '1':
    userjab()
  elif move == '2':
    userswing()
  elif move == '3':
    userheal()
  else:
    print('Invalid move; choose 1, 2, or 3')
  cpumove()
  stats()
  putput = input('Press any key to continue ')

if cpuhp>1:
  print('CPU wins!')
else:
  print('User wins!')
