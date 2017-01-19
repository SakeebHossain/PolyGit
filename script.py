#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import simplejson as json

def getLanguages(username):
    # dictionary that we use to track language totals
    repo_links = []
    lang_dict = {}
    page_num = 1
    count = 0

    # get the html of the page using requests and parse with bs4
    res = requests.get("https://api.github.com/users/" + username + "/repos")

    # make sure the profile was found by checking if their first repo page exists
    if (res.status_code != 200):
        print("ERROR", res.status_code, ": The profile doesn't exist.")
        return

    # get the links from the json obtained from the GithubAPI
    repos_json = json.loads(res.text)
    for repo in repos_json:
        repo_links.append("https://github.com/" + repo["full_name"])
        count += 1

    # for i in repo_links:
    #     print("DEBUGGING:", i)
    # print(count)

    for link in repo_links:
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        project_langs = soup.find_all('span', class_="lang")
        for lang in project_langs:
            


#getLanguages("kshvmdn") # hi keshav

def getProjectLangs(url):
    langs = []
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    x = soup.find_all('span', class_="lang")

    for i in x:
        print(i.string)

getProjectLangs("https://github.com/MalusGreen/TheRealSurface")
