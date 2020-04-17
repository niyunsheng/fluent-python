symbols = '$¢£¥€¤'

# 列表推导
codes = [ord(s) for s in symbols if ord(s) > 127]
print(codes)

# 列表推导+func
def non_ascii(c):
    return c > 127
codes = [ord(s) for s in symbols if non_ascii(ord(s))]
print(codes)

# filter+lambda
codes = list(filter(lambda c: c > 127, map(ord, symbols)))
print(codes)

# filter + func
codes = list(filter(non_ascii, map(ord, symbols)))
print(codes)

# 列表推导 笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# 生成式表达式 笛卡尔积
tshirts = ((color, size) for color in colors for size in sizes)

for tshirt in tshirts:
    print(tshirt)