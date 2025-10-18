side1 = side2 = side3 = 0
llist = [side1, side2, side3]
go = 'yes'

def main():
  for i in range(len(llist)):
    while True:
      try:
        llist[i] = int(input(f'Triangle side {i + 1} length: '))
        break
      except ValueError:
        print("Needs integer for length")
        continue

  llist.sort()
  xx = ((llist[0] ** 2) + (llist[1] ** 2)) == llist[2] ** 2

  if xx:
    print("That is a right triangle")
  else:
    print("That is not a right triangle")

while go == 'yes':
  main()
  go = input('\nTry another triangle? (yes/no)\n')
