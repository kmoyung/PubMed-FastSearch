# PubMed Fast Search
A graphical user interface that will quickly search the entire PubMed database and return relevant publications along with their abstracts.

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

* * *

### Contact
Kevin Moyung: kevinmoyung@gmail.com
