# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, width, height).

# Additional notes
# - Further adaptations from https://www.pygame.org/wiki/Spritesheet
# - Cleaned up overall formatting.
# - Updated from Python 2 -> Python 3.

import pygame


class SpriteSheet:

	def __init__(self, filename):
		"""Load the sheet."""
		try:
			self.sheet = pygame.image.load(filename).convert()
		except pygame.error as e:
			print(f"Unable to load spritesheet image: {filename}")
			raise SystemExit(e)


	def image_at(self, rectangle, colorkey = None):
		"""Load a specific image from a specific rectangle."""
		# Loads image from x, y, x+offset, y+offset.
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert()
		image.blit(self.sheet, (0, 0), rect)
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, pygame.RLEACCEL)
		return image

	def images_at(self, rects, colorkey = None):
		"""Load a whole bunch of images and return them as a list."""
		return [self.image_at(rect, colorkey) for rect in rects]

	def load_horizontal_sheet(self, image_width, colorkey = None):
		"""Load a horizontal strip of uniform sprites from a single-row spritesheet."""
		width = image_width
		image_count = self.sheet.get_width() // image_width
		height = self.sheet.get_height()
		result = []
		for i in range(0, image_count):
			left = i * width
			top = 0
			#bottom = height - 1
			#right = (i + 1) * width - 1
			#rect = (left, top, right, bottom)
			rect = (left, top, width, height)
			img = self.image_at(rect, colorkey)
			result.append(img)
		return result


	def load_strip(self, rect, image_count, colorkey = None):
		"""Load a whole strip of images, and return them as a list."""
		tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
				for x in range(image_count)]
		return self.images_at(tups, colorkey)
