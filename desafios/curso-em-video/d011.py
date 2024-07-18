sal = float(input('Qual é o salário do funcionário? R$'))
aum = sal + (sal * 15 / 100)
print('Um funcionário que ganhava {}, com um aumento de 15%, passa a receber {:.2f}'.format(sal, aum))