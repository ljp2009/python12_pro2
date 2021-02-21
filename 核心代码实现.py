import time
import random
import hashlib
import json
import requests


class Youdao:
    def __init__(self, query):
        # 翻译接口地址
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.query = query
        self.headers = {
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4263.3 Safari/537.36",
            "Cookie": "OUTFOX_SEARCH_USER_ID=713567564@123.149.156.124; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcfu02up3KHJ9ptSk-Ex; OUTFOX_SEARCH_USER_ID_NCOO=1183871014.8594327; ___rl__test__cookies=1613820241685"
        }

    # 生成lts字段结果
    def getTs(self):
        ts = str(int(time.time() * 1000))
        return ts

    # 生成salt字段结果
    def getSalt(self, ts):
        salt = ts + str(random.randint(0, 9))
        return salt

    # 生成sign加密字段结果
    def getSign(self, salt):
        md5 = hashlib.md5()
        encryption = "fanyideskweb" + self.query + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        md5.update(encryption.encode("utf-8"))
        sign = md5.hexdigest()
        return sign

    # 向接口发送post请求
    def sendRequest(self, data):
        response = requests.post(self.url, headers=self.headers, data=data).content.decode("utf-8")
        return response

    # 解析返回的数据
    def parse(self, response):
        response = json.loads(response)
        # print(response)
        result = response["translateResult"][0][0]["tgt"]
        print(result)

    def run(self):
        # 分别获取ts,salt,sign加密字段字段
        lts = self.getTs()
        salt = self.getSalt(lts)
        sign = self.getSign(salt)
        # 准备发送post请求的字段
        data = {
            "i": self.query,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": lts,
            "bv": "9547aa1ba5be5d10d34f36c428394919",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION",

        }
        # 发送请求获取数据
        response = self.sendRequest(data)
        # 解析得到的数据
        self.parse(response)


if __name__ == '__main__':
    yd = Youdao("你好世界")
    yd.run()