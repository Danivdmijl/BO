import datetime

print("Hello You!, ik ben Dani")

username = input("Wie ben jij?:")

print("Hello " + username)
x = datetime.datetime.now()

print("De datum en tijd is")
print(x)
#Nog een keer script

while True:
    # main program
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break