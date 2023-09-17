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
        if rep.text == "null":
            print(f"IP->[{ipaddress}]未反查到域名")
            print("\033[0m")
        else:
            results = rep.json()
            for result in results:
                domainName = result["domain"]
                if domainName == ipaddress:
                    print(f"IP->[{ipaddress}]未反查到域名")
                    print("\033[0m")
                else:
                    if re.match(
                            r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",domainName):
                        continue
                    # print(domainName)
                    if domainName in mainDomainNameList:
                        continue
 
                    val = tldextract.extract(domainName)
                    domain = f"{val.domain}.{val.suffix}"

            print(f"IP->[{ipaddress}]反查到的域名为: {domain}")
            domain_info=query_domain_info(domain,output_file=output_file)
            #print("主域名:", domain)
        
    except:
        pass

def query_batch_ips(file_path):
    try:
        with open(file_path, 'r') as file:
            ip_list = [line.strip() for line in file]

        for ip in ip_list:
            query_ip_info(ip)

    except FileNotFoundError:
        print(f"文件 {file_path} 不存在")
    except Exception as e:
        print(f"发生未知错误: {e}")

