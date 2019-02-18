import datetime

today = datetime.date.today()

# Normal Collection is Thursday (Day 3 of 0index week)
next_collection = today + datetime.timedelta((3 - today.weekday()) % 7) 

print(next_collection.strftime('%a %d %b'))