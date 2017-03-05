''' window.py '''
import pygame

class window():
	def __init__(self, screen):
		self.screen = screen

	def InitializeWindow(self):
		(widgth, height) = (1200, 700)
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption('Pocket Cities')
		pygame.display.flip
