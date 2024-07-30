sal = float(input('\033[33mQual é o salário do funcionário?\033[m R$'))
if sal >= 1250:
    # nsal = sal + (sal * 10 / 100)
    nsal = sal + sal * 0.10
else:
    # nsal = sal + (sal * 15 / 100)
    nsal = sal + sal * 0.15
print('Quem ganhava \033[32mR${:.2f}\033[m passa a ganhar \033[32mR${:.2f}\033[m'.format(sal, nsal))