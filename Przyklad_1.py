class Przyklad_1():
    def __init__(self):
        pass
    
    def prosty_range(self,dec):
        def generator(x):
            i = 0
            while i < x:
                yield i
                i += 1
                
        def lista(x):
            i = 0
            wynik = []
            while i < x:
                wynik.append(i)
                i += 1
            return wynik
        
        
        def wybor():
            if dec == "1":
                print("Generator")
                for i in generator(99999999):
                    if i != 0 and i % 123 == 0 and i % 401 == 0 and i % 589 == 0:
                        print(i)
            else:
                print("Lista")
                for i in lista(99999999):
                    if i != 0 and i % 123 == 0 and i % 401 == 0 and i % 589 == 0:
                        print(i)
                
        
        wybor()
            

przy = Przyklad_1()

print("Wybierz opcje do znalezienia liczb na skomplikowanych warunkach:")
print("1. Generator (zadziała po chwili)")
print("2. Lista (spal komputer)")
decision = input("Wybierz: ")
if decision == "1":
    przy.prosty_range("1")
else:
    przy.prosty_range("2")
    
print("Jaka jest różnica?")
print("Lista najpierw się tworzy a potem jest zwracana, co oznacza, że każda liczba jest dodawana do listy.")
print("Niepotrzebnie próbujemy generować niepotrzebne nam liczby których w")
print("tym przypadku jest ich bardzo dużo.")
