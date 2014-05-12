from multiprocessing import Process, Pool
import urllib2
import time

def start():
	return time.time()

def http_get(url):

	start_time = start()
	result = {"url": url, "data": urllib2.urlopen(url, timeout=5).read()[:100]}
	print url + " : " + str(start() - start_time)
	return result

proxy = urllib2.ProxyHandler({'http': '155.98.39.24:3128/'})
opener = urllib2.build_opener(proxy) 
urls = ['http://en.wikipedia.org/', 'http://en.wikipedia.org/', 'http://en.wikipedia.org/', 'http://en.wikipedia.org/', 'http://en.wikipedia.org/', 'http://en.wikipedia.org/', 'http://en.wikipedia.org/', 'http://en.wikipedia.org/', 'http://en.wikipedia.org/', 'http://en.wikipedia.org/']
 

start_time = start()
pool = Pool(processes=10)



results = pool.map(http_get, urls)
for result in results:
	print result
