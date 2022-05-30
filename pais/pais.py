import urllib.request
from datetime import datetime, timedelta
import urllib.request
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--days', type=int, default=0, choices=range(0, 7), help='days ago up to 6 days')
args = parser.parse_args()
now = datetime.now() - timedelta(days=args.days)
date = now.strftime('%Y%m%d')
pdf_filename = 'elpais_' + date + '.pdf'
pdf_url = 'https://www.elpais.com.co/elpais/servicios/newstand/files/elpais/' + date + '/pdf_complete/' + pdf_filename
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
try:
    print('Downloading', pdf_filename,'...')
    urllib.request.urlretrieve(pdf_url, pdf_filename)
    print(pdf_filename, 'downloaded')
except Exception as ee:
    print('Today edition is not published online yet')
