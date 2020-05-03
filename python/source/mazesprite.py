import pygame

class MazeSprite(pygame.sprite.Sprite):
	def __init__(self, graphics):
		self.frames = []
		self.up_frames = []
		self.down_frames = []
		self.left_frames = []
		self.right_frames = []
		self.load_frames(graphics)
		self.frame_index = 0
		self.direction = (0, 0)
		self.position = (0, 0)
		self.image = self.frames[self.frame_index]
		self.last_animation_change = 0
		self.speed = self.get_speed()

	# Override this in descendent classes.
	# Each sprite knows how to load its own images.
	def load_frames(self, graphics):
		pass

	# Override this in descendent classes.
	def get_speed(self):
		return 1.0

	def animation_delay_ms(self):
		return 30

	def animate(self, game_time):
		if (game_time > self.last_animation_change + self.animation_delay_ms()):
			self.last_animation_change = game_time
			self.advance_frame()
			# frame_count = len(self.frames)
			# self.frame_index = (self.frame_index + 1) % frame_count
			# self.image = self.frames[self.frame_index]

	def reset_frame(self):
		self.frame_index = 0
		self.image = self.frames[self.frame_index]

	def advance_frame(self):
		frame_count = len(self.frames)
		self.frame_index = (self.frame_index + 1) % frame_count
		self.image = self.frames[self.frame_index]

	def move(self):
		(x, y) = self.position
		(v, h) = self.direction
		(newx, newy) = (x + v, y + h)
		if (newx < 0):
			newx = 0
		if (newy < 0):
			newy = 0
		if (newx > 600):
			newx = 600
		if (newy > 400):
			newy = 400
		self.position = (newx, newy)

	def attempt_up(self, maze):
		self.set_direction_up()
	def attempt_down(self, maze):
		self.set_direction_down()
	def attempt_left(self, maze):
		self.set_direction_left()
	def attempt_right(self, maze):
		self.set_direction_right()

	def set_direction_up(self):
		self.direction = (0, -1 * self.speed)
		if (self.frames != self.up_frames):
			self.frames = self.up_frames
			self.reset_frame()
	def set_direction_down(self):
		self.direction = (0, 1 * self.speed)
		if (self.frames != self.down_frames):
			self.frames = self.down_frames
			self.reset_frame()
	def set_direction_left(self):
		self.direction = (-1 * self.speed, 0)
		if (self.frames != self.left_frames):
			self.frames = self.left_frames
			self.reset_frame()
	def set_direction_right(self):
		self.direction = (1 * self.speed, 0)
		if (self.frames != self.right_frames):
			self.frames = self.right_frames
			self.reset_frame()
	def render(self, screen):
		# (left, top) = self.position
		# w = self.image.get_width()
		# h = self.image.get_height()

		# rect_surface = pygame.Surface((w, h))

		# rect_img = pygame.draw.rect(rect_surface, (255, 255, 255), (left, top, w, h))
		# screen.blit(rect_img, rect_surface)
		screen.blit(self.image, self.position)

