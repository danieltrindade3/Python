from time import sleep
cor = {
    'normal':'\033[m',
    'amarelo':'\033[33m',
    'magenta':'\033[35m',
    'ciano':'\033[36m'
}
num = int(input('{}Informe um número:{} '.format(cor['amarelo'], cor['normal'])))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('{}Analisando o número {}...{}'.format(cor['magenta'], num, cor['normal']))
sleep(3)
print('Unidade: {}{}'.format(cor['ciano'], u))
print('{}Dezena: {}{}'.format(cor['normal'], cor['ciano'], d))
print('{}Centena: {}{}'.format(cor['normal'], cor['ciano'], c))
print('{}Milhar: {}{}'.format(cor['normal'], cor['ciano'], m))