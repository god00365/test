import requests
import re
import time
from multiprocessing import Process, Pool
import urllib2


text = open("normalCT.txt",'a')

def http_get(image):
	
	result = {"url": image, "data": requests.get(image, headers=headers)}
	return result




for i in range(0, 5):

	start1 = time.time()

	headers = {'cache-control':'no-cache'}
	website = requests.get('http://en.wikipedia.org/wiki/Main_Page', headers=headers) #html load
	#website = requests.get('http://www.daum.net', headers=headers)#html load
	end1 = time.time()

	timer1 = end1 - start1 #base html load time

	html = website.text
	pat = re.compile(r'<\s*img [^>]*src="([^"]+)')
	img = pat.findall(html)

	imglen = len(img)

	for num in range(0,imglen) :
		img[num] = 'http:'+img[num]
	#print "%s \n" % (img[num])
	
	
	opener = urllib2.build_opener() 
	
	start2 = time.time() 
	pool = Pool(processes = imglen)

	results = pool.map(http_get, img)
	#for result in results:
		#print result
	end2 = time.time()
	timer2 = end2 - start2 #timecheck for image
	
	res = timer1 + timer2
	
	text.write("\n%s\n" % (res))
	

	

#for down in range(0,imglen):
#	
#	image = requests.get(img[down])

#	rs = (grequests.get(u) for u in img)
#	grequests.map(rs)
#
#	end2 = time.time() #timecheck end
#
#	timer2 = end2 - start2 #image load time
#
#	result = timer1 + timer2 # basic + image load time
#	
#	text.write("\n%s\n" % (result))
#print timeresult
