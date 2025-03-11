entry = list(map(int, input().split()))
horas = 0
minutos = 0
total1 = entry[0]*60 + entry[1]
total2 = entry[2]*60 + entry[3]

if total1 <= total2:
    horas = int((total2-total1)/60)
    minutos = int((total2-total1)%60)
else:
    total2 += 24*60
    horas = int((total2-total1)/60)
    minutos = int((total2-total1)%60)

horas, minutos = (24, 0) if horas == 0 and minutos == 0 else (horas, minutos)
print(f"O JOGO DUROU " + str(horas) + " HORA(S) E " + str(minutos) + " MINUTO(S)")