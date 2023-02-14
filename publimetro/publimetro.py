from datetime import datetime, timedelta
import urllib.request
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--days', type=int, default=0, choices=range(0, 8), help='days ago from today(0) to a week (7)')
args = parser.parse_args()
now = datetime.now() - timedelta(days=args.days)
pdf_filename = now.strftime('%Y%m%d') + '_cali.pdf'
main_url = 'https://rm.metrolatam.com/pdf/' + now.strftime('%Y') + '/' + now.strftime('%m') + '/' + now.strftime('%d')
pdf_url = main_url + '/' + pdf_filename
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
try:
    print('Trying to download', pdf_filename,'...')
    pdf_filename = 'publimetro_' + pdf_filename
    urllib.request.urlretrieve(pdf_url, pdf_filename)
    print(pdf_filename, 'downloaded')
except Exception:
    print(pdf_filename, 'not found. Visit https://www.readmetro.com/es/colombia/cali/archive/ to review')
