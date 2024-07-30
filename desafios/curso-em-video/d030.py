n1 = int(input('\033[33mPrimeiro valor:\033[m '))
n2 = int(input('\033[34mSegundo valor:\033[m '))
n3 = int(input('\033[35mTerceiro valor:\033[m '))
# Verificando o maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
# Verificando o menor valor
menor = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
# Resultado
print('O maior valor digitado foi \033[1;32m{}\033[m'.format(maior))
print('O menor valor digitado foi \033[1;31m{}\033[m'.format(menor))