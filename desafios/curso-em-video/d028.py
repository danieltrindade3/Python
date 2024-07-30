cor = {
    'normal':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
}
distância = float(input('{}Qual é a distância da sua viagem?{} '.format(cor['amarelo'], cor['normal'])))
print('Você está prestes a começar uma viagem de {}{:.1f}Km{}.'.format(cor['azul'], distância, cor['normal']))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de {}R${:.2f}{}'.format(cor['verde'], preço, cor['normal']))
'''preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de {}R${:.2f}{}'.format(cor['verde'], preço, cor['normal']))'''