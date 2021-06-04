from enum import Enum

KEY_WORD = 'Online In Stock'
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
               return KEY_WORD in request.text
          elif self.source == Source.BestBuy:
               return AVAILABLE_TO_SHIP in request.text
          return False