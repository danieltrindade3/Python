from time import sleep
cor = {
    'normal':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'magenta':'\033[35m',
    'ciano':'\033[36m'
}
nome = str(input('{}Digite o seu nome completo:{} '.format(cor['amarelo'], cor['normal']))).strip()
nome2 = nome.split()
print('{}Analisando o seu nome...{}'.format(cor['magenta'], cor['normal']))
sleep(3)
print('Seu nome em {}maiúsculas {}é {}{}{}'.format(cor['azul'], cor['normal'], cor['azul'], nome.upper(), cor['normal']))
print('Seu nome em {}minúsculas {}é {}{}{}'.format(cor['vermelho'], cor['normal'], cor['vermelho'], nome.lower(), cor['normal']))
print('Seu nome tem ao todo {}{} letras{}'.format(cor['verde'], len(nome) - nome.count(' '), cor['normal']))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome é {}{}{} e ele tem {}{} letras{}'.format(cor['magenta'], nome2[0], cor['normal'], cor['ciano'], len(nome2[0]), cor['normal']))