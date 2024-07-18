frase = str(input('Digite uma frase: ')).upper().strip()
print('Nesta frase a letra "a" aparece {} vez(es)'.format(frase.count('A')))
print('A primeira letra "a" aparece na posição {}'.format(frase.find('A') + 1))
print('A última letra "a" aparece na posição {}'.format(frase.rfind('A') + 1))