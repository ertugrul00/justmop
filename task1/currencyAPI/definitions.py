import requests, json

from abc import ABC, abstractmethod

# for keeping data as name, value type => ex: USDTRY': 6.65234.
class ExchangeRate:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return json.dumps((self.name, self.value))

# Provider Interface in general. Provider 1 is already works well with this interface.
class ProviderInterface(ABC):
    @abstractmethod
    def getProviderData(self):
        pass
    @abstractmethod
    def parseProviderData(self, provider1Data):
        pass

# implementing Provider Interface as expected, overrides abstract methods in the interface.
class Provider1(ProviderInterface):
    def __init__(self):
        self.name = "Provider 1"
        self.url = "https://run.mocky.io/v3/e4c58892-3eaa-49e8-a2d4-88ffb0f97c27"
    def getProviderData(self):
        response = requests.get(self.url)
        #print (response.json())
        return response.json()
    def parseProviderData(self, provider1Data):
        temp = provider1Data['data']
        result = []
        for item in temp:
            result.append(ExchangeRate(item['symbol'], item['amount']))
        return result
# This interface is for the second provider (Provider2). It has different functions.
class AnotherProviderInterface(ABC):
    @abstractmethod
    def getThisProviderData(self):
        pass
    @abstractmethod
    def parseThisProviderData(self, provider2Data):
        pass
# Provider2 implements the interface, note that Provider2 can implement use the ProviderInterce 
# since functions are different.
class Provider2(AnotherProviderInterface):
    def __init__(self):
        self.name = "Provider 2"
        self.url = "https://run.mocky.io/v3/cff2fa19-a599-46c7-a83c-c891ba721561"    
    def getThisProviderData(self):
        response = requests.get(self.url)
        #print (response.json())
        return response.json()        
    def parseThisProviderData(self, provider2Data):
        temp = provider2Data['result']
        result = []
        for item in temp:
            result.append(ExchangeRate(item['from'].upper() + item['to'].upper(), item['value']))
        return result        

# Below, I implemented an adapter (works with the ProviderInterface), for the second provider (Provider2).
# Since, It implements the interface, methods are the same as in the ProviderInterface. However,
# in methods, the appropriate calls are made so that provider2 data can be fetched and parsed accordingly.
# By using this adapter, the program can fecth provider2 data like in the provider1 data with the same
# function naming. As a result, Provider2 is adapted to the ProviderInterface.
# Example is below:
#    p1 = Provider1()
#    p2 = Provider2()
#    p2Adapter = AnotherProviderAdapter(p2)
#    data1 = p1.parseProviderData(p1.getProviderData())
#    data2 = p2Adapter.parseProviderData(p2Adapter.getProviderData()) # using same functions in the above line.

class AnotherProviderAdapter(ProviderInterface): 
    def __init__(self, secondProvider):
        self.secondProvider = secondProvider
    def getProviderData(self):
        return self.secondProvider.getThisProviderData() 
    def parseProviderData(self, provider2Data):
        return self.secondProvider.parseThisProviderData(provider2Data)