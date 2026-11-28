class CurrencyConverter:
 # Class attribute

    # TODO: Implement the static method `to_usd`
    @staticmethod
    def to_usd(amt, curr):
        rates = {  
            'EUR': 1.20,  # 1 EUR = 1.20 USD
            'JPY': 0.01   # 1 JPY = 0.01 USD
        }
        if curr == 'EUR':
            return amt * rates['EUR']
        if curr == 'JPY':
            return amt * rates['JPY']
    

print(f"100 EUR = {CurrencyConverter.to_usd(100, 'EUR')} USD")     # 120 USD
print(f"100 JPY = {CurrencyConverter.to_usd(100, 'JPY')} USD")     # 1 USD
