preço = float(input('Qual é o preço do produto? R$'))
off = int(input('Quanto tem de desconto na loja? '))
promo = preço - (preço * off / 100)
print('O produto que custava R${}, na promoção com desconto de {}% vai custar R${}.'.format(preço, off, promo))