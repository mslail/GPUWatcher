from threading import Thread

from src.RequestManager import RequestManager

URL_3080_EVGA = 'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=181376&fbclid=IwAR2HAIwWfFKxUTl1PVd4ZdsSdxgPVbpXZJJe19cZgcDG_qaKsONO0lI7Ry8'
URL_3080_MSI = 'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=185084&fbclid=IwAR0mNKP-VKEaTJZGhfNiBPf0pEzT15lskUcDMMw44By1steZx6sB83-9O_4'


if __name__ == '__main__':
    canadaComputerEVGARequestManager = RequestManager(URL_3080_EVGA)
    canadaComputerMSIRequestManager = RequestManager(URL_3080_MSI)

    t1 = Thread(target = canadaComputerEVGARequestManager.watch)
    t2 = Thread(target = canadaComputerMSIRequestManager.watch)

    t1.start()
    t2.start()