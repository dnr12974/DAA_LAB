def knapsack(n,W,weights,values):
    M=[[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            if weights[i]>w:
                M[i][w]=M[i-1][w]
            else:
                M[i][w]=max(M[i-1][w],values[i]+M[i-1][w-weights[i]])
    return M[n][W]
n=int(input("Enter the number of elements:"))
weights=[0]*(n+1)
values=[0]*(n+1)
for i in range(1,n+1):
    weights[i]=int(input(f"Enter the weight for item {i}:"))
    values[i]=int(input(f"Enter the values of item {i}:"))
W=int(input("Enter the Max capacity:"))
max_val=knapsack(n,W,weights,values)
print(f"The knapsack value for maximum capacity {W} is:{max_val}")