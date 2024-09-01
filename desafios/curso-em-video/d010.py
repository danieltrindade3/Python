cor = {
    'normal':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'magenta':'\033[35m'
}
preço = float(input('{}Qual é o preço do produto? {}R$'.format(cor['amarelo'], cor['normal'])))
off = int(input('{}Quanto tem de desconto na loja?{} '.format(cor['amarelo'], cor['normal'])))
promo = preço - (preço * off / 100)
print('O produto que custava {}R${:.2f}{}, na promoção com desconto de {}{}%{} vai custar {}R${}.{}'.format(cor['azul'], preço, cor['normal'], cor['magenta'], off, cor['normal'], cor['verde'], promo, cor['normal']))