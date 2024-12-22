def solve_n_queens(n):
    def is_safe(board,row,col):
        for i in range(row):
            if board[i]==col or\
               board[i]-i==col-row or \
               board[i]+i==col+row:
               return False
        return True
    def solve(board,row):
        if row==n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board,row,col):
                board[row]=col
                solve(board,row+1)
                board[row]=-1
    result=[]
    solve([-1]*n,0)
    return result
n=int(input("Enter the value of n:"))
solutions=solve_n_queens(n)
print(f"The solutions for the value of n={n} are: ")
for solution in solutions:
    print(solution)