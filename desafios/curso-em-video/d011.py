cor = {
    'normal':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'magenta':'\033[35m'
}
sal = float(input('{}Qual é o salário do funcionário? {}R$'.format(cor['amarelo'], cor['normal'])))
aum = sal + (sal * 15 / 100)
print('Um funcionário que ganhava {}R${}{}, com um aumento de {}15%{}, passa a receber {}R${:.2f}{}'.format(cor['verde'], sal, cor['normal'], cor['magenta'], cor['normal'], cor['azul'], aum, cor['normal']))