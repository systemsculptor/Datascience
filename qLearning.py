import os
import math
import time
import random

#globals
board_x = 5
board_y = 5
game_running = True
player_block = "#"
goal_block = "^" #Goal
black_block = "░"  #wall
white_block = "█"  # Areas to move around
game_board = []

def place_random_walls(count): #recursive
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
	elif game_board[x][y] == 2:
		return True
	else: 
		return False

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


while (game_running):
	time.sleep(0.17)
	os.system('cls')
	for x in range(board_x):
		for y in range(board_y):
			update(game_board[x][y], x, y)
			draw(game_board[y][x])
			print(' ', end = '')
		print()
		
def playerMove():
	# # # 
    # # # 
    # # ^
	
def qMaximation(alpha, gamma): 
	for i in range(1, board_x):
		for j in range(1, board_y):
			currentIterated = currentIterated + 1 
			totalIterated = currentIterated 
			print(currentIterated)
			if (currentIterated > totalIterated)
				print("The current score" + currentIterated + "Is greater than" + totalIterated)
			else:
				print("The current score " + currentIterated + "Is lower than" + totalIterated)
		 #set total iterated to stop when player reaches goal 
	if valid_step(x=x+1, y=y+1): # make the player not touch the walls ever again 
		for i in range():
			pass
		pass
	else:
		minusScore = minusScore = - 0.5
	pass	#NEED TO CREATE A FUNCTION WHERE THERE SCORE 


	


	print("Total Steps taken to reach end goal:" )

#def qMaximation()


