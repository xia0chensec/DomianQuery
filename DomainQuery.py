# -*- coding: utf-8 -*-
# @Author: xia0chen

from module.baidu import query_domain_info
from module.argparse import parseArgs
from module.log import banner
from ipsearch.ipsearch import query_ip_info
import ipaddress
import requests
requests.packages.urllib3.disable_warnings()  # 抑制https错误信息
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def main():
    parseClass = parseArgs()
    args = parseClass.parse_args()
    output_file=args.output
    if args.url:
        # 判断输入是否为IP地址
        if is_valid_ip(args.url):
            # 进行IP域名反查
            domain = query_ip_info(args.url,output_file=output_file)
            # 再进行域名权重查询
            query_domain_info(domain, args.output)
        else:
            # 直接进行域名权重查询
            query_domain_info(args.url, args.output)
    elif args.file:
        try:
            with open(args.file, "r") as file:
                input_list = [line.strip() for line in file]

            for input_item in input_list:
                if is_valid_ip(input_item):
                    # 进行IP域名反查
                    domain = query_ip_info(input_item,output_file=output_file)
                    # 再进行域名权重查询
                    query_domain_info(domain, args.output)
                else:
                    # 直接进行域名权重查询
                    query_domain_info(input_item, args.output)

        except FileNotFoundError:
            print(f"找不到文件 {args.file}")
    else:
        print("请提供合适的参数：-u 域名或IP地址，-f 批量查询文件路径")

if __name__ == "__main__":
    banner()
    main()