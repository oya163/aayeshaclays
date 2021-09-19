import iso3166

def get_country_codes():
    country_codes = []
    for k, v in iso3166.countries_by_alpha3.items():
        country_codes.append((k, v.name))
    return country_codes