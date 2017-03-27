import sys
import json
import urllib.parse
import requests

valid = True
url=sys.argv[1]
apiKey="AIzaSyA-ZkVp0wt8eBgLFTU22uKxfgmFCHsfx5A"
vurl='https://www.googleapis.com/pagespeedonline/v2/runPagespeed?url='+ urllib.parse.quote_plus(url) +'&filter_third_party_resources=true&locale=it_IT&screenshot=false&key=' + apiKey


response = requests.get(vurl)

x=json.loads(response.text)


print();
print();
print();
print('--------------------------------------')
print('--------------------------------------')
print('  |||' + url + '|||');
print('--------------------------------------')
print('--------------------------------------')
print();
print(x['ruleGroups'])
print();
print();
print();

exit("pagespeedtest url " + url )
