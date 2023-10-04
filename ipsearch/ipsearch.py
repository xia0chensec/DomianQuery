# -*- coding: utf-8 -*-
# @Author: xia0chen

import re
import tldextract
import requests
from module.baidu import query_domain_info
import time
def query_ip_info(ipaddress, output_file):
    mainDomainNameList = []

    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }
    url = f'https://api.webscan.cc/?action=query&ip={ipaddress}'
    try:
        rep = requests.get(url=url, headers=headers, timeout=2)
        results = rep.json()  # 解析API响应

        if results and results[0]["domain"] != ipaddress:
            for result in results:
                domainName = result["domain"]
                if re.match(
                        r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                        domainName):
                    continue
                val = tldextract.extract(domainName)
                domain = f"{val.domain}.{val.suffix}"      
            print(f"IP->[{ipaddress}]反查到的域名为: {domain}")
            query_domain_info(domain, output_file=output_file)  # 查询域名信息
        else:
            print(f"IP->[{ipaddress}]未反查到域名")
            print("\033[0m")
    except Exception as e:
        pass


