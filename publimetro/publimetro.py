from calendar import MONDAY, FRIDAY, WEDNESDAY
import urllib.request
from datetime import datetime
now = datetime.now()
if now.weekday() not in [MONDAY, WEDNESDAY, FRIDAY]:
    print('Publimetro has no edition today')
else:
    pdf_filename = now.strftime('%Y%m%d') + '_cali.pdf'
    main_url = 'https://rm.metrolatam.com/pdf/' + now.strftime('%Y') + '/' + now.strftime('%m') + '/' + now.strftime('%d')
    pdf_url = main_url + '/' + pdf_filename
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    try:
        urllib.request.urlretrieve(pdf_url, pdf_filename)
        print(pdf_filename, 'downloaded')
    except Exception:
        print(pdf_filename, 'not found. Visit https://www.readmetro.com/es/colombia/cali/archive/ to review')
