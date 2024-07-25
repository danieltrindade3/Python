num = int(input('Por favor, digite um número qualquer: '))
res = num % 2
if res == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))