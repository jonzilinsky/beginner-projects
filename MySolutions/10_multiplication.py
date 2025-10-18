table = int(input('Choose highest number in multiplication table: (e.g. 9 or 12) '))
llist = list(range(1,table+1))

for i in llist:
  for j in llist:
    if len(str(i*j)) == 1:
      print(f'    {i*j} ', end='')
    elif len(str(i*j)) == 2:
      print(f'   {i*j} ', end='')
    elif len(str(i*j)) == 3:
      print(f'  {i*j} ', end='')
    else:
      print(f' {i*j} ', end='')
  print('\n')
