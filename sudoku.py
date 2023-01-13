mat=[[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
import random as r
from random import choice as c
# PRINTS THE SUDOKU PUZZLE
def printsudoku(mat):
    for i in range(4):
        print("---------------------------------")
        for j in range(4):
            print("|  ",mat[i][j], end="\t")
        print("|")
    print("---------------------------------")
#FIRST BOX IN SUDOKU
mat[r.randint(0,1)][r.randint(0,1)]=r.randint(1,4)
#SECOND BOX
# comment
n = r.randint(1,4)
if (n == 1):
    mat[0][2] = c([i for i in range(1, 5) if i not in [mat[0][0], mat[0][1], mat[2][2], mat[3][2]]])
elif (n == 2):
    mat[0][3] = c([i for i in range(1, 5) if i not in [mat[0][0], mat[0][1], mat[2][3], mat[3][3]]])
elif (n == 3):
    mat[1][2] = c([i for i in range(1, 5) if i not in [mat[1][0], mat[1][1], mat[2][2], mat[3][2]]])
else:
    mat[1][3] = c([i for i in range(1, 5) if i not in [mat[1][0], mat[1][1], mat[2][3], mat[3][3]]])
#THIRD BOX
n = r.randint(1,4)
if (n == 1):
    mat[2][0] = c([i for i in range(1, 5) if i not in [mat[0][0], mat[1][0], mat[2][2], mat[2][3]]])
elif (n == 2):
    mat[2][1] = c([i for i in range(1, 5) if i not in [mat[0][1], mat[1][1], mat[2][2], mat[2][3]]])
elif (n == 3):
    mat[3][0] = c([i for i in range(1, 5) if i not in [mat[0][0], mat[1][0], mat[3][2], mat[3][3]]])
else:
    mat[3][1] = c([i for i in range(1, 5) if i not in [mat[0][1], mat[1][1], mat[3][2], mat[3][3]]])
#LAST BOX IN SUDOKU
n = r.randint(1,4)
if (n == 1):
    mat[2][2] = c([i for i in range(1, 5) if i not in [mat[0][2], mat[1][2], mat[2][0], mat[2][1]]])
elif (n == 2):
    mat[2][3] = c([i for i in range(1, 5) if i not in [mat[0][3], mat[1][3], mat[2][0], mat[2][1]]])
elif (n == 3):
    mat[3][2] = c([i for i in range(1, 5) if i not in [mat[0][2], mat[1][2], mat[3][0], mat[3][1]]])
else:
    mat[3][3] = c([i for i in range(1, 5) if i not in [mat[0][3], mat[1][3], mat[3][0], mat[3][1]]])
printsudoku(mat)
"""#SOLVING SUDOKU
# FIRST BOX
for i in range(2):
    for j in range(2):
        if (mat[i][j] == " "):
            if (i == 0 and j == 0):
                mat[0][0] = c([i for i in range(1, 5) if i not in ([mat[0][1], mat[0][2], mat[0][3], mat[1][0], mat[2][0], mat[3][0], mat[1][1]])])
            elif (i == 0 and j == 1):
                mat[0][1] = c([i for i in range(1, 5) if i not in ([mat[0][0], mat[0][2], mat[0][3], mat[1][0], mat[2][1], mat[3][1], mat[1][1]])])
            elif (i == 1 and j == 0):
                mat[1][0] = c([i for i in range(1, 5) if i not in ([mat[0][0], mat[2][0], mat[3][0], mat[0][1], mat[1][3], mat[1][2], mat[1][1]])])
            elif (i == 1 and j == 1):
                mat[1][1] = c([i for i in range(1, 5) if i not in ([mat[0][1], mat[2][1], mat[3][1], mat[0][0], mat[1][3], mat[1][2], mat[1][0]])])
# SECOND BOX
for i in range(4):
    for j in range(4):
        if (mat[i][j] == " "):
            if (i == 0 and j == 2):
                mat[0][2] = c([i for i in range(1, 5) if i not in ([mat[0][0], mat[0][1], mat[0][3], mat[1][2], mat[2][2], mat[3][2], mat[1][3]])])
            elif (i == 0 and j == 3):
                mat[0][3] = c([i for i in range(1, 5) if i not in ([mat[0][0], mat[0][1], mat[0][2], mat[1][2], mat[1][3], mat[2][3], mat[3][3]])])
            elif (i == 1 and j == 2):
                mat[1][2] = c([i for i in range(1, 5) if i not in ([mat[1][0], mat[1][1], mat[1][3], mat[0][2], mat[2][2], mat[3][2], mat[0][3]])])
            elif (i == 1 and j == 3):
                mat[1][3] = c([i for i in range(1, 5) if i not in ([mat[1][0], mat[1][1], mat[1][2], mat[0][3], mat[2][3], mat[3][3], mat[0][2]])])
# THIRD BOX
for i in range(4):
    for j in range(4):
        if (mat[i][j] == " "):
            if (i == 2 and j == 0):
                mat[2][0] = c([i for i in range(1, 5) if i not in ([mat[0][0], mat[1][0], mat[3][0], mat[2][1], mat[2][2], mat[2][3], mat[3][1]])])
            elif (i == 2 and j == 1):
                mat[2][1] = c([i for i in range(1, 5) if i not in ([mat[0][1], mat[1][1], mat[3][1], mat[2][0], mat[2][2], mat[2][3], mat[3][0]])])
            elif (i == 3 and j == 0):
                mat[3][0] = c([i for i in range(1, 5) if i not in ([mat[0][0], mat[1][0], mat[2][0], mat[3][1], mat[3][2], mat[3][3], mat[2][1]])])
            elif (i == 3 and j == 1):
                mat[3][1] = c([i for i in range(1, 5) if i not in ([mat[0][1], mat[1][1], mat[2][1], mat[3][0], mat[3][2], mat[3][3], mat[2][0]])])

# FOURTH BOX
for i in range(4):
    for j in range(4):
        if (mat[i][j] == " "):
            if (i == 2 and j == 2):
                mat[2][2] = c([i for i in range(1, 5) if i not in ([mat[0][2], mat[1][2], mat[3][2], mat[2][0], mat[2][1], mat[2][3], mat[3][3]])])
            elif (i == 2 and j == 3):
                mat[2][3] = c([i for i in range(1, 5) if i not in ([mat[0][3], mat[1][3], mat[3][3], mat[2][0], mat[2][2], mat[2][1], mat[3][2]])])
            elif (i == 3 and j == 2):
                mat[3][2] = c([i for i in range(1, 5) if i not in ([mat[0][2], mat[1][2], mat[2][2], mat[3][0], mat[3][1], mat[3][3], mat[2][3]])])
            elif (i == 3 and j == 3):
                mat[3][3] = c([i for i in range(1, 5) if i not in ([mat[0][3], mat[1][3], mat[2][3], mat[3][0], mat[3][2], mat[3][1], mat[2][2]])])
printsudoku(mat)

"""
