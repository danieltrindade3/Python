cor = {
    'normal':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'magenta':'\033[35m',
    'ciano':'\033[36m'
}
frase = str(input('{}Digite uma frase:{} '.format(cor['amarelo'], cor['normal']))).upper().strip()
if frase.count('A') == 0:
    print('Nesta frase a letra {}a{} aparece {}nenhuma{} vez!'.format(cor['verde'], cor['normal'], cor['vermelho'], cor['normal']))
else:
    print('Nesta frase a letra {}a{} aparece {}{}{} vez(es)'.format(cor['ciano'], cor['normal'], cor['verde'], frase.count('A'), cor['normal']))
    print('A primeira letra {}a{} aparece na posição {}{}{}'.format(cor['ciano'], cor['normal'], cor['magenta'], frase.find('A') + 1, cor['normal']))
    print('A última letra {}a{} aparece na posição {}{}{}'.format(cor['ciano'], cor['normal'], cor['magenta'], frase.rfind('A') + 1, cor['normal']))