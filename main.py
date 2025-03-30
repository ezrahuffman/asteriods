import pygame

from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid

def main():
	pygame.init()

	clock = pygame.time.Clock()
	dt = 0

	updatable_group = pygame.sprite.Group()
	drawable_group = pygame.sprite.Group()
	asteroids_group = pygame.sprite.Group()
	Player.containers = (updatable_group, drawable_group)
	Asteroid.containers = (updatable_group, drawable_group, asteroids_group)
	AsteroidField.containers = (updatable_group)

	asteroid_field = AsteroidField()
	player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		# Render
		screen.fill((0, 0, 0))

		updatable_group.update(dt)
		for drawable in drawable_group:
			drawable.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
