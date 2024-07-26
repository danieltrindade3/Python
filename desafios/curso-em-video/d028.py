distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))
else:
    preço = distância * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))
'''preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''