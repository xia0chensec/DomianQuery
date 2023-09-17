# -*- coding: utf-8 -*-
# @Author: xia0chen

import json
import requests
import time

def query_domain_info(domain,output_file=None):
    # 构建API请求URL
    url = f'https://apistore.aizhan.com/baidurank/siteinfos/a0201ed0e27cec1be98588d9c40c02d4?domains={domain}'

    try:
        # 发送API请求
        response = requests.get(url,timeout=2)
        response.raise_for_status()  # 检查响应状态

        # 解析JSON响应
        data = json.loads(response.text)
#print(data)
        success_data = data["data"]["success"]
        result_data = []
        if output_file:
            with open(output_file, "a") as f:
                for item in success_data:
                    domain = item["domain"]
                    pc_br = item["pc_br"]
                    m_br = item["m_br"]
                    if pc_br > 0 or m_br > 0:
                        print("\033[31m")
                        result_line = f"域名: {domain} 百度权重: {pc_br} 百度移动权重: {m_br}\n"
                        print(result_line, end=" ")
                        f.write(result_line)
                        result_data.append(result_line)
                        print("\033[0m")

                    else:
                        result = f"域名: {domain} 百度权重: {pc_br} 百度移动权重: {m_br}\n"
                        print(result, end=" ")
        else:
            for item in success_data:
                domain = item["domain"]
                pc_br = item["pc_br"]
                m_br = item["m_br"]
                if pc_br>0 or  m_br>0:
                    result_line = f"域名: {domain} 百度权重: {pc_br} 百度移动权重: {m_br}\n"
                    print("\033[31m"+result_line, end=" ")
                    result_data.append(result_line)
                    print("\033[0m")

                else:
                    result = f"域名: {domain} 百度权重: {pc_br} 百度移动权重: {m_br}\n"
                    print(result, end=" ")
                    print("\033[0m")

                    # 返回结果
            return result_data
        


    except requests.exceptions.RequestException as e:
        print(f"查询域名 {domain} 时发生异常:", e)

    except KeyError:
        print(f"未能提取域名 {domain} 的数据，请检查API响应格式。")

    except json.JSONDecodeError as e:
        print(f"解析域名 {domain} 的JSON数据时发生错误:", e)

    return []
