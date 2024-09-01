cor = {
    'normal':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}
dia = int(input('{}Quantos dias alugados?{} '.format(cor['amarelo'], cor['normal'])))
km = float(input('{}Quantos Km rodados?{} '.format(cor['amarelo'], cor['normal'])))
pago = (dia * 60) + (km * 0.15)
print('O total a pagar é de {}R${:.2f}'.format(cor['verde'], pago))