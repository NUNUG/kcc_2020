import pygame
from gamedata import *
from spritesheets import SpriteSheet

# Load images from disk
#img_background = pygame.image.load(GameData.IMAGE_BACKGROUND_FILENAME)
#img_well_brick = pygame.image.load(GameData.IMAGE_WELL_BRICK_FILENAME)
#img_crunch_brick = pygame.image.load(GameData.IMAGE_CRUNCH_BRICK_FILENAME)
#img_piece_brick = pygame.image.load(GameData.IMAGE_PIECE_BRICK_FILENAME)


class Graphics:
	def __init__(self):
		ss_gobbler = SpriteSheet(GameData.IMAGE_GOBBLER_SPRITESHEET_FILENAME)
		img_gobblers = ss_gobbler.load_horizontal_sheet(GameData.GOBBLER_IMAGE_SIZE[0])
		#self.images = img_gobblers

		gsize = GameData.GOBBLER_SPRITE_SIZE
		self.img_gobbler_left = [pygame.transform.smoothscale(img_gobblers[0], gsize), pygame.transform.smoothscale(img_gobblers[1], gsize)]
		self.img_gobbler_right = [pygame.transform.smoothscale(img_gobblers[2], gsize), pygame.transform.smoothscale(img_gobblers[3], gsize)]
		self.img_gobbler_down = [pygame.transform.smoothscale(img_gobblers[4], gsize), pygame.transform.smoothscale(img_gobblers[5], gsize)]
		self.img_gobbler_up = [pygame.transform.smoothscale(img_gobblers[6], gsize), pygame.transform.smoothscale(img_gobblers[7], gsize)]


		# self.img_gobbler_left = [img_gobblers[0], img_gobblers[1]]
		# self.img_gobbler_right = [img_gobblers[2], img_gobblers[3]]
		# self.img_gobbler_down = [img_gobblers[4], img_gobblers[5]]
		# self.img_gobbler_up = [img_gobblers[6], img_gobblers[7]]

		ss_ghosts = SpriteSheet(GameData.IMAGE_GHOSTS_SPRITESHEET_FILENAME)
		img_ghosts = ss_ghosts.load_horizontal_sheet(GameData.GHOST_IMAGE_SIZE[0])
		self.img_ghost_yellow = img_ghosts[0]
		self.img_ghost_pink = img_ghosts[1]
		self.img_ghost_cyan = img_ghosts[2]
		self.img_ghost_red = img_ghosts[3]
