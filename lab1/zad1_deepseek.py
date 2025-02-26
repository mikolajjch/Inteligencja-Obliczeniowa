import math
from datetime import datetime

def biorhythm(t, cycle):
    return math.sin(2 * math.pi * t / cycle)

def main():
    name = input("Name: ")
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))

    birth = datetime(year, month, day)
    now = datetime.now()
    days_alive = (now - birth).days
    print(f'You have been alive for {days_alive} days.')

    cycles = {
        "physical": 23,
        "emotional": 28,
        "intellectual": 33
    }

    for cycle_type, cycle_length in cycles.items():
        val = biorhythm(days_alive, cycle_length)
        print(f'{cycle_type.capitalize()} score: {val:.2f}')
        if val > 0.5:
            print("Great result!")
        elif val < -0.5:
            next_val = biorhythm(days_alive + 1, cycle_length)
            if next_val > val:
                print("Don't worry, tomorrow will be better!")
        else:
            print("Standard result")

if __name__ == "__main__":
    main()