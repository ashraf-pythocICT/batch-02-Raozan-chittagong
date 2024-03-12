exchange_rates = {
    "USD to BDT": 110,
    "AED to BDT": 30,
    "EUR to BDT": 118,
    "CNY to BDT": 15 }


def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount

    conversion_rate = exchange_rates.get(f"{from_currency} to {to_currency}")
    if conversion_rate is None:
        return "Conversion not supported"

    converted_amount = amount * conversion_rate
    return converted_amount

if __name__ == "__main__":
    print("Currency Converter project, batch-2")
    amount = float(input("Enter the amount: "))
    from_currency = input("From Currency (e.g., USD, AED, EUR, CNY): ")
    to_currency = input("To Currency (e.g., BDT): ")

    result = convert_currency(amount, from_currency, to_currency)
    if isinstance(result, str):
        print(result)
    else:
        print(f"{amount} {from_currency} is equivalent to {result:.2f} {to_currency}")
