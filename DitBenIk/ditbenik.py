import datetime

print("Hello You!, ik ben Dani")

username = input("Wie ben jij?:")

print("Hello " + username)
x = datetime.datetime.now()

print("De datum en tijd is")
print(x)

#3vragen
print("Je gaat nu 3 vragen krijgen over mij.")

print("In welke stad woon ik?")

antwoord2 = input("A = Alkmaar B = Amsterdam C = Utrecht :")

print(antwoord2)
if antwoord2 == "A":
    print("Dat is goed!")

elif antwoord2 == "B":
    print("Dat is fout :(")

elif antwoord2 == "C":
    print("Zucht.. dat is al helemaal fout")

#3vragen2
print("Hoe oud ben ik?")

antwoord3 = input("A = 16 B = 17 C = 18 :")

print(antwoord3)
if antwoord3 == "A":
    print("Dat is fout")

elif antwoord3 == "B":
    print("Dat is helemaal goed")

elif antwoord3 == "C":
    print("Was het maar zoon feest, helaas dat is fout")

#3vragen3
print("Welke opleiding heb ik hier voor gedaan")

antwoord4 = input("A = HBR B = MVI C = ZWL :")

print(antwoord4)
if antwoord4 == "A":
    print("Nope niet goed")

elif antwoord4 == "B":
    print("Helemaal correct")

elif antwoord4 == "C":
    print("Nee gewoon niet helemaal fout weer dit")

#Nog een keer script
print(username + " wil jij dit programma nog een keer doen?")

antwoord = input("Type Y voor ja en N voor nee: ")

print(antwoord)
if antwoord == "N":
    print("Dankjewel")

elif antwoord == "Y":
    print("Begin opnieuw")