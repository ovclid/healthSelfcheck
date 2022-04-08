#%% 
#urllib.request 모듈을 활용한 이미지 다운로드
import urllib.request

# 'https://hcs.eduro.go.kr/#/loginHome' 첫 화면의 대학교 이미지 다운로드
# HTML 이미지는 <img> 태그안에 있거나 css의 background img로 존재
# 확인방법은 크롬 검사모드에서 Elements -> Styles

url = "https://rl6cz18qh.toastcdn.net/eduro/1.9.8/images/common/loginhome_group_institute.png"
urllib.request.urlretrieve(url, "c.png")

#%%
#requests 모듈을 활용한 이미지 다운로드
#requests 모듈이 좀더 빠르고 우회할 수 있는 방법 제공

import requests

headers = headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
pic = requests.get(url, headers=headers)

with open('d.jpg', 'wb') as photo:
    photo.write(pic.content)
# %%
