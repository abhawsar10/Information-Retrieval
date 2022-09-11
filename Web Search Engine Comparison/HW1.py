from bs4 import BeautifulSoup
import time
from time import sleep
import requests
from random import randint
from html.parser import HTMLParser
from urllib.parse import unquote
import json

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100Safari/537.36'}

class SearchEngine:

    @staticmethod
    def search(query, sleep=True):
            
        print("sleeping...")
        if sleep: # Prevents loading too many pages too soon
            time.sleep(randint(10, 100))
        print("out of sleep")

        temp_url = '+'.join(query.split()) #for adding + between words for the query
        url = 'http://www.search.yahoo.com/search?p=' + temp_url
        url1 = 'http://www.search.yahoo.com/search?p=' + temp_url + "&b=8"
        print(url)

        soup = BeautifulSoup(requests.get(url, headers=USER_AGENT).text,"html.parser")
        soup1 = BeautifulSoup(requests.get(url1, headers=USER_AGENT).text,"html.parser")


        a = SearchEngine.scrape_search_result(soup)
        b = SearchEngine.scrape_search_result(soup1)

        if len(a)==0 or len(b)==0:
            print("yea... youre blocked")

        if len(a)>=10:
            print("a")
            new_results = a
        else:
            print("a+b")
            new_results = a + b


        return new_results[:10]


    @staticmethod
    def scrape_search_result(soup):
        
        raw_results = soup.find_all("a",attrs= {   "class": "d-ib ls-05 fz-20 lh-26 td-hu tc va-bot mxw-100p" } )
        # print(raw_results[0])

        results = []
        #implement a check to get only 10 results and also check that URLs must not be duplicated

        for result in raw_results:
            link = result.get('href')
            # print(link)
        
            try:
                start = link.index("/RU=")
                end = link.index("/RK=")
            except (ValueError):
                continue
            results.append(unquote(link[start+4:end]))

        # print(results)
        return results


def read_qs(fname):

    file1 = open(fname, 'r')
    queries=[]

    while True:
        line = file1.readline()
        if not line:
            break
        queries.append(line[:-2])   #do something about the last space

    file1.close()
    return queries

def run_qs(queries):

    q_dict = {}

    for q in queries:
        print("Q:",q)
        q_dict[q] = SearchEngine.search(q,True)

    with open("my_res.json", "w") as outfile:
        json.dump(q_dict, outfile)


queries = read_qs("100QueriesSet4.txt")
run_qs(queries[:10])