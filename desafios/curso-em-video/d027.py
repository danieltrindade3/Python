num = int(input('\033[33mPor favor, digite um número qualquer:\033[m '))
res = num % 2
if res == 0:
    print('O número {} é \033[32mpar\033[m'.format(num))
else:
    print('O número {} é \033[32mímpar\033[m'.format(num))