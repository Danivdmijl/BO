import datetime

print("Hello You!, ik ben Dani")

username = input("Wie ben jij?:")

print("Hello " + username)
x = datetime.datetime.now()

print("De datum en tijd is")
print(x)
#Nog een keer script
print(username + " wil jij dit programma nog een keer doen?")

antwoord = input("Type Y voor ja en N voor nee: ")

print(antwoord)
if antwoord == "N":
    print("Dankjewel")

else:
    print("Begin opnieuw")