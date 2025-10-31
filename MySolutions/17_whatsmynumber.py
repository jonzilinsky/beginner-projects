for i in range(1,1000):
  booll = True
  string = (str(i))
  nums = []
  if i  == 1:
    booll = False
  else:
    for j in range(2, i):
      if (i%j == 0):
        booll = False
  for char in string:
    number = int(char)
    nums.append(number)
  if len(string) < 2:
    booll = False
  elif (nums[0] + nums[1]) % 2 == 0:
    booll = False
  for j in string:
    if j == '1' or j == '7':
      booll = False
  if sum(nums) > 10:
      booll = False
  if len(string) > 2:
    if nums[-2] % 2 == 1 or nums[-2] < 2:
      booll = False
  if len(string) != nums[-1]:
    booll = False
  if booll:
    print(i)
