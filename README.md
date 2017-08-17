# PubMed Fast Search
A graphical user interface that will quickly search the entire PubMed database and return relevant publications along with their abstracts.

### Table of Contents
+ [Introduction](https://github.com/kmoyung/PubMed-FastSearch/blob/master/README.md#introduction)
+ [Installing and Running Python](https://github.com/kmoyung/PubMed-FastSearch/blob/master/README.md#installing-and-running-python)
+ [Quick Start](https://github.com/kmoyung/PubMed-FastSearch/blob/master/README.md#quick-start)
+ [How the Program Works](https://github.com/kmoyung/PubMed-FastSearch/blob/master/README.md#how-the-program-works)
+ [Contact](https://github.com/kmoyung/PubMed-FastSearch/blob/master/README.md#contact)

## Introduction
[PubMed](https://www.ncbi.nlm.nih.gov/pubmed/) is undoubtedly the go-to database for scientific journals, abstracts, and other publications. Those familiar with using the search engine know that it only displays the publication title, along with the authors. But what if you wanted to quickly read through the abstracts of each result? Look no further. PubMed Fast Search enables the user to enter keywords, specific journals, and even search a particular publish year. The program then searches the entire Database, and will generate all relevant publications along with their abstracts. There is even an option to export the search result into a text file for quick references.

## Installing and Running Python
*This section is for those who are unfamiliar and/or have not used Python on their computers. Please skip to [Quick Start](https://github.com/kmoyung/PubMed-FastSearch/blob/master/README.md#quick-start) if you already have Python installed on your computer.*

Python is a powerful programming language that is used widely in many different industries and institutions with its popularity growing every day. The following instructions will help you quickly install Python and start using the PubMed Fast Search right away. 

1. Download and install [Python 3.x.x](https://www.python.org/downloads/). Make sure you're installing Python 3, not 2!
2. Once installed, find where your Python.exe file is located. You will need to know the location of that folder.

![](https://github.com/kmoyung/PubMed-FastSearch/blob/master/images/Finding_Python_Address.PNG)

3. Open your command line (Windows) and enter the following command with your own location to change to the Python directory.

![](https://github.com/kmoyung/PubMed-FastSearch/blob/master/images/Change_Directory.PNG) 

## Quick Start
*This program is only supported on Python 3. It will not work for Python 2.x.*

Below are instructions to help you get started if you are already familiar with Python:

Before you get started, please install [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/):

`python -m pip install beautifulsoup4`

![](https://github.com/kmoyung/PubMed-FastSearch/blob/master/images/Install_BeautifulSoup4.PNG)

We will be using [Tkinter](https://wiki.python.org/moin/TkInter) to launch our GUI. Make sure it's installed or up-to-date (this library is usually pre-installed with Python)

`python -m pip install -update tkinter`

![](https://github.com/kmoyung/PubMed-FastSearch/blob/master/images/Update_Tkinter.PNG)

Run PubMed Fast Search:

`python pubmedfs.py`

![](https://github.com/kmoyung/PubMed-FastSearch/blob/master/images/Run.PNG)

![](https://github.com/kmoyung/PubMed-FastSearch/blob/master/images/GUI.PNG)

If you would like to output your search results to a text file, click the checkbox:

![](https://github.com/kmoyung/PubMed-FastSearch/blob/master/images/Checkbox_Output.PNG)

You will be prompted to name your file and select a location to save it:

![](https://github.com/kmoyung/PubMed-FastSearch/blob/master/images/Save_File.PNG)

## How the Program Works

This program uses the [NCBI E-Utilities (eutils)](https://www.ncbi.nlm.nih.gov/books/NBK25500/) framework to query the PubMed database for relevant articles using a single URL [(see the section about searching here)](https://www.ncbi.nlm.nih.gov/books/NBK25500/#_chapter1_Searching_a_Database_). This Python program takes advantage of the URL search method and, to make it more user-friendly, I've implemented a graphical user interface library [(Tkinter)](https://wiki.python.org/moin/TkInter). The user can input keywords, a specific journal name, and/or publish year. These inputs are then parsed through the script and implemented as a eutils search URL. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) then accesses the search results page that eutils generates and scrapes the PubMed IDs. These PubMed IDs are each accessed using BeautifulSoup again, this time scraping the title, abstract, author(s), and publication info, returning it to the console (or outputting the returned values to a text file).

* * *

### Contact
Kevin Moyung: kevinmoyung@gmail.com
