# PubMed Fast Search v1.0
# Author: Kevin Moyung
# Contact: kevinmoyung@gmail.com
# Acknowledgements: PubMed, BeautifulSoup4, Python

from bs4 import BeautifulSoup
import requests
import tkinter
from tkinter import *
import sys

# GUI
top = tkinter.Tk()
top.title("PubMed Fast Search")
top.geometry("400x400")

orig_stdout = sys.stdout

# Error message used to prompt any errors in searching
Error = Label(top, text = "")

# Output error message
OutputConfirm = Label(top, fg = 'blue')

# Used to indicate whether or not the output checkbox is checked
outputon = IntVar()

def search():

    # Take keywords, journal, pdate input from GUI
    keywords = E1.get()
    journal = E2.get()
    pdate = E3.get()

    # Output results to a file if checkbox is checked
    if outputon.get() == 1:
        outputtext(keywords, journal, pdate)
    else:
        # Refresh the output message from last search
        OutputConfirm.config(text="")

    # Set search result url as a list for parsing
    resulturl = []

    keywords = keywords.replace(" ", "+")

    # Check if user entered keywords
    if keywords is "":
        Error.config(text= "You must enter at least one keyword!", fg = "red")
        #error = Label(top, text = "You must enter at least one keyword! ", fg = "red")
        #error.pack()
        raise Exception("Re-enter keywords")
    else:
        keywords = "+AND+" + keywords

    # Check if user entered a journal name
    if journal is "":
        journal = ""
    else:
        journal = journal + "[journal]+"

    # Check if user entered a publish year
    if pdate is "":
        pdate = ""
    else:
        pdate = "+AND+" + pdate + "[pdat]"

    # Set search url for eutils based on user input
    searchurl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=" + journal + keywords + \
                pdate

    # Request pubmed search result page
    page = requests.get(searchurl)

    # Parse result page using BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')

    # Select pubmed IDs
    idlist = soup.select("id")

    # Append pubmed IDs to resulturl list
    for item in idlist:
        item = "https://www.ncbi.nlm.nih.gov/pubmed/" + item.get_text()
        resulturl.append(item)

    # Iterate through pubmed IDs to scrape article title and abstracts (if available)
    for urlitem in resulturl:
        articlepage = requests.get(urlitem)
        articlesoup = BeautifulSoup(articlepage.content, 'html.parser')

        # Get the article title
        title = articlesoup.find_all("h1")
        title = title[1].get_text()

        # Get the journal name/publish date
        for date in articlesoup.select('div.cit'):
            jnamedate = date.get_text()

        # Get the abstract
        abstract = articlesoup.find("abstracttext")
        if abstract is not None:
            abstract = abstract.get_text()

        # Print the current title
        print(title)

        # Print journal name and publish date
        print(jnamedate)

        # Loop to print out all the authors
        authorlist = ""
        for link in articlesoup.select('div.auths a'):
            author = link.get_text()
            authorlist += author + ", "

        # Removes the extra comma of the author list
        authorlist = authorlist[:-2]

        # Print the current list of authors
        print(authorlist)
        # Print the abstract, if it exists
        print(abstract)
        # Print the Pubmed URL
        print(urlitem)
        # Add a line between results
        print(" ")

    Error.config(text = "Search completed successfully.", fg = "green")

    if outputon.get() == 1:
        outputmessage = "Search results have been exported as " + E1.get() + "-" + E2.get() + "-" + E3.get() + ".txt"
        OutputConfirm.config(text= outputmessage, fg = "blue")

    # Ensures stdout returns back to console after each search
    sys.stdout.close()
    sys.stdout = orig_stdout

# Function that saves output as text file
def outputtext(keywd, jrnl, pdt):
    filename = keywd + '-' + jrnl + '-' + pdt + '.txt'
    sys.stdout = open(filename, 'w')

# Keyword form
L1 = Label(top, text = "Keywords (separate using spaces)")
L1.pack(pady = 5)
E1 = Entry(top, bd = 5)

E1.pack(pady = 5)

# Journal form
L2 = Label(top, text = "Journal Name (optional)")
L2.pack(pady = 5)
E2 = Entry(top, bd = 5)

E2.pack(pady = 5)

# Publish year form
L3 = Label(top, text = "Publish Year (optional)")
L3.pack(pady = 5)
E3 = Entry(top, bd = 5)

E3.pack(pady = 5)

# Submit button
submitbutton = Button(top, text = "Search", command = search)
submitbutton.pack(pady = 10)

# Output to file checkbox
outputcheck = Checkbutton(top, text = "Check here to output search results to a .txt file", variable = outputon,
                          onvalue = 1, offvalue = 0)
outputcheck.pack()

Error.pack()

OutputConfirm.pack()

top.mainloop()
