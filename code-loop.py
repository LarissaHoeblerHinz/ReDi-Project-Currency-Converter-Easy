print("Welcome to our Exchange")
# starting loop that allows user to correct invalid entries before moving on to the next question
while True:
    try:
        # amount = float(input("Enter the amount of money you wish to convert: ")) -> error handling needed for input that is not a float
        amount = float(input("Enter the amount of money you wish to convert: "))
        break
    except ValueError:
        # error handling for occurence of non-float input
        print("Invalid input. Please enter a valid amount.")
while True:
    input_currency = input(
        "Enter the source currency you have (USD, EUR, GBP, JPY): "
    ).upper()
    # error handling for input that is not one of the currencies
    if input_currency in ["USD", "EUR", "GBP", "JPY"]:
        break
    else:
        print("Invalid input. Please enter a valid source currency.")
while True:
    output_currency = input(
        "Enter the target currency you need (USD, EUR, GBP, JPY): "
    ).upper()
    # error handling for input that is not one of the currencies
    if output_currency in ["USD", "EUR", "GBP", "JPY"]:
        break
    else:
        print("Invalid input. Please enter a valid target currency.")

# dictionary provides fixed exchange rates for given currencies
currency_dict = {
    "USD": {"EUR": 0.91, "GBP": 0.78, "JPY": 144.03},
    "EUR": {"USD": 1.10, "GBP": 0.86, "JPY": 157.90},
    "GBP": {"USD": 1.27, "EUR": 1.16, "JPY": 183.65},
    "JPY": {"USD": 0.0069, "EUR": 0.0063, "GBP": 0.0054},
}

if input_currency == output_currency:
    amount_output = amount
else:
    try:
        # calculation of target amount in target currency
        amount_output = amount * currency_dict[input_currency][output_currency]

    # Exception handling for currency input -> only currencies from the dictionary will be accepted as valid
    except KeyError:
        print("Conversion rate not available for the specified currencies.")
        exit()

# providing results by repeating input amount and input currency and giving target amount and target currency
print(amount, input_currency, "is equal to", amount_output, output_currency)
print("Thank you for choosing our Exchange Service")
