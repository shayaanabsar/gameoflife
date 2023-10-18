from collections import defaultdict
from enum import Enum
from time import sleep
import os
from random import randint, choices

class State(Enum):
	ALIVE = 0
	DEAD  = 1

class ConwaysGameofLife:
	def __init__(self, alive_character='██', dimensions=(100,100)):
		self.map = defaultdict(lambda: State.DEAD)
		self.alive_character = alive_character
		self.y_dimension, self.x_dimension = dimensions
		self.generation = 0

	def generate_seed(self):
		for i in range(1000):
			for j in range(1000):
				c = choices([0, 1], weights=(1, 3), k=1)[0]
				self.map[(i, j)] = State.ALIVE if c == 0 else State.DEAD

	def next_generation(self):
		new_map = defaultdict(lambda: State.DEAD)

		for i in range(self.y_dimension):
			for j in range(self.x_dimension):
				neighbours = [
					self.map[(i, j+1)],
					self.map[(i, j-1)],
					self.map[(i+1, j)],
					self.map[(i-1, j)],
					self.map[(i-1, j-1)],
					self.map[(i-1, j+1)],
					self.map[(i+1, j-1)],
					self.map[(i+1, j+1)]
				]
				
				alive_neighbours = neighbours.count(State.ALIVE)
				curr_state = self.map[(i, j)]

				if curr_state == State.ALIVE and (alive_neighbours < 2):
					new_map[(i, j)] = State.DEAD
				elif curr_state == State.ALIVE and (alive_neighbours > 3):
					new_map[(i, j)] = State.DEAD
				elif curr_state == State.DEAD and (alive_neighbours == 3):
					new_map[(i, j)] = State.ALIVE
				else:
					new_map[(i, j)] = curr_state
		
		self.map = new_map


	def print(self):
		for i in range(self.y_dimension):
			for j in range(self.x_dimension):
				if self.map[(i, j)] == State.DEAD:
					print('  ', end='')
				else:
					print(f'\033[1;31m{self.alive_character}', end='')
			print('')

	def play(self):
		self.generate_seed()
		
		while True:
			self.print()
			sleep(0.01)
			self.next_generation()
			os.system('clear')
game = ConwaysGameofLife()
game.play()