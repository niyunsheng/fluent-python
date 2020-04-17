# BEGIN BISECT_DEMO
import bisect
import sys
# 示例1：比较bisect和bisect_left的不同
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # <1>
        offset = position * '  |'  # <2>
        print(ROW_FMT.format(needle, position, offset))  # <3>

# 示例2：根据一个分数，找到它对应的成绩
def grade(bisect_fn,score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect_fn(breakpoints, score)
    return i

if __name__ == '__main__':
    # 示例2
    if sys.argv[-1] == 'left':    # <4>
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # <5>
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

    # 示例2
    print([grade(bisect_fn,score) for score in [33, 99, 77, 70, 89, 90, 100]])
# END BISECT_DEMO
