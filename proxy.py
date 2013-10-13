#!/usr/bin/python encoding=utf-8	
import urllib,urllib2,cookielib,json,time,hashlib,re,socket
import re


def proxyrun(keyword,url,proxyinterval):
	filename = 'ip.txt'
	input = open(filename)
	lines = input.readlines()
	input.close()
	ipnum = len(lines)

	for i in range(0,ipnum):
		proxyip = lines[i].strip().split('@')[0]
		print proxyip
		socket.setdefaulttimeout(10)
		try:
			proxy = urllib2.ProxyHandler({'http':proxyip})
			opener = urllib2.build_opener(proxy)
			urllib2.install_opener(opener)
			baidusearch = 'http://www.baidu.com/s?wd='+urllib.quote(keyword)
			print baidusearch
			response = urllib2.urlopen(baidusearch)
			'''print response.read()'''
			baiduresponse = response.read()
			
			pattern = re.compile(r'EC_url"\s*href="(.+)"><span>'+url)
			'''print baiduresponse			
			responsefile = open('log.txt','w')
			responsefile.writelines(baiduresponse)
			responsefile.close
				
			if 'www.debaa' in baiduresponse:
				print 'ok'''
			match = pattern.search(baiduresponse)

			if match:
				print pattern.groups
				requesturl = match.group(1)
				print requesturl
				response2 = urllib2.urlopen(requesturl)
			else:
				print 'no the fuck url'

			
			time.sleep(proxyinterval);

		except Exception,ex:
			print 'proxy request fail'
			print  ex
			continue
'''proxyrun('超市管理','www.debaa.com',30)'''
