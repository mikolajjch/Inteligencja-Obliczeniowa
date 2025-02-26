import math
from datetime import datetime

def biorhythm(t,cycle):
    return math.sin(2*math.pi*t/cycle)

name = input("Name: ")
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

birth = datetime(year, month, day)
now = datetime.now()
days_alive = (now - birth).days
print(f'been alive for {days_alive} days')

cycles = {
    "physical": 23,
    "emotional": 28,
    "intellectual": 33
}

for c in cycles:
    val = biorhythm(days_alive, cycles[c])
    print(f'{c} score : {val}' )