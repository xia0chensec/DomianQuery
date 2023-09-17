## Domain Query

### 工具介绍

一款用于查询网站权重(仅支持查询百度权重)和IP反查域名的工具，支持单个/批量的域名/IP查询

````
            ********************************
            #                              #
            #         Domain Query         #
            #                              #
            ********************************
                    支持网站权重查询和IP反查域名
                                            Author:xia0chen

usage: DomainQuery.py [-h] [-u URL] [-f FILE] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     要查询的单个域名
  -f FILE, --file FILE  包含域名列表的文件名
  -o OUTPUT, --output OUTPUT        将查询结果输出到指定文件
````

### 如何使用

```
单个域名查询权重
python .\DomainQuery.py -u baidu.com
```



```
单个IP反查域名
python .\DomainQuery.py -u 222.215.172.58
```



```
批量查询
python .\DomainQuery.py -f domain.txt
```

