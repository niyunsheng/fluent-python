# 元组用作记录
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport) # 元组拆包
# 排序后，元组内的值是不变的
# 经过测试，这里既是是一个二维列表，内部的值也是不变的
print(traveler_ids)

# 元组拆包
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude, longitude)

import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

# 用*处理剩下的元素
a, b, *rest = range(5)
print(a, b, rest) # 0, 1, [2, 3, 4]

a, *body, c, d = range(5)
print(a, body, c, d) # 0 [1, 2] 3 4

*head, b, c, d = range(5)
print(head, b, c, d) # [0, 1] 2 3 4

# 嵌套元组拆包

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # <2>
    if longitude <= 0:  # <3>
        print(fmt.format(name, latitude, longitude))

# 具名元组
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)

# _fields类方法
print(City._fields)

# 类方法 _make(iterable)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# _make() 通过接受一个可迭代对象来生成这个类的一个实例
# 它的作用跟 City(*delhi_data) 是一样的
delhi = City._make(delhi_data)
print(delhi)
# 实例方法 _asdict()
print(delhi._asdict()) # type:OrderedDict

