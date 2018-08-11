"""
My own solution to whiteboarding question:
Given a grid of random colors, find the maximum number of connected colors.

author: Lubos Valco
"""

import random

#test data
array = [[random.choice(["g", "b", "r"]) for x in range(10)] for y in range(10)]

height = len(array)
width = len(array[0])

#this array of Booleans remembers whether a tile was checked
bool_array = [[True for x in range(width)] for y in range(height)]

#input data preview
#TODO: Custom print for array could be implemented but im in python 2.7 so no 'sep' in print() lol
for row in array:
	print row

#number of the same colored tiles
counter = 0

#where the selected tiles of the same color are located in an array
color_coordinates = []

#final output
results = []

#returns a nested list of tile coordinates that are availible to check
def find_surroundings(x, y):
	return_list = []
	#check right only for x lower than max width
	try:
		if x < width and bool_array[x+1][y]:	
			return_list.append([x+1,y])
	except:
		pass
	#check left only for x higher than 0
	try:
		if x > 0 and bool_array[x-1][y]:
			return_list.append([x-1,y])
	except:
		pass
	#check down only for y lower than max height
	try:
		if y < height and bool_array[x][y+1]:
			return_list.append([x,y+1])
	except:
		pass
	#check up only for y higher than 0
	try:
		if y > 0 and bool_array[x][y-1]:
			return_list.append([x,y-1])
	except:
		pass
	return return_list

#checks every unchecked tile and recursively counts all its neighbours that share the same color
def find_all_neighbours(x, y, color):
	global counter
	global color_coordinates
	
	#prevents going out of bounds
	countable_neighbours = find_surroundings(x,y)
	
	#check every availible neighbour whether it has the same color 
	for coordinate in countable_neighbours:
		if color == array[coordinate[0]][coordinate[1]] and bool_array[coordinate[0]][coordinate[1]] == True:
			#mark tile as already counted
			bool_array[coordinate[0]][coordinate[1]] = False
			
			#count this tile
			counter+=1
			#add this tile's coordination to output list
			color_coordinates.append([coordinate[0], coordinate[1]])
			
			#continue with the next tile
			find_all_neighbours(coordinate[0], coordinate[1], color)
		
	return [counter, color, color_coordinates]

#iterate through the matrix
for i in range(0, height):
	for j in range(0, width):
	
		#skips already checked tiles
		if bool_array[i][j]:
			all_tiles_of_the_same_color = find_all_neighbours(i, j, array[i][j])
			#in case if tiles were alone
			bool_array[i][j] = False
		
		#remember the highest amount of connected tiles
		if not results or results[0] < all_tiles_of_the_same_color[0]:
			results = all_tiles_of_the_same_color
		counter = 0
		color_coordinates = []

#prepare array to print out the results
output_array = [["_" for x in range(width)] for y in range(height)]

#rewrite the array to show only the result
for coordinate in results[2]:
	output_array[coordinate[0]][coordinate[1]] = results[1]

#results screen
print "the biggest color is: ", results[1], ", with the size of ", results[0]
for row in output_array:
	print row