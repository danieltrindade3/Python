cor = {
    'normal':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'ciano':'\033[36m'
}
real = float(input('{}Quanto você tem na carteira? {}R$'.format(cor['amarelo'], cor['normal'])))
dolar = real / 5.09
euro = real / 5.43
print('Com {}R${:.2f}{} você pode comprar {}US${:.2f}{}'.format(cor['verde'], real, cor['normal'], cor['ciano'], dolar, cor['normal']))
print('Com {}R${:.2f}{} você pode comprar {}EUR €{:.2f}'.format(cor['verde'], real, cor['normal'], cor['ciano'], euro))