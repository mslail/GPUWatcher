from enum import Enum

ONLINE_IN_STOCK = 'Online In Stock'
ONLINE_IN_SPECIAL_ORDER = 'Online Special Order'
AVAILABLE_TO_SHIP = 'Available to ship'

class Source(Enum):
     Null = 0 
     CanadaComputers = 1
     BestBuy = 2

class SourceManager:
     source = Source.Null 
     
     def __init__(self, source):
          self.source = source
     
     def validateSource(self, request):
          if self.source == Source.CanadaComputers:
               return ONLINE_IN_STOCK in request.text or ONLINE_IN_SPECIAL_ORDER in request.text
          elif self.source == Source.BestBuy:
               return AVAILABLE_TO_SHIP in request.text
          return False