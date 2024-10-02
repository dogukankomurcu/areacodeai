import phonenumbers
from phonenumbers import geocoder

def detect_country_without_country_code(phone_number):
    possible_countries = []

    for region_code in [
        "AT", "AU", "BA", "BE", "BG", "BY", "CA", "CH", "CO", "CY", "CZ", "DE", "DK", "DZ", "EE", 
        "EG", "ES", "FI", "FR", "GB", "GR", "HR", "HU", "IE", "IQ", "IT", "LT", "LU", "LV", "MA", 
        "MD", "ME", "MT", "NL", "NO", "NZ", "PE", "PL", "PT", "QA", "RO", "RS", "RU", "SA", "SE", 
        "TR", "UA"
    ]:      
        
        try:
            parsed_number = phonenumbers.parse(phone_number, region_code)
            if phonenumbers.is_valid_number(parsed_number):
                country_name = geocoder.description_for_number(parsed_number, "en")
                possible_countries.append((country_name, phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)))
        except phonenumbers.phonenumberutil.NumberParseException:
            continue

    return possible_countries if possible_countries else "Ülke tespit edilemedi."

# Örnek kullanım
phone_number = "78604304" # Başında ülke kodu olmayan numara
possible_countries = detect_country_without_country_code(phone_number)

print("Olası ülkeler ve formatlanmış numaralar:")
for country in possible_countries:
    print(f"Ülke: {country[0]}, Formatlı Numara: {country[1]}")



"""
for region_code in [
    "AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AR", "AS", "AT", "AU", "AW", "AX", "AZ",
    "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS",
    "BT", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO",
    "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG",
    "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG",
    "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GT", "GU", "GW", "GY", "HK", "HN", "HR", "HT",
    "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE",
    "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR",
    "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN",
    "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF",
    "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL",
    "PM", "PR", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE",
    "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ",
    "TC", "TD", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TZ", "UA", "UG",
    "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM",
    "ZW"
]: 

"""