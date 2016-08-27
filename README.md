#Facebook文字雲介紹與操作



##取得個人臉書token，與時間代碼:

１．登入facebooke developer頁面（https://developers.facebook.com/）

２．上方工具列的“工具及支援“ 點擊頁面中的Graph API Explorer

3.勾選token的權限，點選Get Token->Get User Access token，只要勾選user_posts，即可，此時會請你登入Facebook，登入後頁面的token即會刷新（注意這個Token有時間性，一段時間後要重新取得Token）
![](https://raw.githubusercontent.com/xxxxsars/Facebook_analysis/master/pic/token_acess.png)


4.取得時間代碼，到以下頁面：http://www.epochconverter.com/ 取得時間代碼，選擇的時間為那個時間點到現在你所發文的內容
![](https://github.com/xxxxsars/Facebook_analysis/blob/master/pic/time.png?raw=true)


5.程式碼撰寫
```python
import requests
import json
import jieba
import collections
import re

#輸入所需資訊
since = '1325347200'
token = 'EAACEdEose0cBAJPq3aCZA4F2ALjw0PI5TxD7ZBWsms9r5bMhRcntz7qmaxZCeoUg0b6PVej0VVAPdGJZBZCC6rZBol2w2vNAXasD8zEfrJruxHSLSVmwh0r2nC2HnZCo8k6uxUytTI1a74mEODEAF8JgtekFy0HYmWV1zVugPZB5ji9M42cmMDW6'
url = ('https://graph.facebook.com/me/posts?since=%s&access_token=%s'%(since,token))
#測試是否有資料
#print(url)
res = requests.get(url)
jd = json.loads(res.text)
```
