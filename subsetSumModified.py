def subset_sum(n, W, weights):
    M = [[False] * (W + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        M[i][0] = True
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i] > w:
                M[i][w] = M[i-1][w]
            else:
                M[i][w] = M[i-1][w] or M[i-1][w-weights[i]]
    
    if M[n][W]:
        subset = []
        i, w = n, W
        while i > 0 and w > 0:
            if M[i][w] and not M[i-1][w]:  # Element i is included in the subset
                subset.append(weights[i])
                w -= weights[i]
            i -= 1
        print(f"The subset with sum {W} exists: {subset[::-1]}")
    return M[n][W]

n = int(input("Enter the number of elements: "))
weights = [0] * (n + 1)
for i in range(1, n + 1):
    weights[i] = int(input(f"Enter the weight {i}: "))
W = int(input("Enter the target sum: "))
answer = subset_sum(n, W, weights)
if answer:
    print(f"The subset with sum {W} exists:")
else:
    print(f"The subset with sum {W} does not exist")
