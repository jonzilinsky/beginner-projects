count = 0

with open('file2.txt') as file, open('out.txt', 'w') as out:
  for line in file:
    for i in range(len(line)):
      if line[i] == 'i':
        if (line[i+1] == ' ') or (line[i+1] == '-'):
          out.write('I')
          count += 1
        else:
          out.write('i')
      else:
        out.write(line[i])
  out.write(f'\n{count} Corrections')
