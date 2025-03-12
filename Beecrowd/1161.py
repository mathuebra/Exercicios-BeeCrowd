import sys

def fatorial (number):
    if number == 0:
        return 1
    return number * fatorial(number-1)

for line in sys.stdin:
    x, y = map(int, line.split())
    print(fatorial(x) + fatorial(y))