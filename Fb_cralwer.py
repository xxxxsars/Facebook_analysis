import requests
import json
import jieba
import collections
import re

#輸入所需資訊
since = '1325347200'
token = 'EAACEdEose0cBAMZADrG525Xgg3ejm76rS5NexaR8yZBuSkYmZC2TbUUnoFtP0QuvZAsd845oLvoITFXij2uRmzqGmgKt8E1zmV9Ryk2JZAoDtQrEQ5eF7pCbjkw8NRR4ZCIBZCQgmXkLnhxlIVLC9C7plHXoj3qvURMsSB8dapY1SDP5mm0IZBt1'
url = ('https://graph.facebook.com/me/posts?since=%s&access_token=%s'%(since,token))
#測試是否有資料
#print(url)
res = requests.get(url)
jd = json.loads(res.text)

#利用迴圈抓取每頁的資訊並將message做分詞將全部字詞存入words list中
words =[]
while 'paging' in jd:
    for post in jd['data']:
        if 'message' in post:
            temp_words = list(jieba.cut(re.sub('\W+','',post['message'])))
            for word in temp_words:
                words.append(word)
    res = requests.get(jd['paging']['next'])
    jd = json.loads(res.text)

#透過collections套件做次數計算與字詞的排列
count_words = collections.Counter(words)
sorted_words = sorted(dict(count_words).items(),key  = lambda x:x[1],reverse = True)

#最後將結果寫入文字檔
with open('word.txt','w',encoding = 'utf-8') as fin:
    for word in sorted_words:
        print(word[0],(word[1]))