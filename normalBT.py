import urllib2

import time
from datetime import datetime

proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:80"})
opener = urllib2.build_opener(proxy_support) 

text = open("normalBT.txt",'a')


for i in range(0, 10):
    order = "case " + str(i+1)
    text.write(order)


    urllib2.install_opener(opener)

    start = time.time()

    #request = urllib2.Request("http://en.wikipedia.org/wiki/Main_Page")
    request = urllib2.Request("http://www.daum.net")
    request.add_header('Pragma','no-store,no-cache,must-revalidate')
    request.add_header('Cache-Control', 'no-cache')
    
    
    content = urllib2.build_opener().open(request).read()

    end = time.time()
    result = end - start

    #print content

    now = datetime.now()
    text.write("\n%s sec   %s \n" % (result,now))
