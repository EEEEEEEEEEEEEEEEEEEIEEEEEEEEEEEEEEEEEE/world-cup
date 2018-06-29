# 接口文档

#### 首页
**`/`**

示例
```
http://127.0.0.1:5000/

{
  "welcome": "Hello World!"
}
```


#### 返回 32 强球队名称，使用分页
**`all_teams?page=xx&per_page=xx`**
```
param: page: 页数
param: per_page: 每页数据数量
```

示例
```
$ http "http://127.0.0.1:5000/all_teams?page=2&per_page=10"
HTTP/1.0 200 OK
Content-Length: 234
Content-Type: application/json
Date: Fri, 29 Jun 2018 13:40:47 GMT
Server: Werkzeug/0.14.1 Python/3.6.4

[
    "巴西",
    "瑞典",
    "比利时",
    "突尼斯",
    "哥伦比亚",
    "波兰",
    "乌拉圭",
    "伊朗",
    "丹麦",
    "尼日利亚"
]
```


#### 返回各小组净胜球最多的球队
**`/most_gd`**

示例
```
$ http://127.0.0.1:5000/most_gd
HTTP/1.0 200 OK
Content-Length: 508
Content-Type: application/json
Date: Fri, 29 Jun 2018 13:36:03 GMT
Server: Werkzeug/0.14.1 Python/3.6.4

[
    {
        "A": [
            "乌拉圭",
            5
        ]
    },
    {
        "B": [
            "葡萄牙",
            1
        ]
    },
    {
        "C": [
            "法国",
            2
        ]
    },
    {
        "D": [
            "克罗地亚",
            6
        ]
    },
    {
        "E": [
            "巴西",
            4
        ]
    },
    {
        "F": [
            "瑞典",
            3
        ]
    },
    {
        "G": [
            "比利时",
            7
        ]
    },
    {
        "H": [
            "哥伦比亚",
            3
        ]
    }
]
```


#### 返回各小组晋级的前两名
**`/most_integral`**

示例
```bash
$ http http://127.0.0.1:5000/most_integral
HTTP/1.0 200 OK
Content-Length: 1128
Content-Type: application/json
Date: Fri, 29 Jun 2018 13:35:15 GMT
Server: Werkzeug/0.14.1 Python/3.6.4

[
    {
        "A": [
            [
                "乌拉圭",
                9
            ],
            [
                "俄罗斯",
                6
            ]
        ]
    },
    {
        "B": [
            [
                "西班牙",
                3
            ],
            [
                "葡萄牙",
                3
            ]
        ]
    },
    {
        "C": [
            [
                "法国",
                6
            ],
            [
                "丹麦",
                3
            ]
        ]
    },
    {
        "D": [
            [
                "克罗地亚",
                9
            ],
            [
                "尼日利亚",
                3
            ]
        ]
    },
    {
        "E": [
            [
                "巴西",
                6
            ],
            [
                "瑞士",
                3
            ]
        ]
    },
    {
        "F": [
            [
                "瑞典",
                6
            ],
            [
                "墨西哥",
                6
            ]
        ]
    },
    {
        "G": [
            [
                "比利时",
                9
            ],
            [
                "英格兰",
                6
            ]
        ]
    },
    {
        "H": [
            [
                "哥伦比亚",
                6
            ],
            [
                "日本",
                3
            ]
        ]
    }
]
```


#### 返回分差最大的三场比赛
**`/worst_games`**

示例
```bash
$ http http://127.0.0.1:5000/worst_games
HTTP/1.0 200 OK
Content-Length: 224
Content-Type: application/json
Date: Fri, 29 Jun 2018 13:39:40 GMT
Server: Werkzeug/0.14.1 Python/3.6.4

[
    [
        "俄罗斯:沙特阿拉伯",
        "5:0"
    ],
    [
        "俄罗斯:沙特阿拉伯",
        "5:0"
    ],
    [
        "英格兰:巴拿马",
        "6:1"
    ]
]
```
