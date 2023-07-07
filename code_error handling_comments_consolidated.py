# exception handling for entire program within try statement
try:
    print("Welcome to our Exchange")

    # amount = float(input("Enter the amount of money you wish to convert: ")) -> error handling needed for input that is not a float
    amount = float(input("Enter the amount of money you wish to convert: "))

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

    # calculation of target amount in target currency
    amount_output = amount * currency_dict[input_currency][output_currency]

    # providing results by repeating input amount and input currency and giving target amount and target currency
    print(amount, input_currency, "is equal to ", amount_output, output_currency)

    print("Thank you for choosing our Exchange Service")

# Exception handling for float input -> if non-float input is entered, error message will appear
except ValueError:
    print("Invalid amount entered. Please enter a valid amount")

# Exception handling for currency input -> only currencies from the dictionary will be accepted as valid
except KeyError:
    print(
        "Error: Unsupported currency. Please enter on the following currencies (USD, EUR, GBP, JPY)"
    )
