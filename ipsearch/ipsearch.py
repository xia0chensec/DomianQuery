# -*- coding: utf-8 -*-
# @Author: xia0chen

import re
import tldextract
import requests
from module.baidu import query_domain_info
import time

# def query_ip_info(ipaddress, output_file):
#     # 构建API请求URL
#     url = f'https://api.webscan.cc/?action=query&ip={ipaddress}'
#
#     try:
#         # 发送API请求
#         response = requests.get(url, timeout=3)
#         response.raise_for_status()  # 检查响应状态
#
#         # 解析JSON响应
#         data = json.loads(response.text)
#
#         if "null" in response.text:
#             print(f"IP->[{ipaddress}]未反查到域名")
#         else:
#             domain_values = [item['domain'] for item in data]
#             # 打印提取出的值
#             domain = domain_values[0]
#             print("\033[0m")
#             print(f"IP->[{ipaddress}]反查到的域名为: {domain}")
#
#             # 查询域名权重并打印结果
#             # domain_info = query_domain_info(domain)
#             # if output_file:
#             #     query_domain_info(domain, output_file='result.txt')
#             #print(f"调用 query_domain_info 函数，输出文件为: {output_file}")
#             domain_info = query_domain_info(domain, output_file=output_file)
#             #print(f"query_domain_info 函数返回结果: {domain_info}")
#             # if domain_info and output_file:
#             #     with open(output_file, 'a') as file:
#             #         for result in domain_info:
#             #             file.write(result + "\n")
#
#     except requests.exceptions.RequestException as e:
#         print(f"请求出错: {e}")
#     except json.JSONDecodeError as e:
#         print(f"JSON解析错误: {e}")
#     except Exception as e:
#         print(f"发生未知错误: {e}")
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

