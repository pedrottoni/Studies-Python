# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''!!!NÃO DEU CERTO ESSE!!!

import pygame

pygame.init()
pygame.mixer.music.load("edithPiafNonJeneregretterien.mp3")
pygame.mixer.music.play()
pygame.event.wait()

!!!NÃO DEU CERTO ESSE!!! '''

from playsound import playsound

playsound('edithPiafNonJeneregretterien.mp3')
