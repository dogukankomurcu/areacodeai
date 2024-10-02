from flask import Flask, request, render_template
import phonenumbers
from phonenumbers import geocoder
import os

app = Flask(__name__)

# Telefon numarasını işleyen fonksiyon
def detect_country_without_country_code(phone_number):
    possible_countries = []
    for region_code in [
        "AD", "AL", "AT", "AZ", "BA", "BE", "BG", "BH", "CA", "CH", "CZ", "DE", "DK",
        "EE", "ES", "FI", "FO", "FR", "GB", "GG", "GI", "GR", "HR", "HU", "IE", "IM",
        "IS", "IT", "JE", "KW", "LI", "LT", "LU", "LV", "MA", "MC", "MD", "ME", "MK",
        "NL", "NO", "OM", "PL", "PT", "QA", "RO", "RS", "RU", "SE", "SI", "SJ", "SK",
        "SM", "US", "XK"

    ]:
        try:
            parsed_number = phonenumbers.parse(phone_number, region_code)
            if phonenumbers.is_valid_number(parsed_number):
                country_name = geocoder.description_for_number(parsed_number, "en")
                possible_countries.append((country_name, phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)))
        except phonenumbers.phonenumberutil.NumberParseException:
            continue

    return possible_countries if possible_countries else None

# Anasayfa rotası
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        possible_countries = detect_country_without_country_code(phone_number)
        return render_template('result.html', phone_number=phone_number, possible_countries=possible_countries)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=False)

