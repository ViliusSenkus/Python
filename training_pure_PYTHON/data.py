# #*******************************************************************#
# #****************** PYTHON MOKOMASIS FAILAS ************************#
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


# #STRING funkcijos/metodai

# eilute = "string"
# eilute[4]           #gražina 4 eilutės simbolį
# eilute[2:4]         #gražina eilutės elementus pradedant nuo 2 ir baigiant neįskaitytinai 4.
# eilute[4:]          #gražina eilutės elementus pradedant nuo 4.
# eilute[1:6:2]       #gražina eilutės elementus pradedant nuo 1 ir biagiant 6(neįskaitytinai), kas 2 elementus.
# eilute[::2]         #gražina eilutės elementus kas 2 elementus. Galima ir minusinė reikšmė
# len(eilute)         #gražina eilutės simbolių skaičių - eilutės ilgį
# eilute.count('s')   #gražina skaičių nurodantį kiek atitinkamų elementų yra kintamajame eilutė
# eilute.upper()      #pakeičia visas raides į didžiąsas
# eilute.lower()      #pakeičia visas raides į mažąsias
# eilute.isupper()    #true/false ar visos raidės yra didžiosios
# eilute.islower()    #true/false ar visos raidės yra mažiosios
# eilute.capitalize() #pakeičia eilutės pirmą simbolį į didžiąją raidę, o kitas į mažąsias
# eilute.find('ri')   #gražina atrasto fragmento pirmo atitinkamo simbolio eilės numerį. (2)
# eilute.split(',')   #suskaido eilutę į masyvą pagal nurodytą elementą
# arr=[]
# ", ".join('arr')   #sujungia masyvo 'arr' elementus į eilutę, per nurodytą simbolį - ', '
# ", ".join('arr')   #






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

# #for
# for i in range(6):  #nurodant iteracijų skaičių
#   print(i, end="")

# print()

# for i in range(2, 6):  #nurodant iteracijų skaičiaus ribas
#   print(i, end="")

# print()

# for i in range(1, 6, 2):  #nurodant iteracijų skaičiaus ribas ir žingsnį
#   print(i, end="")

# #String iteracija
# print('Line 107-110. Iteration through characters of string \"word\"')
# word = 'word'
# for i in word:
#   print(i, end="-")

# #while
# print('\nLine 113-117. While loop')
# i=6 
# while i < 15:
#   print(i, end=".")
#   i +=1

# #ciklo nutraukimui - break
# #iteracijos peršokimui - continue

# #DUOMENŲ MASYVAI, SĄRAŠAI
# print('\n\tMASYVAI')
# arr = [] #tuščias masyvas
# arr = [0,8,3, 'tekstas', True, [1,2,3], 12.456]

# #masyvo elemento iššaukimas
# arr[2]
# arr[-1] #paskutinio elemento iššaukimas
# arr[5][1] #elemento elemente pasiekimas

# #elemento pridėjimas
# arr=[1,2,3]
# arr.append('dar vienas elementas')
# arr.extend([4,5,6]) #kelių elementų pridėjimas į masyvo galą
# arr.insert(1,True) #įterpia elementą nurodytoje vietoje

# # #Masyvo rūšiaviams
# # arr.sort() #rušiuoja tik skaitmenis ir booleanus
# #   # rūšiuojant reikšmė True prilyginama 1, False - 0.
# # arr.reverse() 

# #elementų naikinimas
# arr.pop() #paskutinio
# arr.pop(3) #trečio elemento panaikinimas
# arr.remove('dar vienas elementas') #elemento su reikšme 'tekstas' panaikinimas
# arr.clear() #viso masyvo išvalymas

# #kitos masyvų f-jos
# arr.count(2)  #skaičiuoja kiek masyve yra nurodytų elementų. šiuo atveju kiek dvejetukų.
#               #jeigu atitikmenų nėra gražina 0
# len(arr) #skaičiuoja pirmo lygmens masyvo elementų skaičių        


