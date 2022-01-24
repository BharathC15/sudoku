# inspiration - youtube - https://www.youtube.com/watch?v=mcXc8Mva2bA
# i -> Row
# j -> Column

GRIDSIZE = 9
IntersectionSize = 3

def sudoPrinter(grid): # print sudoku grid in a pleasing pattern
    for i in range(GRIDSIZE):
        if i % 3 == 0 and i != 0:
            print('\n-----------')
        else:
            print()
            
        for j in range(GRIDSIZE):
            if j % 3 == 0 and j != 0 :
                print('|',end = '')
            print(grid[i][j],end = '')
    
    print()
    
def numValidRow(grid,num,row): # Returns True if it is possible to insert number in the row
    for j in range(GRIDSIZE):
        if grid[row][j] == num:
            return False
    return True

def numValidCol(grid,num,col): # Returns True if it is possible to insert number in the col
    for i in range(GRIDSIZE):
        if grid[i][col] == num:
            return False
    return True

def numValidBox(grid,num,row,col): # Returns True if it is possible to insert number in the box
    x = int(row/3)
    y = int(col/3)
    
    irow = 3 * x
    icol = 3 * y
    
    for ix in range(irow,irow+3):
        for iy in range(icol,icol+3):
            #print(ix,iy)
            if grid[ix][iy] == num:
                return False
    return True
    
def numCheckAll(grid,num,row,col): # Returns True if all above condition statisfy else return false
    return numValidRow(grid,num,row) and numValidCol(grid,num,col) and numValidBox(grid,num,row,col)

def solveSudoku(grid):
    toTry = 1
    
    for i in range(GRIDSIZE):
        for j in range(GRIDSIZE):
            if grid[i][j] == 0:
                for toTry in range(1,GRIDSIZE+1):
                    if numCheckAll(grid,toTry,i,j):
                        grid[i][j] = toTry
                        if solveSudoku(grid):
                            return True
                        else: 
                            grid[i][j] = 0

    print(grid)
    return True

if __name__ == '__main__':
        
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    print('Unsolved Sudoku...')
    sudoPrinter(grid)
    
    finalGrid = solveSudoku(grid)
    print('Solved Sudoku...',finalGrid)