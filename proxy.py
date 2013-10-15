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
			cj = cookielib.CookieJar()
			opener = urllib2.build_opener(proxy,urllib2.HTTPCookieProcessor(cj))
			opener.addheaders =[
				('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:11.0) Gecko/20100101 Firefox/11.0'),
				('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
			]
			urllib2.install_opener(opener)
			baidusearch = 'http://www.baidu.com/s?wd='+urllib.quote(keyword)
			print baidusearch
			response = urllib2.urlopen(baidusearch)
#			print response.geturl()
			baiduresponse = response.read()
			
			pattern = re.compile(r'(EC_desc|EC_url)"\s*href="(.+)"(\s*target.+|><span>)'+url)
			#print baiduresponse			
				
			if 'www.debaa' in baiduresponse:
				print 'ok'
			match = pattern.search(baiduresponse)

			if match:
				print pattern.groups
				requesturl = match.group(2)
				print requesturl
				response2 = urllib2.urlopen(requesturl)
				print response2.geturl()
			else:
				print 'no the fuck url'
			        responsefile = open('log.txt','a')
                	        responsefile.writelines(baiduresponse)
        	                responsefile.close
	
			
			time.sleep(proxyinterval);

		except Exception,ex:
			print 'proxy request fail'
			print  ex
			continue
'''proxyrun('超市管理','www.debaa.com',30)'''
