total = int(input())
count = []
count_recursive = []
sum_total = 0
sum_calls = 0

def fib(n):
    if n == 0:
        count.append(0)
        return 0
    elif n == 1:
        count.append(1)
        return 1
    else: 
        count_recursive.append(1)
        return fib(n-1) + fib(n-2)


for i in range(total):
    current = int(input())
    result = fib(current)
    for j in count:
        sum_total += count[j]
    for j in count_recursive:
        sum_calls += count_recursive[j]
    print(f"fib(" + str(current) +  ") = " + str(sum_calls) + " calls = " + str(sum_total))