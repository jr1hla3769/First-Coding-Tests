# Show number in currency format
currency = lambda n: f"${n:,.2f}"
# Show number in percent format
percent = lambda n: f"{n:.2%}"

# Test currency function
print(currency(99)) # Expected output: USD 99.00
print(currency(123456789.09876543)) # Expected output: USD 123,456,789.10

# Test percent function 
print(percent(0.065)) # Expected output: 6.50%
print(percent(0.7)) # Expected output: 70.00%

# Path: coding%20projects%201/callao/basic.py

# Test convert_to_eur function
print(convert_to_eur("USD", 100)) # Expected output: 84.75
print(convert_to_eur("GBP", 100)) # Expected output: 116.28

# Use FX rates to convert listed currencies to EUR
exchange_rates = {
    "PEN": 0.26,
    "PYG": 0.00012,
    "BOB": 0.14,

}

exchange_rates = {
    "USD": 1.18,
    "GBP": 0.86,
    "PEN": 4.05,
    "BOB": 8.05,
    "PYG": 7.05,
}

        value_in_eur = amount / rate
        return value_in_eur
def convert_to_eur(currency_code, amount):
    if currency_code in exchange_rates:
        rate = exchange_rates[currency_code]
        value_in_eur = amount / rate
        return value_in_eur
    else:
         return None
    
    # Get user input
    currency_code = input("Enter the currency code:").upper()
    amount = float(input("Enter the amount:"))

# Now convert to EUR
value_in_eur = convert_to_eur(currency_code, amount)

if value_in_eur is not None:
     print(f"{amount} {currency_code} is equal to {value_in_eur:.2f} EUR")
else:
     print("Currency code not found")
     
