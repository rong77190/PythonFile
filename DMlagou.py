import http.cookiejar
import urllib

cookie_container = http.cookiejar.CookieJar()
#将一个cookies容器和一个HTTP的cookie的处理器绑定
cookie_support = urllib.request.HTTPCookieProcessor(cookie_container)
#创建一个opener,设置一个handler用于处理http的url打开
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
#安装opener，此后调用urlopen()时会使用安装过的opener对象
urllib.request.install_opener(opener)
pre_url = 'http://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput='
res = urllib.request.urlopen(pre_url)
#生成cookie，保留在cookie处理插件cookieJar
url = 'http://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
headers = {
"User-Agent":"Mozilla/5.0 (Macintosh;Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
}

for pn in range(1,3):
param ={
'first':'true',
'pn':pn,
'kd':'数据挖掘'
}
post_data = urllib.parse.urlencode(param).encode('utf-8')
request = urllib.request.Request(url=url,data=post_data,headers=headers)
response = urllib.request.urlopen(request)
txt = response.read().decode()
print(txt)

