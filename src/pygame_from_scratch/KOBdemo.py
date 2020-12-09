import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
square = pygame.Surface((40, 40))
square.fill((0, 255, 0))
while True:
	screen.blit(square, (200, 200))
	if pygame.event.get(pygame.QUIT):
		break
	pygame.display.update()

pygame.quit()

