def isValidSudoku(board: list[list[str]]) -> bool:
    
    l1 = [] 
    l2 = [] 
    l3 = []
    c = 0
    for i in range(9): 
        d1 = {}
        d2 = {}
        for j in range(9):
            # Checks rows
            if board[i][j] != ".": 
                if board[i][j] in d1: 
                    return False
                else: 
                    d1[board[i][j]] = board[i][j]

            # Checks columns
            if board[j][i] != ".": 
                if board[j][i] in d2: 
                    return False 
                else: 
                    d2[board[j][i]] = board[j][i]

            # Uses L1, L2, and L3 for the box sections 
            if board[i][j]!=".":
                if c>=0 and c<=2: 
                    l1.append(board[i][j])
                if c>=3 and c<=5: 
                    l2.append(board[i][j])
                if c>=6 and c<=8: 
                    l3.append(board[i][j])
            c+=1
            if c == 9: 
                c = 0

            if (i == 2 and j == 8) or (i == 5 and j == 8) or (i == 8 and j == 8):
                if len(set(l1)) != len(l1) or len(set(l2)) != len(l2)  or len(set(l3)) != len(l3) : return False

                l1 = [] 
                l2 = []
                l3 = []

    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))