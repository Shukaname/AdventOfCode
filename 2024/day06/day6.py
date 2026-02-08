# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:34:23 2024

@author: tanou
"""

import numpy as np
from numpy.typing import NDArray


def turn(direction: tuple[int]) -> tuple[int]:
    # -1,0: North; 0,1: East; 1,0 South; 0,-1: West
    if direction[0] == 0:
        return (direction[1], 0)
    
    return (0, -direction[0])
        


file_name: str = "input1.txt"
with open(file_name, "r") as file:
    first_line = True
    for line in file:
        line = line.strip()
        grid_line = np.array(list(line))
        if first_line:
            original_grid: NDArray = grid_line
            first_line = False
        else:
            original_grid = np.vstack((original_grid, grid_line))


for i in range(original_grid.shape[0]):
    for j in range(original_grid.shape[1]):
        if original_grid[i,j] == "^":
            original_pos: tuple[int] = (i, j)

valid_position: int = 0
print(original_grid.size)
for i in range(original_grid.shape[0]):
    print(i)
    for j in range(original_grid.shape[1]):
        grid = original_grid.copy()
        if grid[i, j] == ".":
            grid[i, j] = "#"
        else:
            continue
        
        #set initial condition
        direction: list[int] = [-1, 0] # -1,0: North; 0,1: East; 1,0 South; 0,-1: West
        visited_pos: list[tuple[int]] = [original_pos]
        two_last_pos: list[tuple[any]] = []
        
        fail_safe_counter: int = 0
        fail_safe_limit: int = 10000
        while fail_safe_counter < fail_safe_limit:
            fail_safe_counter += 1
            if visited_pos[-1][0] in (0, grid.shape[0]-1) or visited_pos[-1][1] in (0, grid.shape[1]-1):
                break
            
            if grid[visited_pos[-1][0]+direction[0], visited_pos[-1][1]+direction[1]] == "#":
                direction = turn(direction)
            
            else:
                visited_pos.append((visited_pos[-1][0]+direction[0], visited_pos[-1][1]+direction[1]))
                two_last_pos.append((visited_pos[-2], visited_pos[-1]))
            
            if (len(two_last_pos)>0) and (two_last_pos.count(two_last_pos[-1])>1) :
                #there is a loop
                valid_position += 1
                break

        if fail_safe_counter == fail_safe_limit:
            print("fail_safe_limit reached")
            break

print(len(set(visited_pos)), valid_position)
