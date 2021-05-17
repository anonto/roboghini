sudo pip3 install pygame
------------------------------------------

import pygame

def init():
	pygame.init()
	win = pygame.display.set_mode((100,100))

def getKey(KeyName):
	ans = False
	for eve in pygame.event.get():pass
	keyInput = pygame.key.get_pressed()
	myKey = getattr(pygame,'K_{}'.format(keyName))
	if keyinput [myKey]:
		ans = True
	pygame.display.update()

	return ans

def main():
	if get key('LEFT'):
		print('Key Left was pressed')
	if get key('LEFT'):
		print('Key Right was pressed')

if __name__ == '__main__'
	init()
	while True:
		main()
