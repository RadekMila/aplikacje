class Uzytkownicy:
    def __init__(self,imie,saldo):
        self.imie = imie
        self.saldo = saldo

    def __str__(self):
        return f"{self.imie} | Saldo: {self.saldo}"

class Bank:
    def __init__(self):
        self.konta = []

    def dodaj_konto(self,nazwa):
        self.konta.append(nazwa)

    def usun_konto(self,imie):
        for x in self.konta:
            if x.imie == imie:
                self.konta.remove(imie)
                print(f"Usunięto konto: {imie}")
                return
            print("Nie znaleziono konta.")

    def pokaz_konta(self):
        for x in self.konta:
            print(x)

    def pokaz_saldo(self,imie):
        for x in self.konta:
            if x.imie == imie:
                print(f"{x.imie} ma saldo: {x.saldo}")
                return
            print("Nie znaleziono użytkownika.")

def menu():
    bank = Bank()

    while True:
        print("1.Dodaj Konto")
        print("2.Usuń konto")
        print("3.Pokaż konto")
        print("4.Pokaż saldo")

        wybor = input()

        if wybor == "1":
            nazwa1 = input("Nazwa uzytkownika")
            saldo = float(input("Podaj saldo"))
            dane = Uzytkownicy(nazwa1, saldo)
            bank.dodaj_konto(dane)
        elif wybor == "2":
            usun = input("Podaj konto do usuniecia")
            bank.usun_konto(usun)
        elif wybor == "3":
            bank.pokaz_konta()
        elif wybor == "4":
            imie1 = input()
            bank.pokaz_saldo(imie1)
menu()