# Import Libraries
import json

class DataManagment():
    def currencyData(self):
        '''
        This function calls and organize  the currencies data
        from the currencies.json file
        '''
        # Access json currencies json file
        with open("Currencies.json", "r") as read_file:
            currencyData = (json.load(read_file))['currencies']
            # Initialize lists
            countries = []
            currencies = []
            currenciesCountries = []
            countriesCurrencies = []
            # Append currencnyData into countries & currencies list
            for key in currencyData:
                countries.append(key)
                currencies.append(currencyData[key])
                currenciesCountries.append(currencyData[key]+" ("+key+")")
                countriesCurrencies.append(key + " (" + currencyData[key] + ")")
        return countries, \
            currencies, \
            currenciesCountries, \
            countriesCurrencies, \
            currencyData