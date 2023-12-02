# At first we install bardapi       (pip install bardapi)

# Importing
from bardapi import BardCookies

# Installing datetime module        (pip install datetime)
import datetime

# Making dictonary that will get the cookies
cookie_dict = {
    "__Secure-1PSID" : "dAg6UbztMP6TNx4q6AtMRBVRfrJZaVVDR5tx2o4phawsCusNe-lrCQG9tc5M7wZvym6wZA.",
    "__Secure-1PSIDTS" : "sidts-CjIBPVxjSrU12Un8Gf5yJGfFYXc_WeTLWgDwtuIQH968q5XOc4aApERhcdGbG6lzqk80EBAA",
    "__Secure-1PSIDCC" : "ACA-OxMV8Pgv6Tj3vg4ueRgJDsmOW2V2xtL2IOKFiz4e4IRSUBOyVnXgaduJPERt-ho4O5KNkDgy"
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    Query = input("Enter your Querry: ")
    Reply = bard.get_answer(Query)['content']
    print(Reply)