from countryinfo import CountryInfo
count=input("Enter country name:")
country=CountryInfo(count)

print("capital is:",country.capital())
print("currencies is:",country.currencies())
print("Language is:",country.languages())
print("borders is:",country.borders())
print("Others name is:",country.alt_spellings())