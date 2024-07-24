import requests

API_KEY = 'your_api_key'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

def get_exchange_rate(base_currency):
    response = requests.get(BASE_URL + base_currency)
    if response.status_code != 200:
        print(f"Error fetching data from API: {response.status_code}")
        print(response.text)
        raise Exception("Error fetching data from API")
    data = response.json()
    if 'conversion_rates' not in data:
        print("Error: 'conversion_rates' not found in API response")
        raise Exception("Error: invalid API response")
    return data['conversion_rates']

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency != 'USD':
        amount = amount / rates[from_currency]
    return amount * rates[to_currency]

def main():
    base_currency = 'USD'
    try:
        rates = get_exchange_rate(base_currency)
    except Exception as e:
        print(e)
        input("Press Enter to close the console.")
        return

    print("Available currencies: ", ', '.join(rates.keys()))
    from_currency = input("Enter the currency you want to convert from: ").upper()
    to_currency = input("Enter the currency you want to convert to: ").upper()

    if from_currency not in rates:
        print(f"Error: Currency {from_currency} is not available.")
        input("Press Enter to close the console.")
        return

    if to_currency not in rates:
        print(f"Error: Currency {to_currency} is not available.")
        input("Press Enter to close the console.")
        return

    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Error: Please enter a valid numeric value for the amount.")
        input("Press Enter to close the console.")
        return

    result = convert_currency(amount, from_currency, to_currency, rates)
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    input("Press Enter to close the console.")

if __name__ == "__main__":
    main()
