# -*- coding: utf-8 -*-
import pgzrun


GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
MAP = [ "WWWWWWWWWWWWWWWW",
		"W              W",
		"W              W",
		"W  W  KG       W",
		"W  WWWWWWWWWW  W",
		"W              W",
		"W      P       W",
		"W  WWWWWWWWWW  W",
		"W     GK    W  W",
		"W              W",
		"W              D",
		"WWWWWWWWWWWWWWWW"]

def screen_coords(x, y):
	return (x * GRID_SIZE, y * GRID_SIZE)

def grid_coords(actor):
	return round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE)

def setup_game():
	global game_over, player, keys_to_collect
	game_over = False
	player = Actor("player", anchor=("left", "top"))
	keys_to_collect = []


	for y in range(GRID_HEIGHT):
		for x in range(GRID_WIDTH):
			square = MAP[y][x]
			if square == "P":
				player.pos = screen_coords(x, y)
			elif square == "K":
				key = Actor("key", anchor=("left", "top"), pos = screen_coords(x, y))
				keys_to_collect.append(key)




def draw_background():
	for y in range(GRID_HEIGHT):
		for x in range(GRID_WIDTH):
			screen.blit("floor1", screen_coords(x, y))



def draw_scenery():
	for y in range(GRID_HEIGHT):
		for x in range(GRID_WIDTH):
			square = MAP[y][x]
			if square == "W":
				screen.blit("wall", screen_coords(x, y))
			elif square == "D":
				screen.blit("door", screen_coords(x, y))

def dray_actors():
	player.draw()
	for key in keys_to_collect:
		key.draw()

def draw():
	draw_background() #壁紙描画
	draw_scenery()	  #背景描画
	dray_actors()	  #プレイヤーキャラ描画


# キーボードのイベントハンドラ
def on_key_down(key):
	if key == keys.LEFT:
		move_player(-1, 0)
	elif key == keys.UP:
		move_player(0, -1)
	elif key == keys.RIGHT:
		move_player(1, 0)
	elif key == keys.DOWN:
		move_player(0, 1)


def move_player(dx, dy):
	(x, y) = grid_coords(player)
	x += dx
	y += dy
	square = MAP[y][x]
	if square == "W":
		return
	elif square == "D":
		if len (keys_to_collect) > 0:
			return
	for key in keys_to_collect:
		(key_x, key_y) = grid_coords(key)
		if x == key_x and y == key_y:
			keys_to_collect.remove(key)
			break
	player.pos = screen_coords(x, y)


setup_game()
pgzrun.go()



