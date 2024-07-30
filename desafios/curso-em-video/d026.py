vel = int(input('\033[33mQual é a velocidade atual do carro?\033[m '))
if vel > 80:
    multa = (vel - 80) * 7
    print('\033[1;31mMULTADO! \033[mVocê excedeu o limite permitido que é de 80Km/h')
    print('\033[mVocê deve pagar uma multa de \033[1;31mR${:.2f}!'.format(multa))
print('\033[1;32mTenha um bom dia! \033[mDirija com segurança!')