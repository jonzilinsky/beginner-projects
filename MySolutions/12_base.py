ddict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
otherdict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
good = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']


def too10(z, listt):
  n = len(listt) - 1
  newllist = []
  for i in listt:
    if i.isdigit():
      value = int(i) * (z ** n)
      newllist.append(value)
      n = n - 1
    elif i.isalpha():
      value = ddict[i] * (z ** n)
      newllist.append(value)
      n = n - 1
  return sum(newllist)

def from10(btoo, x):
  llist = []
  if x == 0:
    return '0'
  while x >= 1:
    z = int(x % btoo)
    if z < 10:
      llist.insert(0,z)
    else:
      llist.insert(0,otherdict[z])
    x = x // btoo
  tring = "".join([str(i) for i in llist])
  return tring

def main():
  llist = list(input('Number to convert: ').upper())

  while True:
    try:
      base = int(input('Base to convert from (2 to 16) : '))
      too = int(input('Base to convert to (2 to 16) : '))
      if base < 2 or base > 16 or too < 2 or too > 16:
        raise ValueError('Out of range')
      break
    except ValueError:
      print('Print integer from 2 to 16')

  for i in llist:
    if i not in good[0:base]:
      print(f'Number to convert not in base {base}')
      return

  base10 = too10(base,llist)
  print(from10(too,base10))

while True:
  main()
  gogo = input('Would you like to continue converting? (yes/no) : ')
  if gogo == 'yes':
    continue
  else:
    break
