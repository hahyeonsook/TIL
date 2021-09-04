import sys

input = sys.stdin.readline
notes = [0] + list(map(int, input().split()))
first = notes[1]
descending = False
mixed = False
if first == 8:
    descending = True
    notes = [0] + notes[::-1][:-1]

for i in range(1, 9):
    if notes[i] != i:
        mixed = True
        break

if mixed:
    print("mixed")
elif descending:
    print("descending")
else:
    print("ascending")
