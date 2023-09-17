# -*- coding: utf-8 -*-
# @Author: xia0chen

from argparse import ArgumentParser
def parseArgs():
    parser = ArgumentParser()
    #parser = argparse.ArgumentParser(description="1")
    parser.add_argument("-u", "--url", help="要查询的单个域名")
    parser.add_argument("-f", "--file", help="包含域名列表的文件名")
    parser.add_argument("-o", "--output", help="将查询结果输出到指定文件")
    return parser

if __name__ == "__main__":
    args = parseArgs()
