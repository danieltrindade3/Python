import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('desafios/curso-em-video/d018.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('\033[35mTocando...')
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
# pygame.time.Clock().tick('10')
print('\033[34mTocado!\033[m')