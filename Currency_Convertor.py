print("Welcome to Currency Convertor")
import requests
def currency_convertor(base,target,amount):
    response=requests.get("https://openexchangerates.org/api/latest.json?app_id=998861d13c2d44ceb37998ac8f558491")
    data=response.json()
    exchange_rates=data['rates']
    if base in exchange_rates and target in exchange_rates:
        try:
            amount=float(amount)
            original_amount = amount / exchange_rates[base]
            converted_amount = original_amount * exchange_rates[target]
            print(amount,base,"=",converted_amount,target)
        except:
            print("Invalid Input")
    else:
        print("Invalid Currency Codes")
        
base=input("Enter the base currency (example:INR): ").upper()
target=input("Enter the target currency (example:USD): ").upper()
amount=input("Enter amount the amount to convert:")
currency_convertor(base,target,amount)