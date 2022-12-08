f = open('./data/temp.json','rt',encoding='utf-8-sig')
data = f.read()
f.close()
print(type(data)) # str

import json
items = json.loads(data)
print(type(items)) # dict

for k,val in items.items():
    # print(k, '>', val)
    print(k, '>>', val['Job']) # 직업만 뽑아냄

