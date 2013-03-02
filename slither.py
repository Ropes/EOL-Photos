import requests
from BeautifulSoup import BeautifulSoup

EOL_SITE = 'http://eol.jsc.nasa.gov'
MISSION_RESULTS_POST_URL = 'http://eol.jsc.nasa.gov/scripts/sseop/mrf.pl'

STOCK_MISSION_POST_DATA = {'mission':None,
                            'MRFList': None,
                            'frame1': None,
                            'frame2': None,
                            'roll': 'E',
                            'showcldpcb': 'on',
                            'showfcltcb': 'on',
                            'showfeatcb': 'on',
                            'showgeoncb': 'on',
                            'showimagecb': 'on',
                            'showlatcb': 'on',
                            'showloncb': 'on',
                            'showpdatecb': 'on',
                            'showtiltcb': 'on',
                            'sortrb': None,
                            'table': 'images',
                            'what': 'records'}

def post_req(url, payload):
    headers = {}
    return requests.post(url, data=payload, headers=headers)

def parse_results_page(src):
    soup = BeautifulSoup(src)
    table = soup(table)[1]

    

payload = STOCK_MISSION_POST_DATA
payload.update({'mission': 'ISS031'})

'''
print payload
html_data = post_req(MISSION_RESULTS_POST_URL, payload).content
with open('neh.html', 'w') as f:
    html_data = f.write(html_data)
'''

with open('neh.html', 'r') as f:
    html_data = f.read()
    print len(html_data)
    soup = BeautifulSoup(html_data)
    table = soup('table', {'summary': 'This table holds the body information.'})[0]
    center = table('td', {'align': 'left'})[0]('center')[1]
    #all of the rows 
    images = center.findAll('tr')[1:]
    for i in images:
        print i('td')


