# https://www.us-proxy.org/#list
from lxml import html
from lxml.etree import XPath
import csv,os,json
import requests
from ProxyList import ProxyList
import random

proxies = ProxyList().find_online_proxies(size=20, types=['anonymous', 'elite_proxy'])
print(proxies)
