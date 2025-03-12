entry1 = input().split(" ")
entry2 = input().split(" ")

for i in range(0, 2):
    entry1[i] = int(entry1[i])
    entry2[i] = int(entry2[i])

    if i == 1:
        entry1[i+1] = float(entry1[i+1])
        entry2[i+1] = float(entry2[i+1])

total = entry1[1] * entry1[2] + entry2[1] * entry2[2]
print(f"VALOR A PAGAR: R$ {total:.2f}")
