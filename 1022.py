import math

total = int(input())
expressions = []
output_sample = []

def simplify(n1, d1):
    gcd = math.gcd(n1, d1)
    return int(n1/gcd),int(d1/gcd)

for i in range(total):
    expressions.append(input().split())
    n1 = int(expressions[i][0])
    d1 = int(expressions[i][2])
    n2 = int(expressions[i][4])
    d2 = int(expressions[i][6])

    if expressions[i][3] == '+':
        output_sample.append(str(n1*d2 + n2*d1) + '/' + str(d1*d2))
    if expressions[i][3] == '-':
        output_sample.append(str(n1*d2 - n2*d1) + '/' + str(d1*d2))
    if expressions[i][3] == '*':
        output_sample.append(str(n1*n2) + '/' + str(d1*d2))
    if expressions[i][3] == '/':
        output_sample.append(str(n1*d2) + '/' + str(n2*d1))

    #new_n1, new_d1 = simplify(int(output_sample[i].split('/')))
    new_n1, new_d1 = output_sample[i].split('/')
    new_n1, new_d1 = simplify(int(new_n1), int(new_d1))

    print(output_sample[i] + ' = ' + str(new_n1) + '/' + str(new_d1))
