# encoding:UTF-8
import re
import urllib.request

def getHtml(url):
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    return data
def getImg(html):
    reg = r'src="(http://imgsrc.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

html = getHtml("http://tieba.baidu.com/p/4726996972")
print (getImg(html))

# print (getHtml("http://tieba.baidu.com/p/4726996972"))