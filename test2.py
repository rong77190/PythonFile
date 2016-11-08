# encoding:UTF-8
import urllib.request

url = "http://tieba.baidu.com/p/4726996972"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)