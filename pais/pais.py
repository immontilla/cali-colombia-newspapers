import urllib.request
from datetime import datetime
now = datetime.now()
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
