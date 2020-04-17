Sample code for Chapter 2 - "An array of sequences"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

# 补充：timeit库

reference：[timeit](https://docs.python.org/zh-cn/3/library/timeit.html)

该模块提供了一种简单的方法来计算一小段 Python 代码的耗时。它有 命令行界面 以及一个 可调用 方法。它避免了许多用于测量执行时间的常见陷阱.

```python
timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)
# 使用给定语句、 setup 代码和 timer 函数创建一个 Timer 实例，并执行 number 次其 timeit() 方法。可选的 globals 参数指定用于执行代码的命名空间。

# setup语句在开头只执行一次

timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=5, number=1000000, globals=None)
# 使用给定语句、 setup 代码和 timer 函数创建一个 Timer 实例，并使用给定的 repeat 计数和 number 执行运行其 repeat() 方法。可选的 globals 参数指定用于执行代码的命名空间。
```