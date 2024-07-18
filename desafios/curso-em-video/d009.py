lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = lar * alt
litro = área / 2
print('Sua parede tem a dmensão {}X{} e sua área é de {}m².'.format(lar, alt, área))
print('Para pintar a parede, você precisa de {}l de tinta.'.format(litro))