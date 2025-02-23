n = int(input())
matrix =[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n):
    matrix[i][i],matrix[i][n-i-1]=matrix[i][n-i-1],matrix[i][i]
for row in matrix:
    print(' '.join(map(str, row)))
    #print(*row)
