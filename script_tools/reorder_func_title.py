import re

"""
使用脚本前请手动把内容的顺序调换
此脚本将自动改写标题的标号
"""

def reorder_332(_lines) :
    FUNC_NUM = 9
    old = list(range(1, FUNC_NUM + 1))
    new = [2, 3, 4, 5, 6, 7, 8, 1, 9]
    assert len(old) == len(new)
    for l in range(len(_lines)) :
        for i in range(FUNC_NUM) :
            # 注意字符串的第一个字符是空格
            old_str = f" 3.3.2.{old[i]}"
            new_str = f" 3.3.2.{new[i]}"
            if old_str in _lines[l] :
                _lines[l] = _lines[l].replace(old_str, new_str)
                break
    return _lines

def reorder_331(_lines) :
    old = [19,20,21,22,24, 1, 2, 3, 4, 17,  5,  6,  7,  8,  9, 10, 11, 13, 14, 15, 16, 23, 18, 12]
    new = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    assert set(old) == set(new) == set(range(1,25))
    assert len(old) == len(new) == 24
    old2new = [(old[i], new[i]) for i in range(len(old))]
    # 从大到小，以防将3.3.1.10识别为3.3.1.1这种情况
    old2new.sort(key=lambda x : x[0], reverse=True)
    for l in range(len(_lines)) :
        for i in range(len(old2new)):
            # 注意字符串的第一个字符是空格
            old_str = f" 3.3.1.{old2new[i][0]}"
            new_str = f" 3.3.1.{old2new[i][1]}"
            if old_str in _lines[l] :
                _lines[l] = _lines[l].replace(old_str, new_str)
                break
    return _lines



with open("../ReqSpec/RequirementsSpecification.md", 'r', encoding='utf-8') as fr, \
            open("../ReqSpec/RequirementsSpecification2.md", 'w', encoding='utf-8') as fw:
    lines = fr.readlines()
    reorder_332(lines)
    reorder_331(lines)
    fw.writelines(lines)


