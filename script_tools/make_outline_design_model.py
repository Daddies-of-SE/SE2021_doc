from contextlib import redirect_stdout
import sys

def manufacture_title():
    """
    用于批量产生设计概要的模板

    使用方法：
    修改TITLE_ORDER为3/4/5/6
    修改TITLE_Alphabet为A/B/C/D
    修改FUNC_NUM为实际的功能个数
    然后run

    输出：见main里面的输出重定向
    """

    i = 1
    TITLE_ORDER = 3
    TITLE_Alphabet = 'A'
    FUNC_NUM = 24

    while i <= FUNC_NUM :
        TITLE_PREFIX = f'{TITLE_ORDER}.{i}'
        raw = \
            f"""
            ### {TITLE_PREFIX}  {TITLE_Alphabet}{i:02} 
            #### {TITLE_PREFIX}.1 实现简述及约定  

            #### {TITLE_PREFIX}.2 功能实现流程



            #### {TITLE_PREFIX}.3 用户界面设计

            | **NO** | **类型** | **信息内容** | **信息表现** | **说明** |
            | ------ | -------- | ------------ | ------------ | -------- |
            |        |          |              |              |          |

            输出：

            #### {TITLE_PREFIX}.4 相关接口

            | 序号 | 类型 | 接口编号/名称 | 来源/文档编号 | 说明 |
            | ---- | ---- | ------------- | ------------- | ---- |
            |      |      |               |               |      |

            #### {TITLE_PREFIX}.5 出错处理设计



            #### {TITLE_PREFIX}.6 出错信息

            | 序号 | 错误编码 | 错误信息 | 说明/处理办法 |
            | ---- | -------- | -------- | ------------- |
            | 1    |          |          |               |

            """
        print(raw)
        i += 1


# f = sys.stdout
f = open('out.txt','w', encoding='utf8')
with redirect_stdout(f):
    manufacture_title()
f.close()

