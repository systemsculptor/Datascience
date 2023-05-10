import os
import math
import time
import random

#globals
board_x = 10
board_y = 10
game_running = True
player_block = "#"
goal_block = "^" #Goal
black_block = "░"  #wall
white_block = "█"  # Areas to move around
game_board = []

def place_random_walls(count): #recursive
	"""places random walls in the board exluding 0,0"""
	if count <= 0:
		return
	game_board[random.randrange(1,board_x)][random.randrange(1,board_y)] = 1
	place_random_walls(count - 1)

def build_game_board():
	for x in range(board_x):
		game_board.append([])
		for y in range(board_y):
			game_board[x].append(0)
	game_board[0][0] = "#"
	
	
build_game_board()
place_random_walls(4)
game_board[board_x-1][board_y-1] = 2

def out_of_bounds(x : int, y : int):
	if x > len(game_board)-1:
		return True
	if x < 0:
		return True
	if y > len(game_board[x])-1:
		return True
	if y < 0:
		return True
	return False

def valid_step(x : int, y : int):
	if out_of_bounds(x,y):
		return False
	elif game_board[x][y] == 1:
		return False
	elif game_board[x][y] == 0:
		return True
	if game_board[x][y] == 2:
		print("You Won")
		#stop this when it wins so counting is accurate
		return True
	else: 
		return False
	


def get_player_position() -> list:
	"""Returns a list [x, y] of the players position on the board"""
	player_position = [0,0]

	for i in range(len(game_board)):
		if '#' in game_board[i]:
			player_position[0] = i
			player_position[1] = game_board[i].index('#')
			break
		
	return player_position

def draw(value):
	if value == 0:
		print(white_block, end = '')
	elif value == 1:
		print(black_block, end = '')
	elif value == '#':
		print(player_block, end = '')
	elif value == 2:
		print(goal_block, end = '')
	else:
		print('?', end = '')

def update(value, x, y): #logic step
	pass

def move_player(x : int, y : int):
	if (x < -1 or x > 1) or (y < -1 or y > 1):
		raise ValueError("Expected normalized vector eg. (-1,-1) to (1,1)")

	player_position = get_player_position()

	if valid_step(player_position[0] + x, player_position[1] + y):
		game_board[player_position[0]][player_position[1]] = 0
		game_board[player_position[0] + x][player_position[1] + y] = '#'

def qTable():
	for i in range(0, 100):
		player_position = get_player_position()
		count = 0
		count = count + 1 
		tempCount = 0
		count = tempCount
		while(count > tempCount):
			print("Test")
	for i in range(0, count):
		qTable = []
		if(count > tempCount):
			qTable.append(player_position()) 
	for each in range(0, count):
		print(qTable)
						
#def findOptimalPath():
#	for i in range(0, count):



while(game_running):

	os.system('cls')
	for x in range(board_x):
		for y in range(board_y):
			update(game_board[x][y], x, y)
			draw(game_board[y][x])
			print(' ', end = '')
			qTable()
		print()
	time.sleep(1)


