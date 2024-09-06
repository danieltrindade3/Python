import math
cor = {
    'normal':'\033[m',
    'amarelo':'\033[33m',
    'magenta':'\033[35m',
    'ciano':'\033[36m'
}
num = float(input('{}Digite um valor:{} '.format(cor['amarelo'], cor['normal'])))
print('O valor digitado foi {}{}{} e a porção inteira é {}{}'.format(cor['magenta'], num, cor['normal'], cor['ciano'], math.trunc(num)))