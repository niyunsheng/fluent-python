Sample code for Chapter 3 - "Dictionaries and sets"

From the book "Fluent Python" by Luciano Ramalho (O'Reilly, 2015)
http://shop.oreilly.com/product/0636920032519.do

# 补充：正则表达式库re

## 正则表达式对象

re.compile(pattern, flags=0)

将正则表达式的样式编译为一个 正则表达式对象 （正则对象），可以用于匹配，通过这个对象的方法 match(), search() 以及其他如下描述：

re.finditer(pattern, string, flags=0)

pattern 在 string 里所有的非重复匹配，返回为一个迭代器 iterator 保存了 匹配对象 。 string 从左到右扫描，匹配按顺序排列。空匹配也包含在结果里。

## 匹配对象

```
match = re.search(pattern, string)
if match:
    process(match)
```

Match.group([group1, ...])

返回一个或者多个匹配的子组。如果只有一个参数，结果就是一个字符串，如果有多个参数，结果就是一个元组（每个参数对应一个项），如果没有参数，组1默认到0（整个匹配都被返回）.

