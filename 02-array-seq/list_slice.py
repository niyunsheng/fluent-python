# 建立由列表组成的列表
board = [['_'] * 3 for _ in range(3)]
print(board) 
board[1][2] = 'X'
print(board)

# 上面这个代码等同于
board = []
for i in range(3):
    row=['_'] * 3 
    board.append(row)

# 下面这种方法不对，因为外面的列表其实包含 3 个指向同一个列表的引用
board = [['_'] * 3 ]*3
print(board) 
board[1][2] = 'X'
print(board)

# 上面这个代码等同于
row=['_'] * 3 
board = [] 
for i in range(3):
    board.append(row)