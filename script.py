#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import simplejson

def getLanguages(url):
    # dictionary that we use to track language totals
    repos = []
    lang_dict = {}
    page_num = 1

    # get the html of the page using requests and parse with bs4
    res = requests.get(url + "?page=" + str(page_num) + "&tab=repositories")

    # make sure the profile was found by checking if their first repo page exists
    if (res.status_code != 200):
        print("ERROR", res.status_code, ": The profile doesn't exist.")
        return

    # go to repositories and get the link to every repo. Then add it to "repos" list
    while (res.status_code == 200):
        soup = BeautifulSoup(res.text, 'html.parser')


        # download each page of the next page
        repo_list_page = url + "?page=" + str(page_num) + "&tab=repositories"
        res = requests.get(repo_list_page)

        q = soup.find_all("div ", class_ = 'd-inline-block mb-1')

        for tag in q:
            s = tag.find_all("a")
            print(s)

        page_num += 1



    # # get the url to the repo list from the given url


    # go to each repo in the repo list and grab the correct languages

# start up

getLanguages("https://github.com/SakeebHossain")