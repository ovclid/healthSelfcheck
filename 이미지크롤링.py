#%%
#from urllib import request
import urllib


# 홈페이지에서 이미지는 img 태그에 있거나 css의 백그라운 이미지에 존재
# 찾는 방법 : 웹사이트 개발자 모드에서 Elements의 우측 별도 프레임에 Styles
url = "https://rl6cz18qh.toastcdn.net/eduro/1.9.8/images/common/loginhome_group_institute.png"

urllib.request.urlretrieve(url, "a.png")

#%%
