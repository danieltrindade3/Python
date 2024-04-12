real = float(input('Quanto você tem na carteira? R$'))
dolar = real / 5.09
euro = real / 5.43
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar EUR €{:.2f}'.format(real, euro))