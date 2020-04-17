import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)
memv = memoryview(numbers)
print(len(memv)) # 5
print(memv[0]) # -2

memv_oct = memv.cast('B')
print(memv_oct.tolist()) # [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]

memv_oct[5] = 4
print(numbers) # array('h', [-2, -1, 1024, 1, 2])