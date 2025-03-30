import pygame

import shot
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
	pygame.init()

	clock = pygame.time.Clock()
	dt = 0

	updatable_group = pygame.sprite.Group()
	drawable_group = pygame.sprite.Group()
	asteroids_group = pygame.sprite.Group()
	shots_group = pygame.sprite.Group()
	Player.containers = (updatable_group, drawable_group)
	Asteroid.containers = (updatable_group, drawable_group, asteroids_group)
	Shot.containers = (updatable_group, drawable_group, shots_group)
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

		for asteroid in asteroids_group:
			if asteroid.is_colliding(player):
				print("Game Over!")
				raise SystemExit
			for s in shots_group:
				if s.is_colliding(asteroid):
					s.kill()
					asteroid.split()
					break

		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
