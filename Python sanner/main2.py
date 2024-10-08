import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter Mobile Number with Country code : ")
mobileNoo = phonenumbers.parse(mobileNo)

print(timezone.time_zones_for_number(mobileNoo))

print(carrier.name_for_number(mobileNo, "en"))

print(geocoder.description_for_number(mobileNoo, "en"))

print("Valid Mobile Number :", phonenumbers.is_valid_number(mobileNo))

print("Checking possibility of Number :", phonenumbers.is_possible_number(mobileNo))