from datetime import date
cor = {
    'normal':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m'
}
ano = int(input('{}Que ano quer analisar?{} Coloque {}0{} para analisar o ano atual: '.format(cor['amarelo'], cor['normal'], cor['verde'], cor['normal'])))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {}{}{} é {}BISSEXTO{}!'.format(cor['amarelo'], ano, cor['normal'], cor['verde'], cor['normal']))
else:
    print('O ano de {}{}{} {}NÃO é BISSEXTO{}!'.format(cor['amarelo'], ano, cor['normal'], cor['vermelho'], cor['normal']))