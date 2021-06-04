import time

from src.RequestManager import RequestManager
from src.Source import Source
from src.urls import CANADA_COMPUTER_URLS

TIMEOUT_SECONDS = 240

if __name__ == '__main__':
    canadaComputerRequestManager = RequestManager('', Source.CanadaComputers)
    while True:
        for url in CANADA_COMPUTER_URLS:
            canadaComputerRequestManager.url = url
            canadaComputerRequestManager.validateRequest()
        print('Sleeping for ' + str(TIMEOUT_SECONDS) + ' seconds ...' )
        time.sleep(TIMEOUT_SECONDS)

