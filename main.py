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



while 1:
	updater.update()
	renderer.render()
