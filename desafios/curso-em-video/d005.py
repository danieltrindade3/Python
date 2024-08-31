cor = {
    'normal':'\033[m',
    'amarelo':'\033[33m',
    'magenta':'\033[35m',
    'ciano':'\033[36m'
}
n1 = float(input('{}Primeira nota do aluno:{} '.format(cor['amarelo'], cor['normal'])))
n2 = float(input('{}Segunda nota do aluno:{} '.format(cor['amarelo'], cor['normal'])))
média = (n1 + n2) / 2
print('A média entre {}{:.1f}{} e {}{:.1f}{} é igual a {}{:.1f}{}'.format(cor['magenta'], n1,cor['normal'], cor['magenta'], n2, cor['normal'], cor['ciano'], média, cor['normal']))