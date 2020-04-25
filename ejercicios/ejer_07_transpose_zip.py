data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
dataArray = True
dataY = [0, 0, 0, 0]
dataX = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
ctrl = 0
y = x = -1
while x < 3:
    x = x + 1
    y = -1
    while y < 2:
        y = y + 1
        dataX[y][x] = data[x][y]

dataY = [
    tuple(dataX[0]), tuple(dataX[1]), tuple(dataX[2])
]
data_transpose = tuple(dataY)  # replace with your code
print(data_transpose)
