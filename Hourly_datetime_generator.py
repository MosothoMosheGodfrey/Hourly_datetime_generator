from datetime import datetime, timedelta

# Format datetime(Year, month, day, hour)
# e.g.... datetime(1957, 1, 1, 1), no need to write single digits as double: i.e 0 as 00
Begin_Date = datetime(1957, 1, 1, 1)
End_Date = datetime(2022, 1, 31, 23)

# Function generator....
def Hourly_datetime_generator(Begin_Date, End_Date):
    while Begin_Date < End_Date:
        yield Begin_Date
        Begin_Date = Begin_Date + timedelta(hours=1)
# Convert list to string...
datetime_str =[str(x)[:13] for x in Hourly_datetime_generator(Begin_Date, End_Date)]

print(datetime_str)
