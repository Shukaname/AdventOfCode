# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:13:54 2024

@author: tanou
"""
#%% Part 1
with open(r"./input1.txt", "r") as file:
    L1, L2 = [], []
    for line in file:
        vals = line.split()
        L1.append(int(vals[0]))
        L2.append(int(vals[1]))

L1.sort()
L2.sort()
sum_of_distance = 0
for i in range(len(L1)):
    sum_of_distance+=abs(L1[i]-L2[i])
print(sum_of_distance)

#%% Part 2
similarity_score = 0
for i in L1:
    similarity_score += i*L2.count(i)
print(similarity_score)