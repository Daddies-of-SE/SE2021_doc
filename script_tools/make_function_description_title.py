from contextlib import redirect_stdout
import sys

def manufacture_title():
    TITLE_PREFIX = '3.3.2'
    FUNC_LVL = '#' * 5
    FUNC_NUM = 2
    DETAIL_LEVEL = FUNC_LVL + '#'
    for i in range(8, FUNC_NUM+8):
        print(f'{FUNC_LVL} {TITLE_PREFIX}.{i}')
        print(f'{DETAIL_LEVEL} {TITLE_PREFIX}.{i}.1 功能描述')
        print(f'{DETAIL_LEVEL} {TITLE_PREFIX}.{i}.2 操作流程')
        print(f'{DETAIL_LEVEL} {TITLE_PREFIX}.{i}.3 输入')
        print(f'{DETAIL_LEVEL} {TITLE_PREFIX}.{i}.4 输出')
        print(f'{DETAIL_LEVEL} {TITLE_PREFIX}.{i}.5 约束与约定')


f = sys.stdout
with redirect_stdout(f):
    manufacture_title()

