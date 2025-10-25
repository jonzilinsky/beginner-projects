#def fibo():
#  x = 1
#  y = 0
#  length = 1
#  while True:
#    try:
#      length = int(input('Which number in the Fibonacci sequence would you like? '))
#      break
#    except ValueError:
#      print('Please type integer')
#      continue
#  for i in range(1,length):
#    z = x + y
#    y = x
#    x = z
#  print(y)

#fibo()

def reco(length):
  if length == 0:
    return 0
  elif length == 1:
    return 1
  else:
    return reco(length -1) + reco(length - 2)

steps = int(input('Which number in the Fibonacci sequence would you like? ')) - 1
print(reco(steps))
