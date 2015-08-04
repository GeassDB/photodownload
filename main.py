# -* - coding: UTF-8 -* -  
from HTMLParser import HTMLParser  
import htmllib,urllib,formatter,string  
import os,sys,time  
import threading  
''''' 
Created on 2015-08-03
@author: GeassDB 
'''  
#建立线程池，并启动线程直到结束  
def parallel(urls):    
    startTime = time.time()  
    threads=[]  
    counts = range(len(urls))  
    for i in counts:  
        t=MyThread(downloadImage,(urls[i],),downloadImage.__name__)  
        threads.append(t)  
    for i in counts:  
        threads[i].start()  
    for i in counts:  
        threads[i].join()  
    print 'use time cost:%s'%(time.time()-startTime)  
  
#自定义线程类  
class MyThread(threading.Thread):  
    def __init__(self,func,args,name=''):  
        threading.Thread.__init__(self)  
        self.name=name  
        self.func=func  
        self.args=args  
    def run(self):  
        apply(self.func,self.args)  
  

#下载图片到本地     
def downloadImage(imageUrl):  
    dir = "./image"  
    try:  
        if not os.path.exists(dir):  
            os.mkdir(dir)  
    except:  
        print "Failed to create directory in %s"%dir  
        exit()  
    image = imageUrl.split('/')[-1]  
    path = dir+"/"+image  
    data = urllib.urlopen(imageUrl).read()  
    f = file(path,"wb")  
    f.write(data)  
    f.close()  
  
#main&生成urls  
if __name__ == "__main__":  
    urls = []  
for a in range(2000,2001):
    for b in range(13,14):
        for c in range(1,21):
            for d in range(1,11):
                for e in range(1,31):
                        url = "http://202.115.139.10/zxs_zp/"+str(a)+"/"+str(a) + str(b).rjust(2,"0") + str(c).rjust(2,"0") + str(d).rjust(2,"0") + str(e).rjust(2,"0")+".jpg"  
                        urls.append(url)  
parallel(urls)   