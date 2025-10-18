def coinvert():
  coins = giveback % 1
  coins = coins * 100
  quart = int(coins / 25)
  dimes = int((int(coins - quart*25)) / 10)
  nickels = int((int(coins - quart*25 - dimes*10)) / 5)
  pennies = int(coins - quart*25 - dimes*10 - nickels*5)
  ddict = {'Quarters':quart, 'Dimes':dimes, 'Nickels':nickels, 'Pennies':pennies}
  return ddict

while True:
  try:
    price = input('\nHow much the total price is: $')
    given = input('How much cash the customer gave: $')
    giveback = round((float(given) - float(price)), 2)
    print(f'\nTotal change to give back: ${giveback}\n{coinvert()}')
    check = input('Another transaction? (y/n)\n')
    if check == 'y':
      continue
    else:
      break
  except ValueError:
    print('Incorrect value inputs')
    continue
