import time

print("Hallo, welkom bij me beroeps opdracht. \nJe krijgt straks verschillende vragen en elke vraag beinvloed het spel, sommige kunnen je dus af laten gaan. Succes! ")

def vraag1(): 
    vraag1 = input("Je zit thuis en hoort ineens een knal. Wat doe je?  \n  A) Je doet niks en hoopt op het beste. B) Je vlucht en bent van plan naar nederland te gaan. ") 
    if vraag1.lower() == "b":
        vraag2()
    elif vraag1.lower() == "a":
        print("Je bent meteen ontploft je bent af probeer het opnieuw.")
        vraag1

def vraag2():
    vraag2 = input("Alright we gaan naar Nederland. Je pakt je spullen en bent van plan te gaan. Maar hoe ga je er heen?\nA) Met de boot  B) Lopend en proberen te mee liften met mensen. ")
    if vraag2.lower() == "a":
        vraag3()
    elif vraag2.lower() == "b":
        vraag4()

def vraag4():
    vraag4 = input("Een auto stopt en wilt je helpen over de grens. Hij stelt je eerst een vraag en dat bepaalt of je mee mag of niet. De vraag is: is het friet of patat. A) Friet B) Patat")
    if vraag4.lower() == "a":
        vraag8()
    elif vraag4.lower() == "b":
        vraag15()

def vraag3():
    vraag3 = input("d")
    if vraag3.lower() == "a":
        vraag5()
    elif vraag3.lower() == "b":
        vraag5()

def vraag5():
    vraag5 = input("Interesant!\nWaar ben je van plan te wonen? A) Noord-Holland B) Zuid-Holland")
    if vraag5.lower() == "a":
        vraag6()
    elif vraag5.lower() == "b":
        vraag6()

def vraag6():
    vraag6 = input("Ahh oke!\nEr komen flinken golven met tegen wind. Blijf je door varen op de hoop dat je het nog red of blijf je drijven terwijl je terug drijft A) Door varen B) Drijven")
    if vraag6.lower() == "a":
        vraag7()
    elif vraag6.lower() == "b":
        vraag7()

def vraag7():
    vraag7 = input("Je bent veilig in nederland aangekomen. Bedank je de bestuurder?\n A) Ja B) Nee")
    if vraag7.lower() == "a":
        print("Dat is netjes, hij geeft je 50% korting!\nJe word gewaardeerd in nederland. Je hebt je droom baan en woont op de plek waar je wou!\n Je hebt het gehaald!")
    elif vraag7.lower() == "b":
        print("Dat is niet zo netjes.. Hij wou je korting  geven maar die kan je nu vergeten\nJe word gewaardeerd in nederland. Je hebt je droom baan en woont op de plek waar je wou!\n\n Gefeliciteerd je hebt het gehaald!")

def vraag8():
    vraag8 = input("De helper is hier totaal NIET blij mee.. Hij besluit je te ontvoeren. Werk je mee of stribel je tegen? \nA) Je werkt mee B) Je stribelt tegen")
    if vraag8.lower() == "a":
        print("Goede keus, hij slaat je in de boeie en doet een blindoek om.")
        vraag9()
    elif vraag8.lower() == "b":
        print("Je bent veel te vervelend en hij slaat je KO, zet je in het voertuig en gaat er vandoor.")
        vraag9()

def vraag9():
    vraag9 = input("Je zit op een stoel. En de ontvoerder komt naar je toe. Hij begint je te ondervragen waarom je friet koos.. A) Je zegt: Het is toch gwn friet?.. B) Je zegt dat je  z.s.m antwood wou geven waardoor je maar wat zij")
    if vraag9.lower() == "a":
        vraag10()
    elif vraag9.lower() == "b":
        vraag10()

def vraag10():
    vraag10 = input ("Je had gwn patat moeten zeggen Ik geef je de keus uit 2  items.. We gaan vechten wat kies je? A) Een Walther P99 B) Een Knuppel")
    if vraag10.lower() == "a":
        vraag11()
    elif vraag10.lower() == "b":
        vraag12()

def vraag12():
    vraag12 = input("Je gaat hem proberen te slaan waar sla je? A) Hoofd B) Been")
    if vraag12.lower() == "a" "b":
        vraag14()

def vraag11():
    vraag11 = input ("Je krijgt het wapen in je handen en wilt hem schieten. Waar schiet je? A) Been B) Hoofd")
    if vraag11.lower() == "a" "b":
        vraag13()

def vraag13():
    vraag13 = input ("Er zaten geen kogels in het wapen.. Hij komt op je af wat doe je? A) Je gooit het wapen naar hem toe B) Je doet alsof er een kogel in zit")
    if vraag13.lower() == "a":
        print("Je mist\nHij gaat het gevecht met je aan en wint.. Je bent af, probeer het opnieuw!")
        time.sleep(1)
        vraag1
    elif vraag13.lower() == "b":
        print("Hij is niet gek hij heeft de kogels er zelf uit gehaald..\nHij gaat het gevecht met je aan en wint..\nJe bent af, probeer het opnieuw!")
        time.sleep(1) 
        vraag1

def vraag14():
    vraag14 = input("Je houte knuppel breekt door 2e das balen. Wat doe je nu? A) Je gooit het kleine deel B) Je probeert met een kleine helft over door te vechten.")
    if vraag14.lower() == "a":
        print("Je mist.. Hij gaat het gevecht met je aan en wint.\n Je hebt verloren probeer het opnieuw!")
        time.sleep(1)
        vraag1
    elif vraag14.lower() == "b":
        print("Je was verbaast toen je knuppel brak. De overvaller was er snel bij en pakte de knuppel af\nHij gaat het gevecht met je aan en wint..\nJe hebt verloren probeert het opnieuw!")
        time.sleep(1)
        vraag1

def vraag15():
    vraag15 = input ("De helper vond dat het goede antwoord en wilt je meenemen de grens over.\nNa wat gesprekken gaat het over je toekomst in nederland. Wat wil je later worden? A) Software Developer B) 2D Designer")
    if vraag15.lower() == "a" "b":
        vraag16()

def vraag16():
    vraag16 = input("Goede keus zegt ie, maar waar ben je van plan te wonen? A) Zuid Holland B) Noord Holland")
    if vraag16.lower() == "a" "b":
        vraag17()

def vraag17():
    vraag17 = input("Heb je nog Hobby's A) Vissen B) Muziek")
    if vraag17.lower() == "a":
        vraag18()
    elif vraag17.lower() == "b":
        vraag19()

def vraag18():
    vraag18 = input("Vis je op roof vis of van alles? A) Roof B) van alles")
    if vraag18.lower() == "a" "b":
        vraag20()

def vraag19():
    vraag19 = input("leuk luister je er alleen naar of speel je ook zelf? A) Luisteren B) Zelf")
    if vraag19.lower() == "a" "b":
        vraag20()

def vraag20():
    vraag20 = input("Interesant en leuk! Ga je dit ook doen in nederand? A) Ja B) Nee") 
    if vraag20.lower() == "a":
        print("Ah oke, je bent veilig afgezet en de helper wenst je veel succes!\nJe hebt het gehaald gefeliciteerd!")
    elif vraag20.lower() == "b":
        vraag21()

def vraag21():
    vraag21 = input("Oh, hoezo niet ga je het niet missen? A) Helaas wel B) Nee hoor")
    if vraag21.lower() == "a" "b":
        print("Ah oke, je bent veilig afgezet en de helper wenst je veel succes!")

vraag1()