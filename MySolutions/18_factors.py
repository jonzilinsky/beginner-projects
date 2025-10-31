numm = int(input('Choose a number to print factors of: '))
llist = []
def factors(x):
  for i in range(1,x + 1):
    if x % i == 0:
      llist.append(i)
  for i in llist:
    if i != numm:
      print(f'{i}, ',end='')
    else:
      print(i,end='')
factors(numm)
if len(llist) == 2:
  print('\nThe number is prime')
