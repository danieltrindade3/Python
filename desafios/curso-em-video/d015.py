from math import hypot
cor = {
    'normal':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'magenta':'\033[35m',
    'ciano':'\033[36m'
}
op = float(input('{}Comprimento do {}cateto oposto:{} '.format(cor['amarelo'], cor['magenta'], cor['normal'])))
adj = float(input('{}Comprimento do {}cateto adjacente:{} '.format(cor['amarelo'], cor['magenta'], cor['normal'])))
print('A hipotenusa vai medir {}{:.2f}'.format(cor['ciano'], hypot(op, adj)))