import socket
import requests
import urllib.request
import os
from datetime import datetime
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileMerger, PdfFileReader
from PIL import Image
from datetime import datetime, timedelta
import urllib.request
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--days', type=int, default=0, choices=range(0, 8), help='days ago from today(0) to a week (7)')
args = parser.parse_args()

def day_month_year(pattern):
    now = datetime.now() - timedelta(days=args.days)
    return now.strftime(pattern)


def magazine_urls():
    names = ['adn-cali-','adn_cali_-_', 'adn_cali_']
    patterns = ['%d%m%Y', '%Y%m%d']
    urls = []
    for name in names:
        for pattern in patterns:
            urls.append(MAGAZINE_URL + name + day_month_year(pattern))
    return urls


def get_source():
    magazine_url = None
    urls = magazine_urls()
    for url in urls:
        print('Trying to get', url, '...')
        try:
            request = requests.get(url)
            if request.status_code == 200:
                magazine_url = url
                break
        except Exception:
            pass
    if magazine_url is None:
        return None
    return request.text


def images_magazine_url():
    source = get_source()
    if source is None:
        return None
    soup = BeautifulSoup(source, features="html.parser")
    image = soup.find("meta", attrs={'property': 'og:image'})
    link = image['content']
    start = link.find(IMAGE_URL_DOMAIN) + len(IMAGE_URL_DOMAIN)
    end = link.rfind('/jpg/page_1.jpg')
    uuid = link[start:end]
    return IMAGE_URL_DOMAIN + str(uuid) + '/jpg/'


def magazine_as_pdf(url):
    magazine = PdfFileMerger()
    index = 1
    last_page = False
    while not last_page:
        filename = 'page_' + str(index)
        img_file = filename + '.jpg'
        img_file_url = url + img_file
        try:
            urllib.request.urlretrieve(img_file_url, img_file)
            image = Image.open(img_file)
            pdf_file = filename + '.pdf'
            image.save(pdf_file)
            os.remove(img_file)
            magazine.append(PdfFileReader(pdf_file, 'rb'))
            os.remove(pdf_file)
            print('Appending page ', str(index))
            index += 1
        except Exception:
            last_page = True
    magazine_pdf = 'adn_' + day_month_year("%Y_%m_%d") + '.pdf'
    magazine.write(magazine_pdf)
    return magazine_pdf


MAGAZINE_URL = 'https://issuu.com/diarioadn.co/docs/'
IMAGE_URL_DOMAIN = 'https://image.isu.pub/'
socket.setdefaulttimeout(30)
images_magazine_url = images_magazine_url()
if images_magazine_url is not None:
    pdf = magazine_as_pdf(images_magazine_url)
    print(pdf, 'done!')
else:
    print('Today edition is not published online yet')
