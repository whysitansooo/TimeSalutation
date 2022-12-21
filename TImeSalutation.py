import time 

timestamp = float(time.strftime('%H'))
if timestamp >=5 and timestamp <12:
    print("Good morning")
elif timestamp >=12 and timestamp <18:
    print("Good afternoon")
elif timestamp >=18 and timestamp <=9:
    print("Good evening")
else:
    print("Good night")


# https://docs.python.org/3/library/time.html#time.strftime
