###############################################################################
# Gobbler Development
###############################################################################
# This is the game under development.
# Instructions:
# 	Left, right, up or down to move the Gobbler.
#	Space-bar to rotate
#	Down to drop the piece
#	Fill all the blocks in a line to clear the line.
#	Clear multiple lines at once for more points!
###############################################################################

import pygame
from pygame.locals import *
import sys
import functions
import gobblersprite
import maze
#import ghostsprites
#from gamedata import GameData
import graphics
from sounds import *

pygame.mixer.pre_init(22050, -16, 2, 256)
pygame.init()
pygame.mixer.init()

# Setup for the screen.
screen_size = (640, 480)
screen = pygame.display.set_mode([screen_size[0], screen_size[1]])
pygame.display.set_caption("Gobbler")

# Game Setup
f = functions.GameFunctions()
g = graphics.Graphics()
gobbler = gobblersprite.GobblerSprite(g)
maze = maze.Maze(g)

#img_background = pygame.image.
#img_background_scaled = pygame.transform.scale(img_background, screen_size)

# Load sounds
#game_sounds = GameSounds()

# Load and play background music.
#pygame.mixer.music.load(GameData.MUSIC_BACKGROUND_FILENAME)
#pygame.mixer.music.play(-1)

# This is the main game loop.  Everything below here repeats forever.
fps = 60
while True:
	pygame.time.Clock().tick(fps)
	game_time = pygame.time.get_ticks()

	for event in pygame.event.get():
		# Pay attention if the user clicks the X to quit.
		if event.type == pygame.QUIT:
			sys.exit()

		# Check the keyboard for keypresses. (These buttons must be pressed repeatedly.)
		if event.type == pygame.KEYDOWN:
			if (event.key == K_ESCAPE):
				sys.exit()
			# if (event.key == K_LEFT):
			# 	this_piece.move_left(well_matrix)
			# if (event.key == K_RIGHT):
			# 	this_piece.move_right(well_matrix)
			# if (event.key == K_UP):
			# 	this_piece.move_left(well_matrix)
			# if (event.key == K_DOWN):
			# 	this_piece.move_right(well_matrix)

	# If DOWN is held, drop it faster
	keys = pygame.key.get_pressed()
	if (keys[K_UP]):
		gobbler.attempt_up(maze)
	if (keys[K_DOWN]):
		gobbler.attempt_down(maze)
	if (keys[K_LEFT]):
		gobbler.attempt_left(maze)
	if (keys[K_RIGHT]):
		gobbler.attempt_right(maze)
	# if (keys[K_DOWN]):
	# 	dropping_speed = int(hover_duration / 10 * 95)
	# else:
	# 	dropping_speed = 0

	# Draw the maze
	f.draw_maze(screen, screen_size)

	# Draw the pellets
	f.draw_pellets(screen, screen_size)

	# Move the Gobbler
	gobbler.move()
	gobbler.animate(game_time)

	# Draw the Gobbler
	gobbler.render(screen)
	#screen.blit(g.images[5], (0, 0))


	# Draw the ghosts

	# # Draw the score box
	# g.draw_scoreboard(screen, screen_size, score)

	# Put the scene on the monitor.
	pygame.display.update()

# End of game loop.
