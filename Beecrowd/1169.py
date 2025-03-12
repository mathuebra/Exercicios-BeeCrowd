import sys
import math

def solve(number):
    if number == 0: return 1
    return 2**(number) + solve(number-1)

size = input()

for line in sys.stdin:
    current = int(line)
    print(f'{math.floor(solve(current-1)/(12*10**3))}' + ' kg')