# -*- coding: utf-8 -*-
# @Author: xia0chen

from module.baidu import query_domain_info
from module.argparse import parseArgs
from module.log import banner
from ipsearch.ipsearch import query_ip_info
import ipaddress
import requests
import re
import tldextract
from urllib.parse import urlparse
requests.packages.urllib3.disable_warnings()  # 抑制https错误信息

def extract_and_validate_ip(ip):
    ip_pattern = r'(\d+\.\d+\.\d+\.\d+)'  # 正则表达式用于提取IPv4地址
    match = re.search(ip_pattern, ip)
    
    if match:
        extracted_ip = match.group(1)  # 提取第一个分组中的IP地址
        return extracted_ip
    else:
        # 提取域名，例如http://bbfx.scuvc.com,则取出域名scuvc.com
        extracted_info = tldextract.extract(ip)
        top_level_domain = extracted_info.domain + "." + extracted_info.suffix
        return top_level_domain

def is_valid_ip(ip):     #判断输入是否合法
    extracted_ip = extract_and_validate_ip(ip)
    if extracted_ip:
        try:
            ipaddress.ip_address(extracted_ip)
            return True
        except ValueError:
            return False
    else:
        return False

def main():
    parseClass = parseArgs()
    args = parseClass.parse_args()
    output_file=args.output
    if args.url:
        extracted_info = extract_and_validate_ip(args.url)
        if extracted_info:
            if is_valid_ip(extracted_info):
                #如果是IP则进行IP反查
                domain=query_ip_info(extracted_info,output_file=output_file)
                #query_domain_info(domain, args.output)
            else:
                domain=extracted_info
            #如果是域名则进行权重查询
            query_domain_info(domain,args.output)
    elif args.file:
        try:
            with open(args.file, "r") as file:
                input_list = [line.strip() for line in file]

            for input_item in input_list:
                extracted_info=extract_and_validate_ip(input_item)
                if is_valid_ip(extracted_info):
                    #提取的是IP，进行IP域名反查
                    domain=query_ip_info(extracted_info,output_file=output_file)
                    # 再进行域名权重查询
                    query_domain_info(domain, args.output)
                else:
                    domain=extracted_info
                #如果是域名则进行权重查询
                query_domain_info(domain, args.output)
        except FileNotFoundError:
            print(f"找不到文件 {args.file}")
    else:
        print("Example:\npython DomainQuery.py -u ip/domain\npython DomainQuery.py -f file.txt\npython DomainQuery.py -f file.txt -o result.txt")

if __name__ == "__main__":
    banner()
    main()
