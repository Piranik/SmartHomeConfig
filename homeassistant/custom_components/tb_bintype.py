import datetime

today = datetime.date.today()
if today.weekday() > 3:
    today = today + datetime.timedelta((0 - today.weekday()) % 7)

week_number = today.isocalendar()[1]

if (week_number % 2) == 0:
    collection_type = "General Waste (Red Lid), Green Waste (Green Lid)"
else:
    collection_type = "General Waste (Red Lid), Recycling (Yellow Lid)"

print(collection_type)