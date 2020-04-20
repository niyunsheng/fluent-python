from clip import clip
print(clip.__defaults__)
# (80,)
print(clip.__code__)  # doctest: +ELLIPSIS
# <code object clip at 0x...>
print(clip.__code__.co_varnames)
# ('text', 'max_len', 'end', 'space_before', 'space_after')
print(clip.__code__.co_argcount)
# 2
