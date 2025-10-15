for i in range(99, 0, -1):
  x = ''
  y = ''
  if i !=1:
    x = str(i) + ' bottles'
  else:
    x = str(i) + ' bottle'
  print(f"{x} of pop the wall, {x} of pop!")
  if i - 1 != 1:
    y = str(i - 1) + ' bottles'
  else:
    y = str(i - 1) + ' bottle'
  print(f"Take one down, pass it around, {y} of pop on the wall!")
