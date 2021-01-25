import random
import string

from pprint import pprint

#this is a dictionary saved on a system
handle = open('/etc/dictionaries-common/words')
words = handle.readlines()
handle.close()


words = [ random.choice(words).upper().replace("'",'').strip() 
          for _ in range (5) ]

grid_size = 20

grid = [[ '_' for _ in range(grid_size)] for _ in range(grid_size) ]

def print_grid():
    for x in range(grid_size):
        print ('\t'*2 + ' '.join( grid[x] ))

for x in range(grid_size):
    for y in range(grid_size):
        if ( grid[x][y] == '_' ):
            grid[x][y] = random.choice(string.ascii_uppercase)
            
        
print_grid() 
# import random
# import string

# from pprint import pprint

# #this is a dictionary saved on a system
# handle = open('dictionary.txt')
# words = handle.readlines()
# handle.close()


# words = [ random.choice(words).upper().replace("'",'').strip() 
#           for _ in range (5) ]

# grid_size = 4

# grid = [[ '_' for _ in range(grid_size)] for _ in range(grid_size) ]

# def print_grid():
#     for x in range(grid_size):
#         print ('\t'*2 + ' '.join( grid[x] ))
        
# orientations = [ 'leftright','updown','diagonalup','diagonaldown' ]

# for word in words:
#     word_length = len(word)
    
#     # sometimes we may run out of room when trying to place a word
#     # so lets keep a boolean value to keep track of wether or not we were 
#     # actually able to to successfully place a word
#     placed = False
#     while not placed:
        
#         orientation = random.choice(orientations)
        
#         if orientation == 'leftright':
#             step_x = 1
#             step_y = 0
#         if orientation == 'updown':
#             step_x = 0
#             step_y = 1
#         if orientation == 'diagonaldown':
#             step_x = 1
#             step_y = 1
#         if orientation == 'diagonalup':
#             step_x = 1
#             step_y = 1
            
#         x_position = random.randint(0, grid_size)
#         y_position = random.randint(0, grid_size)
        
#         ending_x = x_position + word_length*step_x 
#         ending_y = y_position + word_length*step_y
        
#         if ending_x < 0 or ending_x >= grid_size: continue
#         if ending_y < 0 or ending_y >= grid_size: continue

#         failed = False
        
#         for i in range(word_length):
#             character = word[i]
            
#             new_position_x = x_position + i*step_y
#             new_position_y = y_position + i*step_y
            
#             character_at_new_position = grid[new_position_x][new_position_y]
#             if character_at_new_position != '_':
#                 if character_at_new_position == character:
#                    continue
#                 else:
#                     failed = True
#                     break
            
#         if failed:
#             continue
#         else:
#             for i in range(word_length):
#                 charackter = word[i]
                    
#                 new_position_x = x_position + i*step_x
#                 new_position_x = x_position + i*step_x
                    
#                 grid[new_position_x][new_position_y] = character
            
#             placed = True 
            
# for x in range(grid_size):
#     for y in range(grid_size):
#         if ( grid[x][y] == '_' ):
#             grid[x][y] = random.choice(string.ascii_uppercase)
                
# print_grid() 
# print ("Words are:")
# pprint (words)
                 
                