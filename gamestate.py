
import pygame
from random import randint

from direction import Direction
from snake import Snake
from food import Food
from colors import Color

WIDTH = 400
HEIGHT = 300

# size of blocks
BLOCK_S = 10
BLOCK_W = WIDTH / BLOCK_S
BLOCK_H = HEIGHT / BLOCK_S

pygame.init()
clock = pygame.time.Clock()
draw = pygame.draw
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

class GameState:
	def __init__(self):
		self.score = 0
		self.player = Snake(BLOCK_W/2, BLOCK_W/2)
		self.player.grow(5)
		self.food = Food(randint(0, BLOCK_W-1), randint(0, BLOCK_H-1))

	def frame_step(self, input_actions):
		# Check if window is closed
		if pygame.QUIT in [event.type for event in pygame.event.get()]:
			pygame.quit()
			exit()

		reward = 0.0
		terminal = False
		lastScore = self.score

		if sum(input_actions) != 1:
			raise ValueError('Multiple Input Actions!')

		# input_actions[0] == 1: do nothing
		# input_actions[1] == 1: change direction NORTH
		# input_actions[2] == 1: change direction EAST
		# input_actions[3] == 1: change direction SOUTH
		# input_actions[4] == 1: change direction WEST
		if input_actions[1]:
			self.player.changeDirection(Direction.NORTH)
		elif input_actions[2]:
			self.player.changeDirection(Direction.EAST)
		elif input_actions[3]:
			self.player.changeDirection(Direction.SOUTH)
		elif input_actions[4]:
			self.player.changeDirection(Direction.WEST)

		if self.player.hasEaten(self.food):
			self.score += 1
			reward = 1

			# move food
			self.food.x = randint(0, BLOCK_W-1)
			self.food.y = randint(0, BLOCK_H-1)

		self.player.move()
		# Check if the snake has moved off screen
		if self.player.x < 0:
		    self.player.x = BLOCK_W
		elif self.player.x >= BLOCK_W:
		    self.player.x = 0
		if self.player.y < 0:
		    self.player.y = BLOCK_H
		elif self.player.y >= BLOCK_H:
		    self.player.y = 0

		# Check if snake crashed into tail
		for i in range(1, len(self.player.tail)):
		    if self.player.x == self.player.tail[i].x and self.player.y == self.player.tail[i].y:
		        print("Game over: tail")
		        lastScore = self.score
		        self.__init__()
		        terminal = True
		        reward = -1
		        break

		# Draw background
		screen.fill(Color.WHITE)
		# Draw snake
		self.player.draw(draw, screen, Color.RED, (BLOCK_S, BLOCK_S, BLOCK_S, BLOCK_S))
		# Draw food
		self.food.draw(draw, screen, Color.BLUE, (BLOCK_S, BLOCK_S, BLOCK_S, BLOCK_S))

		image_data = pygame.surfarray.array3d(pygame.display.get_surface())
		pygame.display.update()
		clock.tick(60)

		return image_data, reward, terminal, lastScore
