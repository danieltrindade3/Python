sal = float(input('Qual é o salário do funcionário? R$'))
if sal >= 1250:
    # nsal = sal + (sal * 10 / 100)
    nsal = sal + sal * 0.10
else:
    # nsal = sal + (sal * 15 / 100)
    nsal = sal + sal * 0.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal, nsal))