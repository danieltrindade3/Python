from random import choice
pri = str(input('Primeiro aluno: '))
seg = str(input('Segundo aluno: '))
ter = str(input('Terceiro aluno: '))
qua = str(input('Quarto aluno: '))
alunos = [pri, seg, ter, qua]
escolhido = choice(alunos)
print('O aluno escolhido foi {}.'.format(escolhido))