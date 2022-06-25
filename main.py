from meowbit import *
from tanks import *
import math


screen.sync = 0
assets = AssetLoader()

assets.load_palette("./resources/palette.txt")
assets.load_asset("./resources/wall1.txt", "wall")
assets.load_asset("./resources/tank.txt", "tank")

renderer = Renderer()
updater = Updater()

my_image = RasImage(0, 0, assets.assets["wall"], assets.palette)
renderer.renderables_l1.append(my_image)

my_tank = RasImage(16, 0, assets.assets["tank"], assets.palette)
renderer.renderables_l1.append(my_tank)

while 1:
	updater.update()
	renderer.render()
