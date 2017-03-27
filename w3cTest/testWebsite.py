import sys
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup



valid = True
url=sys.argv[1]
vurl='https://validator.w3.org/nu/?doc=' + urllib.parse.quote_plus(url)
x=urllib.request.urlopen(vurl)


soup = BeautifulSoup(x,'html.parser')

result = soup.find("div",{"id" : "results" } )

stmp= False
for each_res in result.findAll("p",{"class" : "success" } ):
	stmp = each_res
	
ftmp= False
for each_res in result.findAll("p",{"class" : "failure" } ):
	ftmp = each_res

if ( ftmp != False ):
	valid = False
	result=ftmp
if ( stmp != False ):
	valid = True
	result=stmp
	

print();
print();
print();
print('--------------------------------------')
print('--------------------------------------')
print('  |||' + url + '|||');
print('--------------------------------------')
print('--------------------------------------')

print();
print(result.contents)
print();
print();
print();
