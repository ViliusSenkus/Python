#*******************************************************************#
#*******************PYTHON*MOKOMASIS*FAILAS*************************#
#*******************************************************************#


# Komentaras


# STRINGAI

#standart output:
print('tekstas')
print('tekstas','tekstas')
print('tekstas', 5, '\"a\"')
      # išvedant informaciją tarp parametrų paliekamas tarpas - separatorius.
      # defaultinis parametras - print(sep=" ")
      # Separatoriaus pakeitimas:
print('tekstas',2,sep="|")
      # defaultinis eilutės galo nustatymas - print(end="\n")
      # Eilutės galo pakeitimas:
print('pirma eilutė', end="---") # simbolių gali būti betkiek, pvz.:end=("-!\n")
print('antra eilutė')
      #darbas su skaičiais kaip tekstu
print('tekstas'+str(7)) #skaičiaus konvertaviams į tekstą
print('labas' * 2)      #teksto kartojimas n kartų
      # matematiniai veiksmai eilutėje
print(5+5)
print(5**2) #kelia kvadratu
print(5//3) #dalina iki sveiko skaiciaus
print(min(1,2,3,4), max(1,2,3,4), abs(-5), pow(5, 3), round(8/3))
print(7+int('4')) # teksto konvertavimas į skaičių


#INPUT

#standart input
input()
input('cia reikalaujama inputo')
kintamasis = input()  #inputas visada string'as.
                      # Pakeisti galima taip:
kintamasis=int(input())


# KINTAMIEJI

pavadinimas = 'reiksme' #string
kablelis = 4.5456       #int, float
                        #bool

#kintamojo panaikinimas:
del pavadinimas


#CONDITIONALL PROGRAMMING

# general case
if 5==5:
  print('general if case demo. Just checked if 5 equal to 5')

# if in if
if 5==5:
  print('if in if demo. First if is correct')
  if 7==7:
    print('second if is correct')

# else if
teisybe = True        
if not teisybe:
  print('else if demo. You see this if ture is false. line 69')
elif teisybe == 4:
  print('else if demo. You see this if ture is equal to 4. line 71')
else:
  print('else if demo. You see this if ture is true. line 73')

#ternar operator
data = input('iveskite skaiciu žodžiais ')
number = 5 if data == 'five' else 0

#logical operators and/or
if 7==7 and 6==6 or 4==4:
  print('demo of logical operators, line 81')
