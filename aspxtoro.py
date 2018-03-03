# -*- coding: utf-8 -*-

#pip install requests urllib2
#pip install beautifulsoup
#easy_install requests-toolbelt
#pip install contextlib #for aleatority model close session
#pip install time for aleatority model wait
#install requesocks from git --> copiar en usr/lib/python2.7/distpackages/ y ejecutar python setup.py install #tor socks5 to http
#sudo apt-get install python-socksipy #other option to socks5 not working properly yet

#install last version of openssl
#sudo dpkg --remove --force-depends openssl
#./config --prefix=/usr         \
#         --openssldir=/etc/ssl \
#         --libdir=lib          \
#         shared                \
#         zlib-dynamic
#sudo make MANDIR=/usr/share/man MANSUFFIX=ssl install
#sudo install -dv -m755 /usr/share/doc/openssl-1.0.2d #check the version
#sudo cp -vfr doc/*     /usr/share/doc/openssl-1.0.2d

#sudo apt-get install tor deb.torproject.org-keyring
#tor
#export http_proxy='http://localhost:9010'  #the port is on 9010 instead of 9050
#export https_proxy='http://localhost:9010'
#python aspxtoro.py run

#import aleatority
#from contextlib import contextmanager # to close session
#import time # to idle sessions each x ids

#import socks5 to httprequests reckesocks
import requesocks as requests
#import the basis
import urllib2
from requests_toolbelt import SSLAdapter
from bs4 import BeautifulSoup
import re
import ssl
import time
import re
x = 0 #0
for x in range (0, 22131): #range of ids
#let's start the script. for function to select link id with ssl, copy it to Output.csv and print it
	s = requests.session() #ssl session
	s.proxies = {'http': 'socks5://127.0.0.1:9010', #the port is on 9010 instead of 9050
                   'https': 'socks5://127.0.0.1:9010'}
#feching url and get request
#s.mount(url, SSLAdapter(ssl.PROTOCOL_TLSv1)) # ojo al protocolo ssl
	#client / server 	SSLv2 	SSLv3 	SSLv23 	TLSv1 	TLSv1.1 	TLSv1.2
    # SSLv2 			yes 	no  	yes 	no  	no  		no
    # SSLv3 			no  	yes 	yes 	no  	no  		no
    # SSLv23 			no  	yes 	yes 	yes 	yes 		yes
    # TLSv1 			no  	no  	yes 	yes 	no  		no
    # TLSv1.1 			no  	no  	yes 	no  	yes 		no
    # TLSv1.2 			no  	no  	yes 	no  	no  		yes
	x = x + 1
	url = "url=" + str(x) + 'command'
	#r = session.post('https://api.github.com', auth=('user', 'pass'))
	r = s.get(url, verify=False) # <form name="loginform" method="post" action="userinfo.php">
	f = open("Input.csv", "a")		 #append to csv
	f.write('\n'+url+",") #new line url comma
	f.close()	
	print url #print soup.prettify() #see the html
#script to scrap the soup, filter it, copy it in Output.csv and print
	rcontent = r.content.decode('latin1').encode('utf-8')
	rcontent = str(rcontent)
	adv = re.search('div class="advogados".*?b class', rcontent)#tabela do advogado
	if adv != None:
		adv = str(adv.group(0))
		soup = BeautifulSoup(adv)	
		for scrap in soup.find_all('div'):
			strscrap = str(scrap)
			a=re.sub("<span.*?>","",strscrap)#apagando lixo
			stra = str(a)
			b=re.sub("\<div.*?>","",stra)
			strb = str(b)
			c=re.sub("</div>",",",strb)
			strc = str(c)
			d=re.sub("</span>","",strc)
			strd = str(d)
			e=re.sub("<label>",",",strd)
			stre = str(e)
			f=re.sub("</label>",",",stre)
			strf = str(f)
			g=re.sub('<h2>',"",strf)
			strg = str(g)
			h=re.sub('</h2>',",",strg)
			strh = str(h)
			i=re.sub('div',",",strh)
			stri = str(i)
			j=re.sub('active since',',active since',stri)
			strj=str(j)
			k=str(re.sub('ĂÂŁ',"ã",strj)) #tildes y virguilillas 
			k2=str(re.sub('Ã£',"ã",k))
			k3=str(re.sub('Ãª',"ê",k2))
#			k4=str(re.sub('Ãª',"ê",k3))
#			k5=str(re.sub('ĂÂŁ',"ã",k4))k2Ã©
#			k1=str(re.sub(' ',"á",k5))
			k12=str(re.sub('Ã©',"é",k2))
			k13=str(re.sub('ĂÂ',"í",k12))
			k14=str(re.sub('Ã³',"ó",k13))
#			k15=str(re.sub('',"ú",k14))k2Ã©
			m=str(k14)
			filtstrscrap= str(m.join([s for s in m.strip().splitlines(True) if s.strip("\n" or "\r,").strip()]))
			filcode = str(filtstrscrap)
			strm=str(filcode)
			f = open("Input.csv", "a")		 #append to csv to read with excel later
			f.write(strm)
			print strm
	if x % 90 == 0:
		time.sleep(1.5)
f.close()
#except:
 #   pass
#aleatority to avoid machine recognition
#		if x % 30 == 0: #si id múltiplo de 30 entonces hacer un idle time de 1.5s
#			time.sleep(1.5)
#		contextlib.closing(s) #this at the end to close session but then add also the next two
#		s = requests.session() s.proxies = {'http': 'socks5://127.0.0.1:9010',
#		                 'https': 'socks5://127.0.0.1:9010'}
