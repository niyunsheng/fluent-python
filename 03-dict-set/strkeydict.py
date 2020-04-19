"""StrKeyDict always converts non-string keys to `str`

Test for initializer: keys are converted to `str`.

    >>> d = StrKeyDict([(2, 'two'), ('4', 'four')])
    >>> sorted(d.keys())
    ['2', '4']

Tests for item retrieval using `d[key]` notation::

    >>> d['2']
    'two'
    >>> d[4]
    'four'
    >>> d[1]
    Traceback (most recent call last):
      ...
    KeyError: '1'

Tests for item retrieval using `d.get(key)` notation::

    >>> d.get('2')
    'two'
    >>> d.get(4)
    'four'
    >>> d.get(1, 'N/A')
    'N/A'

Tests for the `in` operator::

    >>> 2 in d
    True
    >>> 1 in d
    False

Test for item assignment using non-string key::

    >>> d[0] = 'zero'
    >>> d['0']
    'zero'

Tests for update using a `dict` or a sequence of pairs::

    >>> d.update({6:'six', '8':'eight'})
    >>> sorted(d.keys())
    ['0', '2', '4', '6', '8']
    >>> d.update([(10, 'ten'), ('12', 'twelve')])
    >>> sorted(d.keys())
    ['0', '10', '12', '2', '4', '6', '8']
    >>> d.update([1, 3, 5])
    Traceback (most recent call last):
      ...
    TypeError: 'int' object is not iterable

"""
# BEGIN STRKEYDICT

import collections


class StrKeyDict(collections.UserDict):  # <1>

    def __missing__(self, key):  # <2>
        print('missing')
        # 如果找不到的键本身就是字符串，那就抛出 KeyError 异常
        if isinstance(key, str):
            raise KeyError(key)
        # 如果找不到的键不是字符串，那么把它转换成字符串再进行查找
        return self[str(key)]

    def __contains__(self, key):
        print('contain')
        return str(key) in self.data  # <3>

    def __setitem__(self, key, item):
        print('setitem')
        self.data[str(key)] = item   # <4>

# END STRKEYDICT