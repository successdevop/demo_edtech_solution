filename = "country_info.txt"

countries = {}

with open(filename) as info:
    info.readline()
    for rows in info:
        data = rows.strip().split("|")
        country, capital, cc, cc3, iac, timezone, currency = data
        country_dict = {
            "name": country,
            "capital": capital,
            "country_code": cc,
            "cc3": cc3,
            "dialing_code": iac,
            "timezone": timezone,
            "currency": currency
        }

        countries[country.casefold()] = country_dict

# print(countries)


print("=="*5 + " Capital city challenge " + "=="*5)
user_country = input("Enter a country: ").casefold()
if user_country in countries:
    print(f"The capital of {user_country.capitalize()} is => {countries[user_country]['capital']}")
else:
    print("Country not found")


# for cty, cty_detail in countries.items():
#     if cty.casefold() == user_country.casefold():
#         print(f"The capital of {cty} is => {countries[cty]['capital']}")
