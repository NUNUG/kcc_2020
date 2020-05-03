import pygame
from pygame.locals import Color, Rect
import random
from graphics import *

random.seed()

class GameFunctions:
	def __init__(self):
		pass
	def draw_pellets(self, screen, screen_size):
		pass

	def draw_maze(self, screen, screen_size):
		pass

	# def draw_gobbler(self, screen, gobbler):
	# 	screen.blit(gobbler.image, gobbler.position)

	# def draw_well_grid(self, screen, screen_size):
	# 	"""This draws a happy little dot in the well at the center of each cell."""
	# 	wellx, welly = self.well_pixel_coords(screen_size)
	# 	cell_width, cell_height = self.cell_size_in_pixels()
	# 	cols, rows = self.well_dimensions()
	# 	for col in range(cols):
	# 		for row in range(rows):
	# 			dot_pos = (wellx + col * cell_width + int(cell_width / 2), welly + row * cell_height + int(cell_height / 2))
	# 			pygame.draw.circle(screen, Color(128, 128, 128, 255), dot_pos, 3)

	# def draw_well_matrix(self, screen, screen_size, well_matrix):
	# 	"""This draws the existing set pieces in the well.  It draws a set brick for each cell
	# 	in the well matrix which contains a 1."""
	# 	wellx, welly = self.well_pixel_coords(screen_size)
	# 	cell_width, cell_height = self.cell_size_in_pixels()
	# 	cols, rows = self.well_dimensions()
	# 	for row in range(rows):
	# 		for col in range(cols):
	# 			cell = well_matrix[row][col]
	# 			if (cell >= 1):
	# 				brick_pos = (wellx + col * cell_width, welly + row * cell_height)
	# 				screen.blit(img_well_brick, brick_pos)

	# def draw_piece_matrix(self, screen, screen_size, piece):
	# 	"""This draws the current piece on the screen.  It draws a brick for each cell
	# 	in the piece matrix which contains a 1."""
	# 	posx, posy = piece.position
	# 	for row in range(4):
	# 		for col in range(4):
	# 			cellx, celly = self.cell_position_to_pixels(screen_size, (posx, posy))
	# 			if (GameData.SHOW_MATRIX_SHADOW):
	# 				pygame.draw.line(screen, Color(255, 0, 0, 255), (col * 16 + cellx, row * 16 + celly), ((col+1) * 16 + cellx, (row + 1) * 16 + celly))
	# 			if (posy + row >= 0):
	# 				if (piece.matrix[row][col] == 1):
	# 					screen.blit(img_piece_brick, (col * 16 + cellx, row * 16 + celly))

	# def pause_for(self, milliseconds):
	# 	"""Pauses execution for the given time period.  Used for animation sequences and banners."""
	# 	start_ticks = pygame.time.get_ticks()
	# 	while True:
	# 		pygame.time.Clock().tick(1000/30)
	# 		if (pygame.time.get_ticks() > start_ticks + milliseconds):
	# 			break

	# def draw_clearings(self, screen, screen_size, well_matrix, crunch_sound):
	# 	"""Draws crunched bricks in each line to be cleared and plays a crunching sound once for each row."""
	# 	wellx, welly = self.well_pixel_coords(screen_size)
	# 	cell_width, cell_height = self.cell_size_in_pixels()
	# 	lines = self.get_lines_to_clear(well_matrix)
	# 	line_count = len(lines)
	# 	ww, wh = self.well_dimensions()
	# 	for line_num in range(line_count):
	# 		for col in range(ww):
	# 			brick_pos = (wellx + col * cell_width, welly + lines[line_num] * cell_height)
	# 			screen.blit(img_crunch_brick, brick_pos)
	# 		pygame.display.update()
	# 		crunch_sound.play()
	# 		self.pause_for(500)

	# def draw_well(self, screen, screen_size):
	# 	border_size = 5
	# 	borderx, bordery = self.well_pixel_coords(screen_size)
	# 	borderx = borderx - border_size
	# 	bordery = bordery - border_size
	# 	borderw, borderh = self.well_size_in_pixels()
	# 	borderw = borderw + (2 * border_size)
	# 	borderh = borderh + (2 * border_size)
	# 	pygame.draw.rect(screen, Color(255, 255, 255, 255), Rect(borderx, bordery, borderw, borderh))

	# 	wellx, welly = self.well_pixel_coords(screen_size)
	# 	wellw, wellh = self.well_size_in_pixels()
	# 	pygame.draw.rect(screen, Color(0, 0, 0, 255), Rect(wellx, welly, wellw, wellh))

	# def draw_scoreboard(self, screen, screen_size, score):
	# 	"""Draws a box with the score in it onto the screen."""
	# 	screenw, screenh = screen_size
	# 	wellx, welly = self.well_pixel_coords(screen_size)
	# 	wellw, wellh = self.well_size()
	# 	border_size = 5
	# 	padding = 20
	# 	height = 50

	# 	left = wellx + wellw + padding
	# 	right = screenw - padding
	# 	top = welly
	# 	#bottom = top + height
	# 	width = right - left + 1

	# 	pygame.draw.rect(screen, Color(255, 255, 255, 255), Rect(left - border_size, top - border_size, width + border_size * 2, height + border_size * 2))
	# 	pygame.draw.rect(screen, Color(0, 0, 0, 255), Rect(left, top, width, height))

	# 	text = str(score)
	# 	font = pygame.font.SysFont("Lucida Console", 32, 1, 0)
	# 	text_surface = font.render(text, False, Color(255, 255, 255, 255))
	# 	screen.blit(text_surface, (left + (width - text_surface.get_width()) / 2, top + (height - text_surface.get_height()) / 2))

