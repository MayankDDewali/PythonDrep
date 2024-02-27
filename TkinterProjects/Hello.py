import phonenumbers
from phonenumbers import carrier,timezone,geocoder

number=input("Enter your number with + : ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
sim_name = carrier.name_for_number(phone,"en")
regin = geocoder.description_for_number(phone,"en")
print("time_zone: ", time)
print("Sim_name: ",sim_name)
print("regin: ",regin)