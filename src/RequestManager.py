import requests

from src.ProxyManager import ProxyManager
from src.Notifications import Notifications
from src.Source import Source, SourceManager

class RequestManager:
    url = ''
    keyword = ''
    request = None
    proxyManager = ProxyManager()
    notications = Notifications()
    sourceManager = SourceManager(Source.Null)

    def __init__(self, url, source):
        self.url = url
        self.sourceManager.source = source
        
    def makeRequestWithProxy(self, url, proxy):
        try:
            request = requests.get(url, proxies= {'http':'http://' + proxy})
            if (request.status_code != 200):
                print('Error: Invalid status code')
                return False
            self.request = request
            return True
        except:
            print('Removing proxy: ' + proxy)
            self.proxyManager.removeProxy(proxy)
        return False

    def validateRequest(self):
        proxy = self.proxyManager.getRandomProxy()
        isRequestValid = self.makeRequestWithProxy(self.url, proxy)

        if (not isRequestValid):
            print('Invalid request')
            return
            
        if (self.sourceManager.validateSource(self.request)):
            print('Found one in stock for url: ' + self.url)
            self.notications.sendEmail(self.url)
            self.notications.openBrowser(self.url)
            self.notications.playSound()
        else: 
            print('No stock for url: ' + self.url)