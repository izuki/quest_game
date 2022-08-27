import pyxel
 

GRID_W = 16
GRID_H = 12
GRID_SIZE = 50
WIDTH = GRID_W * GRID_SIZE
HEIGHT = GRID_W * GRID_SIZE


pyxel.init(256, 256)

 
def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
 
def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)
 
pyxel.run(update, draw)