#!/usr/bin/python encoding=utf-8
import time,thread
import proxy
def start(runtimes,interval,proxyinterval,keyword,url):
	for i in range(0,runtimes):
                proxy.proxyrun(keyword,url,proxyinterval);
                time.sleep(interval) 

if __name__ == '__main__':
	start(2,60,30,'超市管理','www.debaa.com')
