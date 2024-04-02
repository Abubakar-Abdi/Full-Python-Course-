import requests
#api ... application programming interface
#exchangerate.com
class currency_converter:
    def __init__(self, url):
        self.data=requests.get(url).json()
        self.currencies=self.data["rates"]
    def convert(self, base_currency,target_currency,amount):
        initial_amount=amount
        amount=(amount/self.currencies[base_currency])
        amount=round(amount*self.currencies[target_currency],2)
        return amount

url="https://open.er-api.com/v6/latest/USD"
obje=currency_converter(url)
#print(obje.data)
#print(obje.currencies)
print(obje.convert("EUR","BDT",100))
