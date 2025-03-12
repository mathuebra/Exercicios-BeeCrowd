import sys

for line in sys.stdin:
    x, y = line.split()
    if '0' in (x, y):
        break
    size_x = len(x)
    size_y = len(y)
    
    i = 1
    carry_op = 0
    current_carry = 0
    
    while i <= size_x or i <= size_y:
        number_x = int(x[size_x - i]) if i <= size_x else 0
        number_y = int(y[size_y - i]) if i <= size_y else 0
        
        if (number_x + number_y + current_carry) >= 10:
            carry_op += 1
            current_carry = 1
        else:
            current_carry = 0
        
        i += 1
    
    if carry_op == 0:
        print('No carry operation.')
    elif carry_op == 1:
        print(f'{carry_op} carry operation.')
    else:
        print(f'{carry_op} carry operations.')
