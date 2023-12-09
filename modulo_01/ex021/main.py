# cria ambiente virtual: python -m venv venv
# ativa ambiente virtual: source venv/bin/activate
# instala pygame: pip install pygame 
import pygame


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('./caramelo.mp3')
pygame.mixer.music.play(60)
pygame.event.wait()