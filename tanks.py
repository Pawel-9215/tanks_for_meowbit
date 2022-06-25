from meowbit import *
import random

class AssetLoader():
	def __init__(self):
		self.assets = {}
		self.palette = []
		
	def load_palette(self, directory):
		with open(directory) as pal_file:
			self.palette = eval(pal_file.read())
		
	def load_asset(self, directory, name):
		self.assets[name] = []
		with open(directory) as asset_file:
			for x, line in enumerate(asset_file.readlines()):
				self.assets[name].append([])
				for y, letter in enumerate(line):
					self.assets[name][x].append(letter)
		

class Node2d():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def position(self):
		return (self.x, self.y)
		
		
class RasImage(Node2d):
	def __init__(self, x, y, image, palette):
		super().__init__(x, y)
		self.palette = palette
		self.image = image
		
	def render(self):
		for x, row in enumerate(self.image):
			for y, column in enumerate(row):
				if column in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]:
					print(column)
					screen.pixel(self.x+x, self.y+y, self.palette[column])
		
	def rotate(self, direction):
		pass

class Renderer():
	def __init__(self):
		self.renderables_l1 = []
		self.renderables_l2 = []
		self.renderables_l3 = []
		
		self.bg_color = (79, 76, 72)
		self.grass_amount = 128
		
	def render_bg(self):
		screen.fill(self.bg_color)
		
	def include(self, sprite, layer):
		if layer == 1:
			self.renderables_l1.append(sprite)
		elif layer == 2:
			self.renderables_l2.append(sprite)
		elif layer == 3:
			self.renderables_l3.append(sprite)
		else:
			raise ValueError
		
	def render_grass(self):
		
		for i in range(self.grass_amount):
			x = random.randint(0, 159)
			y = random.randint(0, 127)
			screen.pixel(x, y, (99, 96, 92))
				
	def render(self):
		self.render_bg()
		self. render_grass()
		
		for obj in self.renderables_l3:
			obj.render()
			
		for obj in self.renderables_l2:
			obj.render()
			
		for obj in self.renderables_l1:
			obj.render()
			
		screen.refresh()
		
class Updater():
	def __init__(self):
		self.updatables = []
		
	def update(self):
		for obj in self.updatables:
			obj.update()
			
class Cell(Node2d):
	def __init__(self, wx, wy):
		self.wx = wx
		self.wy = wy
		super().__init__(wx*16, wy*16)
		
		self.content = []
		
		
	def populate(self, cargo):
		self.content.append(cargo)
		
	def empty_cell(self):
		self.content.clear()
		
class Grid():
	def __init__():
		self.cells = []
		
	def populate_grid(self):
		for x in range(10):
			self.cells.append([])
			for y in range(8):
				self.cells[x].append(Cell(x,y))
			
class Tank(Node2d):
	def __init__(self, x, y, img, pal, renderer, updater, direction):
		super().__init__(x, y)
		self.sprite = RasImage(self.x, self.y, img, pal)
		self.direction = direction
		
		renderer.include(self.sprite, 3)
		updater.udpatables.append(self)
		
		self.can_move = true
		
	def move(self, direction):
		pass
		
		
	def update(self):
		pass
		
			
				
			
			
