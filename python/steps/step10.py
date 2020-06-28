###############################################################################
# Gobbler Step 10 - Pellet Collisions
###############################################################################
# Gobbler runs through the maze, but he doesn't eat the pellets.  We will
# add collision detection so that we know when he has eaten a pellet.  When
# he collides with a pellet, the pellet should disappear.
###############################################################################

# PyGame stuff
import pygame
from pygame.locals import *
import sys
# Tile data
import tmxdata
import maze
import pellets
import gobblerpaths
import ghostpaths
# Game files
import graphics
import functions
from directions import *
from navigators import *
# Graphics files
import gobblersprite
import ghostsprite

# Sound and graphics init for PyGame
pygame.init()

# Set up the screen.
screen_size = (55*8, 61*8)
screen = pygame.display.set_mode([screen_size[0], screen_size[1]])
pygame.display.set_caption("Gobbler")

# System setup
g = graphics.Graphics()
f = functions.GameFunctions(g, None)

# Tilesets Setup
tmxdata = tmxdata.TmxData()
maze = maze.Maze(tmxdata)
pellets_template = pellets.Pellets(tmxdata)
pellets = pellets.Pellets(tmxdata)
pellets.reset(pellets_template)
ghost_paths = ghostpaths.GhostPaths(tmxdata)
gobbler_paths = gobblerpaths.GobblerPaths(tmxdata)

# Sprites Setup
gobbler = gobblersprite.GobblerSprite(g, GobblerNavigator(f, gobbler_paths))
ghost_yellow = ghostsprite.YellowGhostSprite(g, RandomNavigator(f, ghost_paths))
ghost_pink = ghostsprite.PinkGhostSprite(g, RandomNavigator(f, ghost_paths))
ghost_cyan = ghostsprite.CyanGhostSprite(g, RandomNavigator(f, ghost_paths))
ghost_red = ghostsprite.RedGhostSprite(g, RandomNavigator(f, ghost_paths))

# Lists setup
all_ghosts = [ghost_yellow, ghost_pink, ghost_cyan, ghost_red]
all_sprites = [gobbler, ghost_yellow, ghost_pink, ghost_cyan, ghost_red]

# Game Loop setup
fps = 60

# Reset all sprites to their starting positions in the maze
for sprite in all_sprites:
	sprite.reset()

# This is the main game loop.  Everything below here repeats forever.
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

	keys = pygame.key.get_pressed()
	if keys[K_UP]:
		gobbler.attempt_direction(maze, gobbler_paths, f, direction_up)
	if keys[K_DOWN]:
		gobbler.attempt_direction(maze, gobbler_paths, f, direction_down)
	if keys[K_LEFT]:
		gobbler.attempt_direction(maze, gobbler_paths, f, direction_left)
	if keys[K_RIGHT]:
		gobbler.attempt_direction(maze, gobbler_paths, f, direction_right)

	gobbler_rect = gobbler.get_center_rect()
	(p_x, p_y, _, _) = gobbler_rect
	if (f.pixel_is_tile_aligned(p_x, p_y)):
		tile_loc = f.tile_location_of_pixel(p_x, p_y)
		(t_x, t_y) = tile_loc

		# Look for a pellet here
		pellet = pellets.pellet_at(t_x, t_y)
		if (pellet != None):
			(x, y, gid, tiled_gid, _) = pellet
			# Is it a power pellet?
			if (gid != 0):
				is_power_pellet = (tiled_gid == 196)
				if (is_power_pellet):
					f.power_up(game_time, gobbler, all_ghosts)
				pellets.gobble(t_x, t_y)
	if f.power_up_expired(game_time):
		f.power_down(gobbler, all_ghosts)

	for sprite in all_sprites:
		sprite.navigator.navigate()

	# Draw the maze
	screen.fill(Color("White"))
	g.draw_maze(maze, screen)

	# Draw the pellets
	g.draw_pellets(pellets, screen)

	# Animate each sprite
	for sprite in all_sprites:
		sprite.animate(game_time)

	# Adjust the location of the sprite in the maze.
	for sprite in all_sprites:
		sprite.move(game_time)

	# Draw the Gobbler
	gobbler.render(screen)

	# Draw the ghosts
	for ghost in all_ghosts:
		ghost.render(screen)

	# Put the scene on the monitor.
	pygame.display.update()

# End of game loop.
