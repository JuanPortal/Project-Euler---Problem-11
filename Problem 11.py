# Project Euler - Problem 11

# First we create a 20x20 board full of zeroes
board = []
for i in range(20):
    board.append([])
    for j in range(20):
        board[i].append(0)

# Now we assign the real values to each one of the cells
board[0][0] = 8
board[0][1] = 2
board[0][2] = 22
board[0][3] = 97
board[0][4] = 38
board[0][5] = 15
board[0][6] = 0
board[0][7] = 40
board[0][8] = 0
board[0][9] = 75
board[0][10] = 4
board[0][11] = 5
board[0][12] = 7
board[0][13] = 78
board[0][14] = 52
board[0][15] = 12
board[0][16] = 50
board[0][17] = 77
board[0][18] = 91
board[0][19] = 8
board[1][0] = 49
board[1][1] = 49
board[1][2] = 99
board[1][3] = 40
board[1][4] = 17
board[1][5] = 81
board[1][6] = 18
board[1][7] = 57
board[1][8] = 60
board[1][9] = 87
board[1][10] = 17
board[1][11] = 40
board[1][12] = 98
board[1][13] = 43
board[1][14] = 69
board[1][15] = 48
board[1][16] = 4
board[1][17] = 56
board[1][18] = 62
board[1][19] = 0
board[2][0] = 81
board[2][1] = 49
board[2][2] = 31
board[2][3] = 73
board[2][4] = 55
board[2][5] = 79
board[2][6] = 14
board[2][7] = 29
board[2][8] = 93
board[2][9] = 71
board[2][10] = 40
board[2][11] = 67
board[2][12] = 53
board[2][13] = 88
board[2][14] = 30
board[2][15] = 3
board[2][16] = 49
board[2][17] = 13
board[2][18] = 36
board[2][19] = 65
board[3][0] = 52
board[3][1] = 70
board[3][2] = 95
board[3][3] = 23
board[3][4] = 4
board[3][5] = 60
board[3][6] = 11
board[3][7] = 42
board[3][8] = 69
board[3][9] = 24
board[3][10] = 68
board[3][11] = 56
board[3][12] = 1
board[3][13] = 32
board[3][14] = 56
board[3][15] = 71
board[3][16] = 37
board[3][17] = 2
board[3][18] = 36
board[3][19] = 91
board[4][0] = 22
board[4][1] = 31
board[4][2] = 16
board[4][3] = 71
board[4][4] = 51
board[4][5] = 67
board[4][6] = 63
board[4][7] = 89
board[4][8] = 41
board[4][9] = 92
board[4][10] = 36
board[4][11] = 54
board[4][12] = 22
board[4][13] = 40
board[4][14] = 40
board[4][15] = 28
board[4][16] = 66
board[4][17] = 33
board[4][18] = 13
board[4][19] = 80
board[5][0] = 24
board[5][1] = 47
board[5][2] = 32
board[5][3] = 60
board[5][4] = 99
board[5][5] = 3
board[5][6] = 45
board[5][7] = 2
board[5][8] = 44
board[5][9] = 75
board[5][10] = 33
board[5][11] = 53
board[5][12] = 78
board[5][13] = 36
board[5][14] = 84
board[5][15] = 20
board[5][16] = 35
board[5][17] = 17
board[5][18] = 12
board[5][19] = 50
board[6][0] = 32
board[6][1] = 98
board[6][2] = 81
board[6][3] = 28
board[6][4] = 64
board[6][5] = 23
board[6][6] = 67
board[6][7] = 10
board[6][8] = 26
board[6][9] = 38
board[6][10] = 40
board[6][11] = 67
board[6][12] = 59
board[6][13] = 54
board[6][14] = 70
board[6][15] = 66
board[6][16] = 18
board[6][17] = 38
board[6][18] = 64
board[6][19] = 70
board[7][0] = 67
board[7][1] = 26
board[7][2] = 20
board[7][3] = 68
board[7][4] = 2
board[7][5] = 62
board[7][6] = 12
board[7][7] = 20
board[7][8] = 95
board[7][9] = 63
board[7][10] = 94
board[7][11] = 39
board[7][12] = 63
board[7][13] = 8
board[7][14] = 40
board[7][15] = 91
board[7][16] = 66
board[7][17] = 49
board[7][18] = 94
board[7][19] = 21
board[8][0] = 24
board[8][1] = 55
board[8][2] = 58
board[8][3] = 5
board[8][4] = 66
board[8][5] = 73
board[8][6] = 99
board[8][7] = 26
board[8][8] = 97
board[8][9] = 17
board[8][10] = 78
board[8][11] = 78
board[8][12] = 96
board[8][13] = 83
board[8][14] = 14
board[8][15] = 88
board[8][16] = 34
board[8][17] = 89
board[8][18] = 63
board[8][19] = 72
board[9][0] = 21
board[9][1] = 36
board[9][2] = 23
board[9][3] = 9
board[9][4] = 75
board[9][5] = 0
board[9][6] = 76
board[9][7] = 44
board[9][8] = 20
board[9][9] = 45
board[9][10] = 35
board[9][11] = 14
board[9][12] = 0
board[9][13] = 61
board[9][14] = 33
board[9][15] = 97
board[9][16] = 34
board[9][17] = 31
board[9][18] = 33
board[9][19] = 95
board[10][0] = 78
board[10][1] = 17
board[10][2] = 53
board[10][3] = 28
board[10][4] = 22
board[10][5] = 75
board[10][6] = 31
board[10][7] = 67
board[10][8] = 15
board[10][9] = 94
board[10][10] = 3
board[10][11] = 80
board[10][12] = 4
board[10][13] = 62
board[10][14] = 16
board[10][15] = 14
board[10][16] = 9
board[10][17] = 53
board[10][18] = 56
board[10][19] = 92
board[11][0] = 16
board[11][1] = 39
board[11][2] = 5
board[11][3] = 42
board[11][4] = 96
board[11][5] = 35
board[11][6] = 31
board[11][7] = 47
board[11][8] = 55
board[11][9] = 58
board[11][10] = 88
board[11][11] = 24
board[11][12] = 0
board[11][13] = 17
board[11][14] = 54
board[11][15] = 24
board[11][16] = 36
board[11][17] = 29
board[11][18] = 85
board[11][19] = 57
board[12][0] = 86
board[12][1] = 56
board[12][2] = 0
board[12][3] = 48
board[12][4] = 35
board[12][5] = 71
board[12][6] = 89
board[12][7] = 7
board[12][8] = 5
board[12][9] = 44
board[12][10] = 44
board[12][11] = 37
board[12][12] = 44
board[12][13] = 60
board[12][14] = 21
board[12][15] = 58
board[12][16] = 51
board[12][17] = 54
board[12][18] = 17
board[12][19] = 58
board[13][0] = 19
board[13][1] = 80
board[13][2] = 81
board[13][3] = 68
board[13][4] = 5
board[13][5] = 94
board[13][6] = 47
board[13][7] = 69
board[13][8] = 28
board[13][9] = 73
board[13][10] = 92
board[13][11] = 13
board[13][12] = 86
board[13][13] = 52
board[13][14] = 17
board[13][15] = 77
board[13][16] = 4
board[13][17] = 89
board[13][18] = 55
board[13][19] = 40
board[14][0] = 4
board[14][1] = 52
board[14][2] = 8
board[14][3] = 83
board[14][4] = 97
board[14][5] = 35
board[14][6] = 99
board[14][7] = 16
board[14][8] = 7
board[14][9] = 97
board[14][10] = 57
board[14][11] = 32
board[14][12] = 16
board[14][13] = 26
board[14][14] = 26
board[14][15] = 79
board[14][16] = 33
board[14][17] = 27
board[14][18] = 98
board[14][19] = 66
board[15][0] = 88
board[15][1] = 36
board[15][2] = 68
board[15][3] = 87
board[15][4] = 57
board[15][5] = 62
board[15][6] = 20
board[15][7] = 72
board[15][8] = 3
board[15][9] = 46
board[15][10] = 33
board[15][11] = 67
board[15][12] = 46
board[15][13] = 55
board[15][14] = 12
board[15][15] = 32
board[15][16] = 63
board[15][17] = 93
board[15][18] = 53
board[15][19] = 69
board[16][0] = 4
board[16][1] = 42
board[16][2] = 16
board[16][3] = 73
board[16][4] = 38
board[16][5] = 25
board[16][6] = 39
board[16][7] = 11
board[16][8] = 24
board[16][9] = 94
board[16][10] = 72
board[16][11] = 18
board[16][12] = 8
board[16][13] = 46
board[16][14] = 29
board[16][15] = 32
board[16][16] = 40
board[16][17] = 62
board[16][18] = 76
board[16][19] = 36
board[17][0] = 20
board[17][1] = 69
board[17][2] = 36
board[17][3] = 41
board[17][4] = 72
board[17][5] = 30
board[17][6] = 23
board[17][7] = 88
board[17][8] = 34
board[17][9] = 62
board[17][10] = 99
board[17][11] = 69
board[17][12] = 82
board[17][13] = 67
board[17][14] = 59
board[17][15] = 85
board[17][16] = 74
board[17][17] = 4
board[17][18] = 36
board[17][19] = 16
board[18][0] = 20
board[18][1] = 73
board[18][2] = 35
board[18][3] = 29
board[18][4] = 78
board[18][5] = 31
board[18][6] = 90
board[18][7] = 1
board[18][8] = 74
board[18][9] = 31
board[18][10] = 49
board[18][11] = 71
board[18][12] = 48
board[18][13] = 86
board[18][14] = 81
board[18][15] = 16
board[18][16] = 23
board[18][17] = 57
board[18][18] = 5
board[18][19] = 54
board[19][0] = 1
board[19][1] = 70
board[19][2] = 54
board[19][3] = 71
board[19][4] = 83
board[19][5] = 51
board[19][6] = 54
board[19][7] = 69
board[19][8] = 16
board[19][9] = 92
board[19][10] = 33
board[19][11] = 48
board[19][12] = 61
board[19][13] = 43
board[19][14] = 52
board[19][15] = 1
board[19][16] = 89
board[19][17] = 19
board[19][18] = 67
board[19][19] = 48

