"""It's a dictionary of currency codes ('AUD' is Australian dollars, 'BGN' is Bulgarian Lev, 'BRL' is Brazilian
Real...) and their exchange rates relative to the Euro.    The rates are example values, not the actual values,
but that doesn't matter here. We'll write a program later in the semester that gets real exchange rate values. Give
me hints but don't write a full solution."""
"""Then, complete this program to calculate conversions between Euros and other currencies.

Ask the user what currency code they would like to convert to.
And, how many Euros they want to convert.

You'll need to get the exchange rate from the dictionary.  If the user enters SEK for Swedish Krona, 
then your program will get 10.8538 from the dictionary.  Store this number in a new variable.

Then, do the math. For example, if the user wants to convert 100 Euros to CAN, Canadian dollars, and the exchange 
rate is 1.3351, then you need to multiply the Euros amount by the exchange rate to get the amount in Canadian Dollars.

So to convert 100 Euros to Canadian dollars, 100 * 1.3351 = 133.51 Canadian dollars.

Display the result to the user.

If the user enters a currency code that is not in the dictionary, print a message telling them that the conversion 
can't be done."""
# keys are the names of currency, and the values are tha conversion rates
rates = {
    'AUD': 1.5311,
    'BGN': 1.9558,
    'BRL': 4.9682,
    'CAD': 1.3351,
    'CHF': 0.9863,
    'CNY': 7.0894,
    'CZK': 24.422,
    'DKK': 7.4419,
    'EUR': 1,
    'GBP': 0.87478,
    'HKD': 7.7493,
    'HRK': 7.5353,
    'HUF': 401.15,
    'IDR': 15491.81,
    'ILS': 3.5065,
    'INR': 81.02,
    'ISK': 145.5,
    'JPY': 145.19,
    'KRW': 1397.7,
    'MXN': 19.2611,
    'MYR': 4.6872,
    'NOK': 10.2019,
    'NZD': 1.6769,
    'PHP': 57.672,
    'PLN': 4.6825,
    'RON': 4.8893,
    'RUB': 86.7666,
    'SEK': 10.8538,
    'SGD': 1.3891,
    'THB': 36.906,
    'TRY': 18.3845,
    'USD': 0.9872,
    'ZAR': 17.7983
}
# ask user which they want to convert
currency_name = input('Enter the currency code to exchange: ')
# check if currency is in the dictionary - hint: if statement probs - got this to work after remembering to re-set
# the variable below in if statement
if currency_name not in rates:
    print('That code is not valid.')
    currency_name = input('Enter the currency code to exchange: ')  # needed to re-enter currency_name with input.
    # otherwise, code would break saying the incorrect input could not be identified

how_many_euros = float(input('Enter how many Euros to convert: ')) # also forgot to global the how_many_euros
# variable - did not break code but had a yellow line beneath it due to it being local to if statement.
# there's a few different way to get variables and info from dictionary, but this way seems/looks most concise
exchange_rate = rates[currency_name]
print(f'The exchange rate is for {currency_name} is {exchange_rate}')
exchanged_currency_amount = how_many_euros * exchange_rate
print(f'The equivalent in {currency_name} currency is {exchanged_currency_amount: .3f}')  # TODO print neat message
# for user - the ': .3f' cuts off 3 decimal points for ease of viewing

# print(exchange_rate)
# jpy_currency_name = 'JPY' # syntax to read values from dictionary
# jpy_exchange_rate = rates[jpy_currency_name]
# examples above how to read from dictionary

# print(jpy_exchange_rate) we want to make this easier for coding - it would be alot fo code otherwise
