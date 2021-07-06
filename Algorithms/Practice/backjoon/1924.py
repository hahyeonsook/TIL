import sys

input = sys.stdin.readline
from datetime import datetime

x, y = map(int, input().split())
day_of_weeks = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
day = datetime(2007, x, y).weekday()
print(day_of_weeks[day])
