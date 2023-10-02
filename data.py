# #*******************************************************************#
# #*******************PYTHON*MOKOMASIS*FAILAS*************************#
# #*******************************************************************#


# # Komentaras


# # STRINGAI

# #standart output:
# print('Line 12. Standart output with one parameter')
# print('Line 13 Standart output with first paramerter,','and second parameter conected with , symbol')
# print('Line 14 with three different parameters (this string, integer, and special characters requering escape symbol \)', 5, '\"a\"')

# #separator
#       # išvedant informaciją tarp parametrų paliekamas tarpas - separatorius.
#       # defaultinis parametras - print(sep=" ")
#       # Separatoriaus pakeitimas:
# print('Line 20. Separator example. use | as an separator beatween two parameters', 2, sep="|")

# #end of string
#       # defaultinis eilutės galo nustatymas - print(end="\n")
#       # Eilutės galo pakeitimas:
# print('Line25. Line end example', end="---") # simbolių gali būti betkiek, pvz.:end=("-!\n")
# print('Second line of Line end example')

# #darbas su skaičiais kaip tekstu
# print('Line 29. integers converting to string example' + str(7)) #skaičiaus konvertaviams į tekstą
# print('Line 30. text multiplication example' * 2)      #teksto kartojimas n kartų

# # matematiniai veiksmai eilutėje
# print('Line 33-36. integers math examples: 5+5, 5**2, 5//3')
# print(5+5)
# print(5**2) #kelia kvadratu
# print(5//3) #dalina iki sveiko skaiciaus
# print('Line 37. Different Math functions print examples (min, max ...)', min(1,2,3,4), max(1,2,3,4), abs(-5), pow(5, 3), round(8/3))
# print('Line 38. string to int converting example', 7+int('4')) # teksto konvertavimas į skaičių


# #INPUT

# #standart input
# input('Line 44-45Standard request input with explanation text. Next request without explanation text')
# input()
# kintamasis = input('Line 46. Input with value assignment to variable.')  #inputas visada string'as.
#                       # Pakeisti galima taip:
# kintamasis=int(input('Line 48. Input as int example.'))


# # KINTAMIEJI

# pavadinimas = 'reiksme' #string
# kablelis = 4.5456       #int, float
#                         #bool

# #kintamojo panaikinimas:
# del pavadinimas


# #CONDITIONALL PROGRAMMING

# # general case
# if 5==5:
#   print('Line 65. General if case demo. Just checked if 5 equal to 5')

# # if in if
# if 5==5:
#   print('Line 69-71. If in if demo. First if is correct')
#   if 7==7:
#     print('second if is correct')

# # else if
# teisybe = True        
# if not teisybe:
#   print('Line 74-80. Else if demo. You see this if ture is false.')
# elif teisybe == 4:
#   print('else if demo. You see this if ture is equal to 4.')
# else:
#   print('else if demo. You see this if ture is true.')

# #ternar operator
# data = input('Line 83-84. Teenar operator demo. Iveskite skaiciu žodžiais ')
# number = 5 if data == 'five' else 0

# #logical operators and/or
# if 7==7 and 6==6 or 4==4:
#   print('Line 88. Demo of logical operators or/and ')

# #CIKLAI

#for
for i in range(6):  #nurodant iteracijų skaičių
  print(i, end="")

print()

for i in range(2, 6):  #nurodant iteracijų skaičiaus ribas
  print(i, end="")

print()

for i in range(1, 6, 2):  #nurodant iteracijų skaičiaus ribas ir žingsnį
  print(i, end="")

#String iteracija
print('Line 107-110. Iteration through characters of string \"word\"')
word = 'word'
for i in word:
  print(i, end="-")

#while
print('\nLine 113-117. While loop')
i=6 
while i < 15:
  print(i, end=".")
  i +=1

#ciklo nutraukimui - break
#iteracijos peršokimui - continue

#DUOMENŲ MASYVAI, SĄRAŠAI
print('\n\tMASYVAI')
arr = [] #tuščias masyvas
arr = [0,8,3, 'tekstas', True, [1,2,3], 12.456]

#masyvo elemento iššaukimas
arr[2]
arr[-1] #paskutinio elemento iššaukimas
arr[5][1] #elemento elemente pasiekimas

#elemento pridėjimas
arr=[1,2,3]
arr.append('dar vienas elementas')
arr.extend([4,5,6]) #kelių elementų pridėjimas į masyvo galą
arr.insert(1,True) #įterpia elementą nurodytoje vietoje

# #Masyvo rūšiaviams
# arr.sort() #rušiuoja tik skaitmenis ir booleanus
#   # rūšiuojant reikšmė True prilyginama 1, False - 0.
# arr.reverse() 

#elementų naikinimas
arr.pop() #paskutinio
arr.pop(3) #trečio elemento panaikinimas
arr.remove('dar vienas elementas') #elemento su reikšme 'tekstas' panaikinimas
arr.clear() #viso masyvo išvalymas

#kitos masyvų f-jos
arr.count(2)  #skaičiuoja kiek masyve yra nurodytų elementų. šiuo atveju kiek dvejetukų.
              #jeigu atitikmenų nėra gražina 0
len(arr) #skaičiuoja pirmo lygmens masyvo elementų skaičių        

