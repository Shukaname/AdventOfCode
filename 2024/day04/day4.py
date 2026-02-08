# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:06:11 2024

@author: Nahte
"""

import numpy as np
from numpy.typing import NDArray


        
def search_xmas(grid: NDArray[str]) -> int:
    
    def try_xmas(grid: NDArray[str], i: int, j: int, i_lim: int, j_lim: int) -> int:
        nb_XMAS: int = 0
        if i>=3 and j>=3: #haut gauche
            if grid[i, j]+grid[i-1,j-1]+grid[i-2,j-2]+grid[i-3,j-3] == "XMAS":
                nb_XMAS += 1

        if i>=3 and j<=j_lim: #haut droit
            if grid[i, j]+grid[i-1,j+1]+grid[i-2,j+2]+grid[i-3,j+3] == "XMAS":
                nb_XMAS += 1

        if i>=3: #haut
            if grid[i, j]+grid[i-1,j]+grid[i-2,j]+grid[i-3,j] == "XMAS":
                nb_XMAS +=1

        #on vient de tester les 3 du dessus
        #maintenant les 3 du dessous:
        if i <= i_lim and j>=3: #bas gauche
            if grid[i, j]+grid[i+1,j-1]+grid[i+2,j-2]+grid[i+3,j-3] == "XMAS":
                nb_XMAS += 1

        if i <= i_lim and j<=j_lim: #bas droit
            if grid[i, j]+grid[i+1,j+1]+grid[i+2,j+2]+grid[i+3,j+3] == "XMAS":
                nb_XMAS += 1

        if i <= i_lim: #bas
            if grid[i, j]+grid[i+1,j]+grid[i+2,j]+grid[i+3,j] == "XMAS":
                nb_XMAS +=1

        #on vient de tester les 3 du bas
        #maintenant gauche et droite:
        if j>=3: # gauche
            if grid[i, j]+grid[i,j-1]+grid[i,j-2]+grid[i,j-3] == "XMAS":
                nb_XMAS += 1

        if j <= j_lim: #droite
            if grid[i, j]+grid[i,j+1]+grid[i,j+2]+grid[i, j+3] == "XMAS":
                nb_XMAS +=1

        
        return nb_XMAS
    
    i_lim: int = grid.shape[0]-4
    j_lim: int = grid.shape[1]-4
    
    nb_XMAS: int = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] == "X":
                nb_XMAS += try_xmas(grid, i, j, i_lim, j_lim)
                    
    return nb_XMAS

def search_x_mas(grid: NDArray[str]) -> int:
    def test_x_mas(grid: NDArray[str]):
        nb_xmas: int = 0
        
        if grid[0,0] == "M" and grid[2,2] == "S":
            nb_xmas += 1
        if grid[0,0] == "S" and grid[2,2] == "M":
            nb_xmas += 1
        if grid[0,2] == "M" and grid[2,0] == "S":
            nb_xmas += 1
        if grid[0,2] == "S" and grid[2,0] == "M":
            nb_xmas += 1
        
        return nb_xmas == 2
    
    
    nb_x_mas: int = 0
    #on cherche les A sur grid[1:-2, 1:-2]
    for i in range(1, grid.shape[0]-1):
        for j in range(1, grid.shape[1]-1):
            if grid[i, j] == "A":
                #on prend le carré 3x3 autour de A pour verifier si MAS apparait
                nb_x_mas += test_x_mas(grid[i-1:i+2, j-1:j+2])
    
    return nb_x_mas


file_name: str = "input1.txt"
with open(file_name, "r") as file:
    first_line: bool = True
    for line in file:
        line = line.strip()
        grid_line = np.zeros(len(line)).astype(str)
        for i in range(len(line)):
            grid_line[i] = line[i]
        if first_line:
            grid = grid_line
            first_line = False
        else:
            grid = np.vstack((grid, grid_line))

nb_XMAS: int = search_xmas(grid)
nb_x_mas: int = search_x_mas(grid)
print(nb_XMAS, nb_x_mas)


        
    
