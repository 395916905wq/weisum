#coding=utf-8  
import sys    
import requests  
import urllib
import json
import datetime

class xll():
    def get_zhishu(self,name,sdate,edate):
        def get_wid(self):    
            url_name=urllib.quote(name)  
            headers={  
'Host': 'data.weibo.com',  
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0',  
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',  
'Accept-Encoding': 'gzip, deflate',  
'Content-Type': 'application/x-www-form-urlencoded',  
'X-Requested-With': 'XMLHttpRequest',  
'Referer': 'http://data.weibo.com/index/hotword?month=default&wname='+url_name,  
'Cookie': 'UOR=www.baidu.com,data.weibo.com,www.baidu.com; SINAGLOBAL=1213237876483.9214.1464074185942; ULV=1464183246396:2:2:2:3463179069239.6826.1464183246393:1464074185944; DATA=usrmdinst_12; _s_tentry=www.baidu.com; Apache=3463179069239.6826.1464183246393; WBStore=8ca40a3ef06ad7b2|undefined; PHPSESSID=3mn5oie7g3cm954prqan14hbg5',  
'Connection': 'keep-alive'  

}
            url = "http://data.weibo.com/index/ajax/contrast?key2="+url_name+"&key3=&key4=&key5=2016-09-01&key6=2016-09-08&_t=0&__rnd="
            r=requests.get(url,headers=headers)
            q = r.text
            a = json.loads(q)
            w = a['data']['key2']['id']
            return w
        w=str(get_wid(name))
        url_name=urllib.quote(name)
        sdate1=str(sdate)        
        edate1=str(edate)
        headers={  
'Host': 'data.weibo.com',  
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0',  
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',  
'Accept-Encoding': 'gzip, deflate',  
'Content-Type': 'application/x-www-form-urlencoded',  
'X-Requested-With': 'XMLHttpRequest',  
'Referer': 'http://data.weibo.com/index/hotword?month=default&wname='+url_name,  
'Cookie': 'UOR=www.baidu.com,data.weibo.com,www.baidu.com; SINAGLOBAL=1213237876483.9214.1464074185942; ULV=1464183246396:2:2:2:3463179069239.6826.1464183246393:1464074185944; DATA=usrmdinst_12; _s_tentry=www.baidu.com; Apache=3463179069239.6826.1464183246393; WBStore=8ca40a3ef06ad7b2|undefined; PHPSESSID=3mn5oie7g3cm954prqan14hbg5',  
'Connection': 'keep-alive'  

}
        url2 = "http://data.weibo.com/index/ajax/getchartdata?wid="+w+"&sdate="+sdate+"&edate="+edate+"&__rnd="
        y=requests.get(url2,headers=headers)
        t = y.text
        u = json.loads(t)
        i = u['zt'][0]['value']
        o = u['zt'][30]['value']
        n=0
        sum1=0
        while n<31:
            sum1=int(sum1)+int(u['zt'][n]['value'])
            n = n+1
        print i,o
        return sum1
Q=xll()
print Q.get_zhishu("希腊","2015-12-01","2015-12-31")