# #SĄRAŠAI---KORTEŽAI --- TUPLE
#   #negalima keisti reikšmės
# data1 = (1,2,3)
# data2 = 4,5,6
# data1[1]
# data2[1]
# tuple(arr) #pakeičia masyvą į tuple
# tuple(eilute) #pakeičia eilutę į eilutės simbolių tuple


# #ŽODYNAI --- DICTIONARY
# data = {'key': 'value', 3: 55, 'vardas':'vardenis', 'tiesa':True}
# data['key']
# data.get('key')
# dict(key='value', next='value2') #key visada eilutė

# data.items()  #gražina sąrašą kaip keikvieno key ir value tuplas, masyve patalpintame į tuple
# print(data.items())

# for key, value in data.items():
#   print(key, ' : ', value )

# data1 = {'key': 'value', 3: 55, 'vardas':'vardenis', 'tiesa':True}
# data.keys()     #gražina raktų masyvą patalpintą į tuple
# data.values()   #gražina reikšmių masyvą patalpintą į tuple

# data.clear()
# data1.pop('vardas')  #išmeta reikšmę, kurios key yra vardas 
# data1.popitem()  #išmeta paskutinę reikšmę


# #SET
#   #reikšmių sąrašas su nesikartojančiais ir išrikiuotais elementais
# set('llllabas') #sukuria elementą/žodyną/objektą su nepasikartojančiom reikšmėm ('l','a','b','s')
# data2 = {1,2,3,4,4,5}
# data2.add(12)
# data2.update(12,13,14)
# data2.remove(13)
# data2.pop() #panaikina pirmą elementą
# data2.clear()

# #frozen set
#   #frozen set = tuple + set
# frozenset([2,3,4])

# #FUNCTIONS

# def funkcija():
#   pass  #absoliučiai nieko neįvyks

# def funkcija(parameter):
#   pass

# #Anoniminė funkcija - liamda funkcija
# x = lambda x, y: x+y    #funkcijos aprašymas
# res = x(2,3)            #funkcijos iššaukimas


# #FILES
# #atidarom-dirbam-uždarom
# failas = open('README.txt', 'w')  #jeigu failo nėra jis bus sukurtas, kartu su visu nurodytu keliu
#                                   # astidarymo režimai:
#                                   # w - write - seną informaciją ištrina;
#                                   # a - append - prideda prie senos informacijos;
#                                   # r - read - nuskaityti failą
# failas.write('Hello\n')        
# failas.read(2)                    #nuskaito du simbolius. Nenurodžius - skaito visą failą
# for eilute in failas:
#   print(eilute, end="")           #nuskaitymas eilutėmis
                                
# failas.close()


# #EXEPTIONS
# try:
#   x = int(input('ivesk skaiciu'))
# except ValueError:                    #vertės klaida. suveikia jeigu yra atitinkamo tipo klaida.
#   print('reikia ivesti skaiciu')
# else:
#   print('nežinoma klaida')
# finally:
#   print('atlikta')


# #WITH ... AS
# try:
#   with open('failas.txt', 'r', encoding='utf-8') as file:  #Šiuo atveju neireikia uždarinėti failo, jis uždaromas automatiškai.
#     print(file.read())
# except FileNotFoundError:
#   print('failas neegzistuoja')


# #MODULES
# # modulis - failas arba failų rinkinys
# # pypi.org

# import time
# time.sleep(2) #sustabdo programą 2 sek.

import platform as plat, sys, os  #įkelia platform kaip plat ir modulius sys ir os
print(sys.path)
print(os.name)
print(plat.system())

from math import sqrt  #dalies modolio importavmas
x=sqrt(36)

#savo modulio importavimui : import failo_pavadinimas_be_.py
#daliai bibliotekų naudojimui reikia jas instaliuoti pvz.: T: pip install cowsay


#DATE-TIME
import datetime as d
print(d.datetime.now().time())

