import socket
import uuid
import requests
import urllib.request
import os
from datetime import datetime
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileMerger, PdfFileReader
from PIL import Image


def day_month_year():
    now = datetime.now()
    return now.strftime("%d%m%Y")


def get_issuu_url(issuu_url):
    return issuu_url + day_month_year()


def get_uuid(issuu_url):
    request = requests.get(issuu_url)
    if request.status_code != 200:
        return None
    source = request.text
    soup = BeautifulSoup(source, features="html.parser")
    image = soup.find("meta", attrs={'property': 'og:image'})
    link = image['content']
    start = link.find(IMAGE_URL_DOMAIN) + len(IMAGE_URL_DOMAIN)
    end = link.rfind('/jpg/page_1.jpg')
    uuid = link[start:end]
    return uuid


def magazine_as_pdf(uuid):
    magazine = PdfFileMerger()
    index = 1
    last_page = False
    while not last_page:
        filename = 'page_' + str(index)
        img_file = filename + '.jpg'
        img_file_url = IMAGE_URL_DOMAIN + str(uuid) + '/jpg/' + img_file
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
    magazine_pdf = 'adn_' + day_month_year() + '.pdf'
    magazine.write(magazine_pdf)
    return magazine_pdf


MAGAZINE_URL = 'https://issuu.com/diarioadn.co/docs/adn_cali_-_'
IMAGE_URL_DOMAIN = 'https://image.isu.pub/'
socket.setdefaulttimeout(30)
issuu_url = get_issuu_url(MAGAZINE_URL)
uuid = get_uuid(issuu_url)
if uuid is not None:
    print('Analyzing', issuu_url)
    pdf = magazine_as_pdf(uuid)
    print(pdf, 'done!')
else:
    print(issuu_url, 'not found')
