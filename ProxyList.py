# Author: Gungor Basa
# 06/23/2017
# Proxy Server Scraper ProxyList class

from lxml import html
from lxml.etree import XPath
import csv,os,json
import urllib
import requests
from urllib import request as urlrequest

class ProxyList(object):
    def __proxy_helper(self, size=None):
        url = "https://www.us-proxy.org/#list"
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        page = requests.get(url,headers=headers)
        doc = html.fromstring(page.content)
        XPATH_TABLE = '//*[@id="proxylisttable"]/tbody'
        rows = doc.xpath(XPATH_TABLE)[0].findall("tr")
        if size != None:
            rows = rows[:size]
        return rows

    def find_proxy(self, size=None, types=None):
        rows = self.__proxy_helper(size)
        proxy_list = []
        for row in rows:
            children = row.getchildren()
            secure = "http"
            if children[6].text == 'yes':
                secure = "https"

            if types == None:
                proxy_list.append([secure, children[0].text + ':' + children[1].text])
            elif children[4].text in types:
                proxy_list.append([secure, children[0].text + ':' + children[1].text])
        return proxy_list

    def find_online_proxies(self, size=None, types=None):
        proxies = self.find_proxy(types=types)
        online_proxy_list = []
        i = 1
        for prox in proxies:
            if self.isOnline(prox[1], prox[0]):
                if size != None and i > size:
                    return online_proxy_list
                online_proxy_list.append(prox)
                i+=1
        return online_proxy_list


    def isOnline(self, ip, protocol):
        try:
            url = 'http://www.httpbin.org/ip'
            req = urlrequest.Request(url)
            response = urlrequest.urlopen(req)
            return True
        except Exception:
            return False
