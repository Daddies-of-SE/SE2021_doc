|      | web行数 | web commit | web 行数2 | backend行数 | backend commit | backend行数2 | wechat行数 | wechat commit | wechat行数2 | 总行数 | 总commit | 总行数2 | score | 工作量 | 工作量v2 |
| ---- | ------- | ---------- | --------- | ----------- | -------------- | ------------ | ---------- | ------------- | ----------- | ------ | -------- | ------- | ----- | ------ | -------- |
| wzk  | ~~52~~  | ~~10~~     | ~~13~~    | 2k**        | 60***          | 1k           | 12k\*\**** | 116           | 6k          | 8k     | 186      | 7k      | 300   | 22%    | 24%      |
| lyy  |         |            |           | 6k          | 126            | 2k           | ~~13~~     | ~~1~~         |             | 6k     | 127      | 2k      | 212   | 19%    | 21%      |
| yy   |         |            |           | 1k          | 46             | 0.6k         | 5k*        | 52            | 5k          | 6k     | 98       | 5.6k    | 183   | 18%    | 20%      |
| sxj  | 7k      | 29         | 5k        | 1k          | 32             | 1k           |            |               |             | 8k     | 61       | 6k      | 175   | 18%    | 20%      |
| kjs  | 1k      | 27         | 1k        | ~~?~~       | ~~5***~~       | ~~?~~        | 1k         | 15            | 0.7k        | 2k     | 47       | 1.7k    | 76    | 12%    | 15%      |
| wjr  |         |            |           | 2k          | 21             | 0.3k         |            |               |             | 2k     | 21       | 0.3k    | 50    | 11%    | 退课     |
| 总计 | 8k      | 66         | 6k        | 12k         | 290            | 4.9k         | 18k        | 184           | 11.7k       | 38k    | 540      | 22.6k   | 996   | 100%   | 100%     |

行数1为github上的addition，commit为github上的commit（不记merge），因此总数都会有出入

行数2为git blame结果

$score=\#lines/70+commit$，其中70为总行数/总commit作为均值，用于归一化

工作量：所有人均分50%（文档、测试等工作）+按score比例分配50%

\* 除去了小程序的lib目录的行数

\*\*除去了static和log文件的谜之行数

***人工修正了服务器上非本人的commit

\****除去了x-admin模板的行数

\*\****除去了小程序新页面模板的行数

~~划掉的是太少可以忽略~~

 
