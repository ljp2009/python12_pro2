import time
import random
import hashlib
import json
import requests

#{"translateResult":[[{"tgt":"hello","src":"hello"}]],"errorCode":0,"type":"id2zh-CHS"}
# i: 你好python。12345689
# from: AUTO
# to: AUTO
# smartresult: dict
# client: fanyideskweb
# salt: 16138216486686
# sign: ea026101426dd4d841011eb8a5a8158a
# lts: 1613821648668
# bv: 2d8b03c2ac4b17dbe418ef6c20102144
# doctype: json
# version: 2.1
# keyfrom: fanyi.web
# action: FY_BY_REALTlME
#
# i: 你好python。123456
# from: AUTO
# to: AUTO
# smartresult: dict
# client: fanyideskweb
# salt: 16138208576366
# sign: f724a50d980cfab009efbcbb8747aa7f  #423067af53713e5d32bd778849ab64d6
# sign: 423067af53713e5d32bd778849ab64d6
# lts: 1613820857636
# bv: 2d8b03c2ac4b17dbe418ef6c20102144
# doctype: json
# version: 2.1
# keyfrom: fanyi.web
# action: FY_BY_REALTlME

# lts
# print(int(time.time()*1000))

# print(random.randint(0,9))

# salt = str(int(time.time()*1000) ) + str(random.randint(0, 9))
#
# md5 = hashlib.md5()
# encryption = "fanyideskweb" + "你好世界" + salt + "Tbh5E8=q6U3EXe+&L[4c@"
# md5.update(encryption.encode("utf-8"))
# sign = md5.hexdigest()
#
# print(sign)