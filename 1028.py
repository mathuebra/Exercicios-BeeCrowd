import math

total = int(input())
entry = []

for i in range(total):
    entry.append(input().split(' '))
    print(int(math.gcd(int(entry[i][0]), int(entry[i][1]))))

