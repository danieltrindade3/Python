cor = {
    'normal':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m'
}
num = int(input('{}Digite um número:{} '.format(cor['amarelo'], cor['normal'])))
suc = num + 1
ant = num - 1
print('O antecessor de {}{}{} é: {}{}{}, e o sucessor é: {}{}'.format(cor['azul'], num, cor['normal'], cor['vermelho'], ant, cor['normal'], cor['verde'], suc))