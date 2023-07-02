# accessing in-built module that exists when an exception occurs
import sys

print("Welcome to our Exchange")

# amount = float(input("Enter the amount of money you wish to convert: ")) -> error handling needed for input that is not a float
# accepting input without check, error meesage will appear after all three entries are made (if one of them is faulty)
amount = input("Enter the amount of money you wish to convert: ")

input_currency = input(
    "Enter the source currency you have (USD, EUR, GBP, JPY): "
).upper()  # error handling needed for input that is not one of the currencies

output_currency = input(
    "Enter the target currency you need (USD, EUR, GBP, JPY): "
).upper()  # error handling needed for input that is not one of the currencies

# dictionary provides fixed exchange rates for given currencies
currency_dict = {
    "USD": {"EUR": 0.91, "GBP": 0.78, "JPY": 144.03},
    "EUR": {"USD": 1.10, "GBP": 0.86, "JPY": 157.90},
    "GBP": {"USD": 1.27, "EUR": 1.16, "JPY": 183.65},
    "JPY": {"USD": 0.0069, "EUR": 0.0063, "GBP": 0.0054},
}

# Exception handling for float input
# changing input value to float variable and handling exception if value invalid
try:
    amount = float(amount)
except ValueError:
    print("Invalid amount entered. Please enter a valid amount")
    sys.exit(1)

# Exception handling for currency input
# Checking if input and output currencies exist in dict and handling exception if it doesn't
try:
    currency_dict[input_currency][output_currency]
except KeyError:
    print(
        "Error: Unsupported target currency. Please enter on the following currencies (USD, EUR, GBP, JPY)"
    )
    sys.exit(1)  # exit command ends imported sys module

# calculation of target amount in target currency
amount_output = amount * currency_dict[input_currency][output_currency]

# providing results by repeating input amount and input currency and giving target amount and target currency
print(amount, input_currency, "is equal to ", amount_output, output_currency)

print("Thank you for choosing our Exchange Service")
