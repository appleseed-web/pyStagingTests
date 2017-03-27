import sys
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup



valid = True
url=sys.argv[1]
x=urllib.request.urlopen(url)


soup = BeautifulSoup(x,'html.parser')

print();
print();
print();
print('--------------------------------------')
print('--------------------------------------')
print('  |||' + url + '|||');
print('--------------------------------------')
print('--------------------------------------')
print();

for each_res in soup.findAll("img" ):
	alt=each_res['alt']
	if ( len(alt) == 0 ) :
		print(each_res['src']);
		
print();
print();
print();

	
