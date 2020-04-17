from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __repr__ 这个特殊方法来得到一个对象的字符串表示形式的
    def __repr__(self):
        return 'repr_Vector(%r, %r)' % (self.x, self.y)

    # 有__str__方法时会优先调用
    def __str__(self):
        return 'str_Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        # print("abs")
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        # print("add")
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # 实现了v*const的运算，注意不是向量相乘
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__=="__main__":
    v1 = Vector(2,4)
    v2 = Vector(2,1)
    print(v1+v2)
    print(abs(v1))
    print(v1*3)
    print(bool(v1))
