cor = {
    'normal':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'magenta':'\033[35m'
}
num = int(input('{}Digite um número:{} '.format(cor['amarelo'], cor['normal'])))
print('O {}dobro{} de {}{}{} vale {}{}{}.'.format(cor['magenta'], cor['normal'], cor['azul'], num, cor['normal'], cor['verde'], num * 2, cor['normal']))
print('O {}triplo{} de {}{}{} vale {}{}{}.'.format(cor['magenta'], cor['normal'], cor['azul'], num, cor['normal'], cor['verde'], num * 3, cor['normal']))
print('{}A raiz quadrada{} de {}{}{} é igual à {}{:.2f}{}'.format(cor['magenta'], cor['normal'], cor['azul'], num, cor['normal'], cor['verde'], pow(num, (1/2)), cor['normal']))