# Then we print the board
for i in range(20):
    for j in range(20):
        if len(str(board[i][j])) == 2:  # If it's a 2 digit number we end it with 3 blank spaces
            print(board[i][j], end="   ")
        else:  # And if it's a 1 digit number, we end it with 4 blank spaces
            print(board[i][j], end="    ")
    print()


# Now we have to create different functions for the different ways we can move (up, down, left, right or diagonally)

# Let's start vertically
def vertically(table):
    products = []
    for k in range(20):  # 20 because of the columns
        for c in range(17):  # 17 is the amount of sums we are going to get for each column
            p = table[c][k] * table[c + 1][k] * table[c + 2][k] * table[c + 3][k]
            products.append(p)
    return products  # we return every sum possible done vertically


# Now horizontally
def horizontally(table):
    products = []
    for k in range(20):  # 20 because of the rows
        for c in range(17):  # 17 is the amount of sums we are going to get for each row
            p = table[k][c] * table[k][c + 1] * table[k][c + 2] * table[k][c + 3]
            products.append(p)
    return products  # we return every sum possible done horizontally


# Here comes the tricky part: the diagonals
# We have to consider that there's a difference between diagonal to the left and diagonal to the right

def diagonallyRight(table):
    products = []
    for k in range(17):  # We start from the fourth row to the 20th (20 - 4 + 1 = 17)
        for c in range(17):  # We start from the first column to the 17th (17 - 1 + 1 = 17)
            p = table[k + 3][c] * table[k + 2][c + 1] * table[k + 1][c + 2] * table[k][c + 3]
            products.append(p)
    return products  # we return every sum possible done diagonally to the right


def diagonallyLeft(table):
    products = []
    for k in range(17):  # We start from the first row to the 17th (17 - 1 + 1 = 17)
        for c in range(17):  # We start from the first column to the 17th (17 - 1 + 1 = 17)
            p = table[k][c] * table[k + 1][c + 1] * table[k + 2][c + 2] * table[k + 3][c + 3]
            products.append(p)
    return products  # we return every sum possible done diagonally to the left


# After that we just merge all the results into one big final list
every_sum = horizontally(board) + vertically(board) + diagonallyRight(board) + diagonallyLeft(board)

# And finally, we print it
print(f"\n{max(every_sum)}")
