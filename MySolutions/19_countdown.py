import datetime, time

year = int(input('Choose year to countdown to: '))
month = int(input('Choose month to countdown to: '))
day = int(input('Choose day to countdown to: '))
hour = int(input('Choose hour to countdown to: '))
minute = int(input('Choose minute to countdown to: '))
second = int(input('Choose second to countdown to: '))
today = datetime.datetime.now() #.isoformat(' ', 'seconds')
usertime = datetime.datetime(year,month, day, hour, minute, second)

interval = usertime - today

while True:
  if usertime < today:
    print('TIME')
    break
  else:
    print(f'Time until {usertime} is:')
    print(str(interval).split('.')[0])
    time.sleep(2)
    today = datetime.datetime.now()
    interval = usertime - today
