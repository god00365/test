import urllib2
import time
from datetime import datetime
from multiprocessing import Process, Pool
import requests
import re


text = open("SeqClientContentLoadTime.txt",'a')

def http_get(image):
	
	result = {"url": image, "data": requests.get(image, headers=headers,proxies=proxies)}
	return result


for i in range(0, 1):

	newId()
	start1 = time.time()
	
	headers = {'cache-control':'no-cache'}
	proxies = {"http":"http://127.0.0.1:6789",}
	website = requests.get('http://en.wikipedia.org/wiki/Main_Page', headers=headers,proxies=proxies) #html load
	
	end1 = time.time()

	timer1 = end1 - start1 #basic html load time

	html = website.text
	pat = re.compile(r'<\s*img [^>]*src="([^"]+)')
	img = pat.findall(html)

	imglen = len(img)

	for num in range(0,imglen) :
		img[num] = 'http:'+img[num]
	#print "%s \n" % (img[num])
	
	start2 = time.time()
	pool = Pool(processes = imglen)

	results = pool.map(http_get, img)
	#for result in results:
		#print result
	end2 = time.time()
	timer2 = end2 - start2
	
	res = timer1 + timer2
	
	text.write("\n%s\n" % (res))
