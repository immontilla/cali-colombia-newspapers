[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

# Colombian newspapers

## ADN Cali

ADN publishes its online version in an embedded reader at https://issuu.com/diarioadn.co/docs/adn_cali_-_{ddmmyyyy} where dd, mm and yyyy depends on the current date. To read this newspaper offline, I built a python script to do so. 

In the embedded reader every page is displayed using an image file. This image is converted to PDF and appended into a unique PDF file using Python.

```bash
pip install -r adn/requeriments.txt
python adn/adn.py
```
