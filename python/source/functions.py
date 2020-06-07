import pygame
from pygame.locals import Color, Rect
import random
from directions import *
from graphics import *
import sounds
from gamedata import GameData

random.seed()

class GameFunctions:
	"""Contains root-level game behaviors.
	Think of these functions as the glue between sprites, maps, graphics
	and the game loop."""
	def __init__(self, graphics, sounds):
		self.graphics = graphics
		self.sounds = sounds
		self.game_over = False
		self.you_win = False
		self.power_up_until = 0
		self.powered_up = False

	def tile_width(self):
		return 8

	def tile_height(self):
		return 8

	def pixel_location_of_tile(self, tile_x, tile_y):
		return (tile_x * 8, tile_y * 8)

	def pixel_is_tile_aligned(self, pixel_x, pixel_y):
		return (pixel_x % 8 == 0) and (pixel_y % 8 == 0)

	def player_is_tile_aligned(self, player):
		(x, y) = player.get_center_tile_position()
		return self.pixel_is_tile_aligned(x, y)

	def tile_location_of_pixel(self, pixel_x, pixel_y):
		return (int(pixel_x // 8), int(pixel_y // 8))

	# Should only be called when player is tile-aligned.
	def player_cango(self, player, player_paths, direction):
		(x_direction, y_direction) = direction.velocity
		(pixel_x, pixel_y) = player.get_center_tile_position()
		tile_aligned = self.pixel_is_tile_aligned(pixel_x, pixel_y)
		if not tile_aligned:
			print("Not tile-aligned!", player)
			raise Exception("Player is not tile-aligned!")	#This will end the program

		(tile_location_x, tile_location_y) = self.tile_location_of_pixel(pixel_x, pixel_y)
		target_tile_x = tile_location_x + x_direction
		target_tile_y = tile_location_y + y_direction
		if (target_tile_x <= 0) or (target_tile_y <= 0) or (target_tile_x > player_paths.xtilecount - 1) or (target_tile_y > player_paths.ytilecount):
			return False
		target_tile = player_paths.tile_grid[target_tile_x][target_tile_y]
		return (target_tile != None) and (target_tile[3] != 0)

	def power_up(self, game_time, gobbler, yellow, pink, cyan, red):
		print("power up!")
		# Ghosts transform from hunters to prey
		yellow.run_away()
		pink.run_away()
		cyan.run_away()
		red.run_away()

		# Background music changes casual to urgent
		self.sounds.play_music_urgent()
		self.sounds.sound_crunch.play()
		self.powered_up = True

		# Start a countdown timer
		self.power_up_until = game_time + 1000 * GameData.GOBBLER_POWERUP_DURATION_SECONDS
		print(game_time)
		print(self.power_up_until)

	def power_up_expired(self, game_time):
		return game_time > self.power_up_until

	def power_down(self, gobbler, yellow, pink, cyan, red):
		if (self.powered_up):
			self.sounds.play_music_casual()
			yellow.hunt()
			pink.hunt()
			cyan.hunt()
			red.hunt()
			self.powered_up = False

	def check_ghost_collision(self, gobbler, ghost):
		ghost_rect = ghost.get_center_rect()
		gobbler_rect = gobbler.get_center_rect()
		has_collision = ghost_rect.colliderect(gobbler_rect)
		if has_collision:
			if ghost.is_scared:
				self.chomp(ghost)
			else:
				self.haunt(ghost, gobbler)
			return True
		return False

	def chomp(self, ghost):
		ghost.reset_frame()
		self.sounds.sound_chomp.play()
		ghost.reset()
		ghost.hunt()

	def haunt(self, ghost, gobbler):
		self.defeat()

	def victory(self):
		print("Victory!")
		self.game_over = True
		self.you_win = True
		self.sounds.stop_music()

	def defeat(self):
		print("Defeat.")
		self.game_over = True
		self.you_win = False
		self.sounds.stop_music()
		self.sounds.sound_death.play()

