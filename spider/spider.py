import sys
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

todo_filename='todofile'
done_filename='donefile'
fof_filename='fof'

with open(todo_filename,'r') as f:
	url=f.readline()
	text=f.read();
	o = urlparse(url)
	baseurl = o.scheme + '://' + o.netloc

done_file = open(todo_filename,'w')
text=text.replace(url,'')
done_file.write(text );
done_file.close();


fourohfour=False

try : 
	x=urllib.request.urlopen(url)
except :
	fourohfour = True


if (not fourohfour) :
	done_file = open(done_filename,'a')
	done_file.write(url );
	done_file.close();

	done_file = open(done_filename,'r')
	donelinks = done_file.read();
	done_file.close();


	soup = BeautifulSoup(x,'html.parser')


	locallinks = []

	for link in soup.findAll("a" , href=True):
		locallink = False
		href = link['href']
		if( donelinks.find(href) != -1 ) :
			pass
		elif( href.find('http') != -1 ) :
			if( href.find(baseurl) != -1 ) :
				locallink =  href 
		elif( href[:1] == '/' ):
			locallink =  baseurl+ href 
		elif( len(href) == 0 ):
			pass
		elif( href[:1] != '#' ):
			locallink =  href 
		if (locallink != False) :
			locallinks.append(locallink)
		

		
	locallinks = (list(set(locallinks)))
	


	todo_file = open(todo_filename,'a')

	for l in locallinks : 
		todo_file.write(l + '\n');
	todo_file.close();
		
	exit(url + " spidered" );
else :
	

	fof_file = open(fof_filename,'a')

	fof_file.write(url + '\n');
	fof_file.close();
	exit(url + " 404'd" );









