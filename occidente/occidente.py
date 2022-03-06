from calendar import SUNDAY
import urllib.request
import locale
from datetime import datetime
now = datetime.now()
year = now.strftime('%Y')
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
month_name = now.strftime('%B')
day = now.day
if now.weekday() == SUNDAY:
    day = day - 1
main_url = 'https://occidente.co/wp-content/version-impresa/' + year
pdf_filename = 'diario-pdf-' + str(day) + '-de-' + month_name + '-de-' + year + '.pdf'
pdf_url = main_url + '/' + pdf_filename
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
try:
    urllib.request.urlretrieve(pdf_url, pdf_filename)
    print(pdf_filename, 'downloaded')
except Exception:
    print(pdf_url, 'not found. Visit', main_url, 'to review')
