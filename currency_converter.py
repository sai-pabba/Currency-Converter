import requests

def get_conversion_rate(from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?amount=1&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch exchange rates.")
        return None
    
    data = response.json()
    rate = data['rates'][to_currency]
    return rate

def convert_currency(amount, from_currency, to_currency):
    rate = get_conversion_rate(from_currency, to_currency)
    if rate:
        converted = amount * rate
        return converted
    else:
        return None

# Main Function
def main():
    print("Welcome to Currency Converter")
    amount = float(input("Enter amount to convert: "))
    from_currency = input("From Currency (e.g., USD, INR, EUR): ").upper()
    to_currency = input("To Currency: ").upper()
    
    result = convert_currency(amount, from_currency, to_currency)
    
    if result:
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()
