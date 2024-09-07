from random import choice
cor = {
    'normal':'\033[m',
    'amarelo':'\033[33m',
    'magenta':'\033[35m'
}
pri = str(input('{}Primeiro aluno:{} '.format(cor['amarelo'], cor['normal'])))
seg = str(input('{}Segundo aluno:{} '.format(cor['amarelo'], cor['normal'])))
ter = str(input('{}Terceiro aluno:{} '.format(cor['amarelo'], cor['normal'])))
qua = str(input('{}Quarto aluno:{} '.format(cor['amarelo'], cor['normal'])))
alunos = [pri, seg, ter, qua]
escolhido = choice(alunos)
print('O aluno escolhido foi {}{}.{}'.format(cor['magenta'], escolhido, cor['normal']))