nome = str(input('\033[33mQual o seu nome completo?\033[m ')).strip()
print('O seu nome tem \033[35mSilva?\033[36m {}'.format('silva' in nome.lower()))