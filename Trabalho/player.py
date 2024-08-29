import os

import pygame

import sys

pygame.mixer.init()

class Player:

    def __init__(self, musica_objeto):
        
        self.musica_objeto = musica_objeto
        
    def start(self):

        exe_dir = getattr(sys, '_MEIPASS', os.getcwd())
        
        file_path = os.path.join(exe_dir, self.musica_objeto.file)

        pygame.mixer.music.load(file_path)
        
        pygame.mixer.music.play()

    def pausar(self):
        
        pygame.mixer.music.pause()

    def despausar(self):
        
        pygame.mixer.music.unpause()

    def parar(self):
        
        pygame.mixer.music.stop()
