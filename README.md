[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

# Colombian newspapers

It is possible to download an old issue of any newspaper using -d as a script argument.

## ADN Cali

ADN publishes its online version in an embedded reader at https://issuu.com/diarioadn.co/docs/adn_cali_-_{ddmmyyyy} where dd, mm and yyyy depends on the current date. To read this newspaper offline, I built a python script to do so. 

In the embedded reader every page is displayed using an image file. This image is converted to PDF and appended into a unique PDF file using Python.

Windows users needs to clone this repo in WSL. Some Python libs like Pillow stop working. Sorry.

```bash
pip install -r adn/requeriments.txt
python adn/adn.py
```

## Diario Occidente

Occidente publishes its online version in https://occidente.co/version-impresa-{yyyy}/ where yyyy is the current year. There is only one edition on weekend.

In some systems, run sudo locale-gen es_ES.UTF-8 could be necessary.

```bash
python occidente/occidente.py
```

## Diario El Pais

This newspaper publishes its online version daily at https://www.elpais.com.co.

```bash
python pais/pais.py
```

## Publimetro

Publimetro publishes its online version on mondays, wednesdays and fridays at https://www.readmetro.com/es/colombia/cali/archive/.

```bash
python publimetro/publimetro.py
```
