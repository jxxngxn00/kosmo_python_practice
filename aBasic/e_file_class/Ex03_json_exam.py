'''
    data / sample.json 파일을 읽고 총합 구해서 출력
'''

f = open('./data/sample.json', 'rt', encoding='utf-8-sig')
data = f.read()
f.close()

import json
i = json.loads(data)

sum=0

for k,v in i.items():
    sum += v['price'] * v['count']


print('총합 : ',sum)
