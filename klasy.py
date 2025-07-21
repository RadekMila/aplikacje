from random import choice


class Produkty:
    def __init__(self,nazwa,cena,ilość):
        self.nazwa = nazwa
        self.cena = cena
        self.ilość = ilość

    def __str__(self):
        return f"{self.nazwa} | Cena: {self.cena} zł | Ilość: {self.ilość}"

class Magazyn:
    def __init__(self):
        self.produkty = []

    def dodaj_produkt(self,produkt):
        self.produkty.append(produkt)

    def usun_produkt(self,nazwa):
        self.produkty = [p for p in self.produkty if p.nazwa != nazwa]

    def pokaz_produkty(self):
        for x in self.produkty:
            print(x)

    def sprzedaj_produkt(self,nazwa,ilość2):
        for z in self.produkty:
            if z.nazwa == nazwa:
                if z.ilość >= ilość2:
                    z.ilość -= ilość2
                    print(f"Sprzedano {ilość2} szt. {nazwa}.")
                else:
                    print("Za mało na stanie")
                return
        print("Produkt nie znaleziony.")

def menu():
    magazyn = Magazyn()
    while True:
        print("\n1.Dodaj produkt")
        print("2.Pokaż produkty")
        print("3.Sprzedaj produkt")
        print("4.Usuń produkt")
        print("5.Wyjście")

        choice = input("Wybierz opcje:")

        if choice == "1":
            nazwa = input("Nazwa produktu: ")
            cena = float(input("Cena: "))
            ilosc = int(input("Ilość: "))
            produkt1 = Produkty(nazwa, cena, ilosc)
            magazyn.dodaj_produkt(produkt1)
        elif choice == "2":
            magazyn.pokaz_produkty()
        elif choice == "3":
            nazwa = input("Nazwa produktu do sprzedaży: ")
            ilosc = int(input("Ilość: "))
            magazyn.sprzedaj_produkt(nazwa, ilosc)
        elif choice == "4":
            nazwa = input("Nazwa produktu do usunięcia: ")
            magazyn.usun_produkt(nazwa)
        elif choice == "5":
            break
        else:
            print("Nieprawidłowa opcja!")

menu()


