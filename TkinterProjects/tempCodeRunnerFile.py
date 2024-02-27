import phonenumbers

# Parse the phone number
phone_number = phonenumbers.parse("+918534002139", None)

# Get the country that the phone number belongs to
country = phonenumbers.region_code_for_number(phone_number)

# Get carrier information for the phone number
carrier = "Unknown"
if phonenumbers.is_valid_number(phone_number):
    carrier = phonenumbers.carrier.name_for_number(phone_number, "en")

print("Country:", country)
print("Carrier:", carrier)
