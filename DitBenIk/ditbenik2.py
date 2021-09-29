import time 
import datetime

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
ja = ["J", "j", "Ja"]
nee = ["N", "n", "nee"]

required = ("\nGebruikt graag alleen A, B, of C\n") 

print("Hello You!, ik ben Dani")

username = input("Wie ben jij?:")

print("Hello " + username)
x = datetime.datetime.now()

print("De datum en tijd is")
print(x)

time.sleep(1)
print("Je gaat nu 3 vragen krijgen!")

time.sleep(1)
def intro():
  print ("Het is een maandag ochtend. Je moet vroeg naar school en je wekker gaat af. Je hebt alleen echt geen zin om wakker te worden. Snooze jij je wekker of sta je toch op.  Wat doe je? :")
  time.sleep(1)
  print ("""  A. Wakker worden
  B. Snooze voor 5 minuten
  C. Je wekker gewoon uit zetten omdat je geen zin heb in school""")
  choice = input(">>> ") 
  if choice in answer_A:
    option_wakker()
  elif choice in answer_B:
    print ("\nJe hebt je verslapen, dat is vervelend.. "
    "\n\nJe bent af!")
  elif choice in answer_C:
    option_uit()
  else:
    print (required)
    intro()

def option_wakker(): 
  print ("\nJe word wakker en moet kiezen, ga je met de bus fiets of benewagen naar het station. "
  "Wat doe je:")
  time.sleep(1)
  print ("""  A. Bus
  B. Fiets
  C. Lopen""")
  choice = input(">>> ")
  if choice in answer_A:
    print("\nDe bus heeft vertraging dus je komt te laat.. Je bent af!")
    "\n\nJe bent af!"
  elif choice in answer_B:
    print ("\n Tijdens het fietsen klapt je band nu komt je te laat.. \n\nJe bent af!")
  elif choice in answer_C:
    option_lopen()
  else:
    print (required)
    option_wakker()

def option_lopen():
  print ("\n Tijdens het lopen zie je een berjaard iemand die een drukke weg moet oversteken, je wilt graag helpen alleen je riskeerd het om de trein te missen.. Zou jij helpen? J/N?")
  choice = input(">>> ")
  if choice in ja:
    print("\nDat is heel aardig van je. Je hebt je trein gemist, je komt op school aan en verteld het verhaal. De docenten geloven je niet en bent niet meer welkom in de les.") 
    print ("\n\nJe bent af!")
  else:
   print("Je komt optijd voor de trein maar er is geen plek meer wacht jij op de volgende of ga je staan? \nA. Wachten\nB. Staan")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nSerieus? je ging wachten omdat je niet wou staan.. Je bent te laat gekomen\n\nJe bent af!")
  elif choice in answer_B:
    print ("\nJe ging staan en bent daardoor optijd \n\nJe hebt het gehaalt!")
  else:
    print (required)
    option_lopen()

def option_uit():
  print ("\nJe hebt je wekker uitgezet en word veel te laat wakker.. "
  "Geef je op of ga je toch nog naar school :")
  time.sleep(1)
  print ("""  A. Boeie ik ben toch al te laat ik heb geen zin meer..
  B. Ja ik wil zo snel mogelijk op school aankomen, ik kom om te leren!""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("Je bent niet op komen dagen.. dit was niet de eerste keer je word geschorst. "
    "\n\nJe bent af!")
  elif choice in answer_B:
    print ("\nJe bent alsnog te laat.. De docenten zijn helemaal klaar met jou en laten je de les niet meer in. "
    "\n\nJe bent af!")

  else:
    print (required)
    option_uit()

intro()