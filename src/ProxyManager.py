import requests
import random
from lxml.html import fromstring

class ProxyManager:
    proxies = set()
    def __init__(self):
        self.proxies = self.getProxies()

    def getProxies(self):
        url = 'https://www.us-proxy.org/'
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:20]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                #Grabbing IP and corresponding PORT
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        return proxies

    def getRandomProxy(self):
        if len(self.proxies) == 0:
            print('No proxies available getting new proxies')
            self.getProxies()
        return random.sample(self.proxies, k=1)[0]

    def removeProxy(self, proxy):
        self.proxies.remove(proxy)