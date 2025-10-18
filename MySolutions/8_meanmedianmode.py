uinput = input("Enter list of numbers separated  by a space: ").split()
numbs = list(map(int, uinput))

def mean():
  a = int(input('How many decimal places would you like for the mean? '))
  print(f'Mean: {round((sum(numbs)/len(numbs)), a)}')

def median():
  numbssort = sorted(numbs)
  middle = len(numbssort)/2
  if len(numbssort) % 2 != 0:
    print(f'Median: {numbssort[int(middle - .5)]}')
  else:
    print(f'Medians: {numbssort[int(middle - 1)]} and {numbssort[int(middle)]}')

def mode():
  highest = 0
  modes = []
  ddict = {}
  for i in numbs:
      if i in ddict:
          ddict[i] += 1
      else:
          ddict[i] = 1
  for value in ddict.values():
    if value > highest:
        highest = value
  for key, value in ddict.items():
    if value == highest:
      modes.append(key)
  print(f'Mode: {set(modes)}')

mean()
median()
mode()
