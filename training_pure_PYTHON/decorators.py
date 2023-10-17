import webbrowser


#DEKORATORIUS
def dekoratorius(func):
      def wrapper(*param):    # *-nurodo belenkokį argumentų sk.
            #param atitinka funkcijos, kuriai taikomas dekoratorius perduodamus parametrus (url_addr)
            print('dekoratorius prieš funkciją')  #galima naudoti validacijai duomenų
            func(*param)
            print('dekoratorius po funkcijos')
      return wrapper

@dekoratorius
def open_url(url_addr, dat):
      webbrowser.open(url_addr)
      print('atidaryta', dat)

open_url('www.google.com', 'google')



#Kitas pavyzdys
def validator (func):
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")
    return wrapper

@validator
def print_sum(a,b):
    print("sum=",a+b)

@validator
def print3(a,b,c):
    print("abc",a,b,c)


print_sum(1,2)
print3(10,20,30)