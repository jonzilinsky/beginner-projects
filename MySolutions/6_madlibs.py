llist = [
  'ADJECTIVE',
  'ADJECTIVE',
  'NOUN (singular)',
  'PLURAL NOUN',
  'ADJECTIVE',
  'COLOR',
  'PLURAL NOUN',
  'ADJECTIVE',
  'NOUN (singular)',
  'VERB (present tense)']

words = []

for i in range(len(llist)):
  words.append(input(f'Type one {llist[i]}: '))

if words[1].startswith(('a','e','i','o','u')):
  a1 = 'an'
else:
  a1 = 'a'

print(f'''\nYesterday morning, I woke up and immediately noticed a {words[0]} smell.
I looked out my window and saw {a1} {words[1]} {words[2]} floating down the street!
It was being chased by {words[3]} wearing {words[4]} {words[5]} {words[6]}.
I quickly grabbed my {words[7]} {words[8]} and decided to {words[9]}.
What a way to start the day!''')
