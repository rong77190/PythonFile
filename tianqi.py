#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='List'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import urllib
import json

class ZuiMei(object):
	def __init__(self):
		self.url='http://www.zuimeitianqi.com/zuimei/queryWeather'
		self.headers={}
		self.headers['User-Agent'] ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
		self.cities ={}
		#城市的id值
		self.cities['怀化'] ='01011505'
		self.cities['衡阳'] ='01011504'
		self.cities['长沙'] ='01011502'
		self.cities['益阳'] ='01011510'
		self.data = {}
		self.city ='长沙'

	def query(self,city='长沙'):
		if city not in self.cities:
			print ('暂时不支持当前城市')
			return None
		self.city = city
		data = urllib.urlencode({'cityCode':self.cities[self.city]}).encode('utf-8')
		req =urllib2.Request(self.url,data,self.headers)
		response =urllib2.urlopen(req)

		html =response.read().decode('utf-8')
		#print html
		self.json_parse(html)

	def json_parse(self,html):
		target =json.loads(html)
		high_temp = target['data'][0]['actual']['high']
		low_temp =target['data'][0]['actual']['low']
		current_temp=target['data'][0]['actual']['tmp']
		actual_desc =target['data'][0]['actual']['desc']
		air_aqigrad =target['data'][0]['air']['aqigrad']
		air_desc =target['data'][0]['air']['desc']
		print ('%s:%s~%s ℃ 现在温度:%s ℃ %s 空气质量:%s %s'%(self.city,low_temp,high_temp,current_temp,actual_desc,air_aqigrad,air_desc))

if __name__ == '__main__':
	zuimei =ZuiMei()
	zuimei.query('益阳')




