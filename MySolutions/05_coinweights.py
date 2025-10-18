gramwt = {'pennies':2.5, 'dimes':2.268, 'nickels':5, 'quarters':5.67}
poundwt = {'pennies':0.0055, 'dimes':0.0050, 'nickels':0.0110, 'quarters':0.0125}
coins = ['pennies','dimes','nickels','quarters']
userwts = {}
coinnum = {}
bigroll = 40
smallroll = 50

def gramsnum():
  for key, values in userwts.items():
    coinnum[key] = int(int(values)/gramwt[key])

def poundnum():
  for key, values in userwts.items():
    coinnum[key] = int(int(values)/poundwt[key])

def value():
  dime = (coinnum['dimes'] * .10)
  nickel = (coinnum['nickels'] * .05)
  quarter = (coinnum['quarters'] * .25)
  return (coinnum['pennies'] + dime + nickel + quarter)

unit = input('Choose weight unit: (grams/pounds)\n')

for i in coins:
  userwts[i] = input(f'What is the weight of {i}? ')

if unit == 'grams':
  gramsnum()
elif unit == 'pounds':
  poundnum()
else:
  print('Unit not recognized')
  exit()

print(f'Coin totals: {coinnum}')
print(f'Wrappers needed: Pennies {(coinnum['pennies']/smallroll)}, ', end='')
print(f'Dimes {(coinnum['dimes']/smallroll)}, ', end='')
print(f'Nickels {(coinnum['nickels']/smallroll)}, ', end='')
print(f'Quarters {(coinnum['quarters']/smallroll)}, ')
print(f'Total approximate value: ${round(value(),2)}')
