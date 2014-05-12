import urllib2
from TorCtl import TorCtl
import time
from datetime import datetime

proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
opener = urllib2.build_opener(proxy_support) 

text = open("TorBasicTime.txt",'a')

def newId():
    conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="")
    conn.send_signal("NEWNYM")




for i in range(0, 10):
    order = "case " + str(i+1)
    text.write(order)
    newId()
	

    start = time.time()
    proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
    urllib2.install_opener(opener)

    #request = urllib2.Request("http://en.wikipedia.org/wiki/Main_Page")
    request = urllib2.Request("http://www.daum.net")	
    request.add_header('Pragma','no-store,no-cache,must-revalidate')
    request.add_header('Cache-Control', 'no-cache')
    
    
    content = urllib2.build_opener(proxy_support).open(request)
    contrd = content.read()
    end = time.time()
    result = end - start

    #print content

    now = datetime.now()
    text.write("\n%s sec   %s \n" % (result,now))

