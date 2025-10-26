menu = {
0: '',
'1': ['Chicken Strips', 3.50],
'2': ['French Fries', 2.50],
'3': ['Hamburger', 4.00],
'4': ['Hotdog', 3.50],
'5': ['Large Drink', 1.75],
'6': ['Medium Drink', 1.50],
'7': ['Milk Shake', 2.25],
'8': ['Salad', 3.75],
'9': ['Small Drink', 1.25]
}

prettymenu ='''
Menu:
1. Chicken Strips - $3.50
2. French Fries - $2.50
3. Hamburger - $4.00
4. Hotdog - $3.50
5. Large Drink - $1.75
6. Medium Drink - $1.50
7. Milk Shake - $2.25
8. Salad - $3.75
9. Small Drink - $1.25

Type numbers of items for order:
(example '449' for 2 Hotdogs and 1 Small Drink)
'''

def main():
  print(prettymenu)
  while True:
    order = input('')
    if order.isdigit():
      break
    else:
      print('Please type integers with no spaces for order:') 
  cost = []
  items = {}

  for i in order:
    cost.append(menu[i][1])
    name = menu[i][0]
    items[name] = items.get(name, 0) + 1

  print(items)
  print(f'Total cost: ${sum(cost):.2f}')

while True:
  main()
  gogo = input('Order again? (yes/no):  ')
  if gogo != 'yes':
    break
