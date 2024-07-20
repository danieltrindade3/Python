n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2
print('A sua nota máxima foi {:.1f}'.format(m))
if m >= 5:
    print('Você passou de ano! PARABÉNS!')
else:
    print('Infelizmente você não passou de ano. ESTUDE MAIS!')
# print('PARABÉNS!' if m >= 5 else 'ESTUDE MAIS!')