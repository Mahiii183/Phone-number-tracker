import phonenumbers #Uses the phonenumbers library

number = input("Enter your phone number with the country code :")

from phonenumbers import geocoder #Uses the built in function from phonenumbers
ch_num = phonenumbers.parse(number, "CH") #Finds location of the number, C for country and H for history
print(geocoder.description_for_number(ch_num, "en")) #Displays it in english

from phonenumbers import carrier #Uses the built in function to locate service provider
serv_num = phonenumbers.parse(number, "RO") #Finds the provider
print(carrier.name_for_number(serv_num, "en")) #Displays the service provider's name in english

