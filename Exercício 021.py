'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''
# Aqui vemos sobre  'pygame'

import pygame
pygame.init() #iniciando o pygame
pygame.mixer.music.load('testeex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()