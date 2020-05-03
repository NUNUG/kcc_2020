import pygame
import mazesprite
import graphics
import gamedata

class GobblerSprite(mazesprite.MazeSprite):
	def __init__(self, graphics):
		mazesprite.MazeSprite.__init__(self, graphics)
		self.direction = (1, 1)

	def animation_delay_ms(self):
		return gamedata.GameData.GOBBLER_ANIMATION_DELAY
		#return 0

	# This overrides the load_frames() method in the mazesprite class, which GobblerSprite inherits.
	def load_frames(self, graphics):
		self.up_frames = graphics.img_gobbler_up
		self.down_frames = graphics.img_gobbler_down
		self.left_frames = graphics.img_gobbler_left
		self.right_frames = graphics.img_gobbler_right
		self.frames = self.left_frames

	# This overrides the get_speed() method in the mazesprite class, which GobblerSprite inherits.
	def get_speed(self):
		return gamedata.GameData.GOBBLER_SPEED

