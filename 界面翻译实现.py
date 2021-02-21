import requests
import time
import random
import hashlib
import json
import tkinter,re
from tkinter import *

class Youdao:
    def __init__(self, query):
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.query = query
        self.headers = {
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4263.3 Safari/537.36",
            "Cookie": "OUTFOX_SEARCH_USER_ID=713567564@123.149.156.124; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcfu02up3KHJ9ptSk-Ex; OUTFOX_SEARCH_USER_ID_NCOO=1183871014.8594327; ___rl__test__cookies=1613820241685"
        }

    # 生成ts字段结果
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
        # print(result)
        return result

    def run(self):
        # 分别获取ts,salt,sign加密字段字段
        ts = self.getTs()
        salt = self.getSalt(ts)
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
            "lts": ts,
            "bv": "9547aa1ba5be5d10d34f36c428394919",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION",

        }
        # 发送请求获取数据
        response = self.sendRequest(data)
        # 解析得到的数据
        data =self.parse(response)
        return data

# 点击翻译的函数
def send_msg(msg,v_top,v_bottom):
    # 如果翻译的内容为空则不作处理
    pattern =r'^\s*$'
    if re.fullmatch(pattern,msg):return
    # 如果翻译内容不为空，调用有道接口请求翻译
    yd = Youdao(msg)
    data =yd.run()
    v_bottom.delete(0.0,"end")
    v_bottom.insert("insert",data+"\n")


# 清空内容的函数
def del_msg(view_top,v_bottom):
    view_top.delete(0.0,"end")
    v_bottom.delete(0.0,"end")


def chatwith():
    root =tkinter.Tk() #实例一个窗口对象
    # root.geometry("500x400") #设置视图的大小
    root.minsize(500, 400)  # 最小尺寸
    root.maxsize(500, 400)  # 最大尺寸
    root.title("有道翻译") #设置视图的标题

    # 待翻译内容输入框
    view_top =tkinter.Text(root,height="12",relief="groove",bd="4",width="70")
    view_top.grid(row=1)
    # 翻译完成内容显示框
    view_bottom =tkinter.Text(root,height="12",relief="groove",bd="4",width="70",bg="#EBEBEB")
    view_bottom.grid(row=2)
    # 翻译按钮和清空按钮
    btn_send =tkinter.Button(root,text="翻译",bg="#E02433",width="10",fg="#fff",command=lambda :send_msg(view_top.get(0.0,"end"),view_top,view_bottom))
    btn_send.grid(row=3,pady="10 0",padx="180 0")
    btn_del =tkinter.Button(root, text="清空",width="10",command=lambda :del_msg(view_top,view_bottom))
    btn_del.grid(row=3,pady="10 0",padx="360 0")

    root.mainloop()


if __name__ == '__main__':
    chatwith()