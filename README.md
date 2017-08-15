# PubMed Fast Search
A graphical user interface that will quickly search the entire PubMed database and return relevant publications along with their abstracts.

## Introduction
PubMed is undoubtedly the go-to database for scientific journals, abstracts, and other publications. Those familiar with using the search engine know that it only displays the publication title, along with the authors. But what if you wanted to quickly read through the abstracts of each result? Look no further. PubMed Fast Search enables the user to enter keywords, specific journals, and even search a particular publish year. The program then searches the entire Database, and will generate all relevant publications along with their abstracts. There is even an option to export the search result into a text file for quick references.

## Getting Started
*This program is only supported on Python 3. It will not work for Python 2.x.*

Before you begin, please install [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/):

`python -m pip install beautifulsoup4`

We will be using [Tkinter](https://wiki.python.org/moin/TkInter) to launch our GUI. Make sure it's installed or up-to-date (this library is usually pre-installed with Python)

`python -m pip install -update tkinter`

Run PubMed Fast Search:

`python pubmedscrape.py`

*If you select output to text file, the text file will be located in the same directory where you ran pubmedscrape.py*

* * *

### Contact
Kevin Moyung: kevinmoyung@gmail.com
