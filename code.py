print("Welcome to our Exchange")

amount = float(input("Enter the amount of money you wish to convert: ")) #need type error
input_currency = input("Enter the source currency you have (USD, EUR, GBP, JPY): ").upper() #need value error
output_currency = input("Enter the target currency you need (USD, EUR, GBP, JPY): ").upper() #need value error
currency_dict = {"USD": {"EUR": 0.91, "GBP": 0.78, "JPY": 144.03},
                 "EUR": {"USD": 1.10, "GBP": 0.86, "JPY": 157.90},
                 "GBP": {"USD": 1.27, "EUR": 1.16, "JPY": 183.65},
                 "JPY": {"USD": 0.0069, "EUR": 0.0063, "GBP": 0.0054}}
amount_output = amount*currency_dict[input_currency][output_currency]
print(amount, input_currency,"is equal to " , amount_output, output_currency)
print("Thank you for choosing our Exchange Service")