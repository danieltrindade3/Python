vel = int(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')