Sample code for Chapter 1 - "The Python Data Model"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do


# 补充：collections.namedtuple

reference:[collections.namedtuple](https://docs.python.org/zh-cn/3/library/collections.html#collections.namedtuple)

```Python
# 创建命名元组子类的工厂函数
collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
```

举例：

```python
>>> # Basic example
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
>>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
33
>>> x, y = p                # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y               # fields also accessible by name
33
>>> p                       # readable __repr__ with a name=value style
Point(x=11, y=22)
```