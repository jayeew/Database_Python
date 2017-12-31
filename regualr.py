#coding=utf-8
# m = re.search(pattern, string)  # 搜索整个字符串，直到发现符合的子字符串。
# m = re.match(pattern, string)   # 从头开始检查字符串是否符合正则表达式。必须从字符串的第一个字符开始就相符。
# 对于返回的m, 我们使用m.group()来调用结果
# str = re.sub(pattern, replacement, string)
# # 在string中利用正则变换pattern进行搜索，对于搜索到的字符串，用另一字符串replacement替换。返回替换后的字符串。
# re.split()    # 根据正则表达式分割字符串， 将分割后的所有子字符串放在一个表(list)中返回
# re.findall()  # 根据正则表达式搜索字符串，将所有符合的子字符串放在一给表(list)中返回

import re
import json

# m = re.split('[0-9]','aaaaa8aaa')
# print(m)
# pattern = re.compile('[a-aA-Z]')
# result = pattern.findall('gfIUWGUFGBGUG#$%468541SADF')
# print(result)
# print('\n')

# delete from user where i<2

# m = re.findall('create table name ((.*?,)*(.*)+$)','create table name (Son int(10),Sname char(10),Sex char(10))')
# print(m[0][0])
# m_ = re.findall('\(?(.*?)\)$',re.findall('create table name ((.*?,)*(.*)+$)','create table name (Son int(10),Sname char(10),Sex char(10))')[0][0])

# m = re.findall('\(?(.*?)\)$',re.findall('create table \w+ ((.*?,)*(.*)+$)','create table studen (name string 10,son int 10)')[0][0])[0].split(',')
# print(len(m))

m = re.findall('\(?(.*?)\)$', re.findall('create table \w+ ((.*?,)*(.*)+$)', 'create table zzz (zzz int 10)')[0][0])[0].split(',')
print(m[0])
# m = re.findall('\(?(.*?)\)$', re.findall('create table ((.*?,)*(.*)+$)', 'create table student (name string 10.son int 10 primarykey)')[0][0])[0].split(',')
# print(len(m))
# print(m[0])
# print(m[1])
# m = re.search('\[(.*?)\]', 'bfiwgdbfu[123]fhwueh[12345]')
# print(m.group(1))
# with open("../helloworld/wjy_json.json", "r") as load_f:
#     load_dict = json.load(load_f)
#     print(load_dict)


# with open("../helloworld/wjy_json.json", "r") as f:
#     f_ = json.load(f)
#     # print(f_)
#
# f_['user']['new_dict']={"name":{"firstname":"shuai", "lastname":"ge*******"}}
# with open("../helloworld/wjy_json.json", "w") as f_load:
#     json.dump(f_, f_load,sort_keys=True, indent=4, separators=(',', ': '))
#
# #查找
# with open("../helloworld/wjy_json.json", "r") as f_load_:
#     for lastname in json.load(f_load_)['user']['name']:
#         if lastname['lastname'] == "jiayi":
#             print(lastname['lastname'])

# print(loadFont())
# test_dict = {'bigberg': [7600, {1: [['phone', 6300p], ['Bike', 800], ['shirt', 300]]}]}
# print(test_dict)
# print(type(test_dict))
#
# json_str = json.dumps(test_dict) #字典转字符串
# print(json_str)
# print(type(json_str))
#
# new_dict = json.loads(json_str) #字符串转字典
# print(new_dict)
# print(type(new_dict))
#
# with open("../helloworld/wjy_json.json", "w") as f:
#     #将数据写入json中
#     json.dump(new_dict, f)
#     print("Upload Completed.")
#
# with open("../helloworld/wjy_json.json", "r") as load_f:
#     load_dict = json.load(load_f)
#     print(load_dict)
# load_dict['smallberg'] = [8200, {1:[['Python', 81], ['shirt', 300]]}]
# print(load_dict)
#
# with open("../helloworld/wjy_json.json", "w") as dump_f:
#     json.dump(load_dict, dump_f)