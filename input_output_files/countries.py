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

print(countries)

missing_values_box = []
for country_w_m_v in countries:
    each_country = countries[country_w_m_v]
    for key, missing_values in each_country.items():
        if missing_values == "":
            missing_values_box.append(key)
    print(f"{each_country['name']} has these missing values: {', '.join(key for key in missing_values_box)}")
    print()
    missing_values_box.clear()


# for country_no_capital in countries:
#     if not countries[country_no_capital]['capital']:
#         print(f"{country_no_capital} - {countries[country_no_capital]['capital']}")


    # print(country_no_capital)
    # if country_no_capital in countries:
    #     for missing_v in countries[country_no_capital]:
    #         if

# print("==" * 5 + " Capital city challenge " + "==" * 5)
# user_country = input("Enter a country: ").casefold()
# if user_country in countries:
#     print(f"{'The capital of ' + user_country.capitalize() + 'is => ' + countries[user_country]['capital'] if
#     countries[user_country]['capital'] else user_country.capitalize() + ' does not have a capital'}")
#     # print(f"The capital of {user_country.capitalize()} is => {countries[user_country]['capital']}")
# else:
#     print("Country not found")

# for cty, cty_detail in countries.items():
#     if cty.casefold() == user_country.casefold():
#         print(f"The capital of {cty} is => {countries[cty]['capital']}")
