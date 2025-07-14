
def haslo():
    while True:
        global user
        check = []
        user = str(input("Stwórz hasło:"))
        powtorz_user = str(input("Powtórz hasło:"))

        if powtorz_user != user:
            print("Błędne powtórzone hasło.")

        if len(user)< 8:
            print("Hasło musi mieć minimum 8 znaków")
        else:
            check.append("0")

        haslo_litera = user
        if not user[0].isupper():
            print("Pierwsza litera musi być duża")
        else:
            check.append("1")

        znaki = ["!", "@", "#", "$", "%", "^", "&", "*", ]
        if not any(z in user for z in znaki):
            print("Hasło musi zawierać chociaż jeden z podanych znaków [!,@,#,$,%,^,&,*]")
        else:
            check.append("2")

        if len(check) == 3:
            print("Hasło poprawnie ustawione.")
            break

    dostep()
#Aplikacja kalkulator z opcja dodawania,odejmowania,mnożenia,dzielenia i sprawdzenia procenta z danej liczby
def Kalkulator():
    znak4 = "%"
    print("Działania: + , - , * , : lub /, %(wylicza procent z danej liczby, end(kończy program)")
    while True:
        liczba1 = int(input("Liczba1:"))
        dzialanie = input()
        liczba2 = int(input("Liczba2:"))

        if dzialanie == "+":
            print(liczba1 + liczba2)
        elif dzialanie == "-":
            print(liczba1 - liczba2)
        elif dzialanie == "*":
            print(liczba1 * liczba2)
        elif dzialanie == ":" or dzialanie == "/":
            print(liczba1 / liczba2)
        elif dzialanie == "%":
            wynik = (liczba1 * 100) / liczba2
            print(f"{round(wynik,4)}{znak4}")
        elif dzialanie == "end":
            break

def przelew():
    global saldo
    kwota = int(input("Prosze podać kwote jaką chcesz przelać:"))
    saldo += kwota
    print(f"Kwota:{kwota} została przelana")
    print(f"Saldo:{saldo}")


def Bank():
    global ustalony_pin,saldo
    saldo = 1000
    proby = 0

    while True:
        ustalony_pin = input("Prosze podać PIN:")
        if ustalony_pin != Pin:
            print("Błędny PIN")
            proby += 1
            if proby >= 4:
                print("Pin został wpisany błędnie 4 razy")
                break
        else:
            user_bank = input("Zalogowano do Banku.Co chcesz zobaczyć/zrobić w swoim banku: Saldo/Przelew").capitalize()
            if user_bank == "Saldo":
                print(f"Saldo:{saldo}")
            elif user_bank == "Przelew":
                przelew()






def dostep():
    global Pin

    haslo = str(input("prosze wpisać hasło"))

    if haslo == user:

        while True:
            aplikacje = input("witamy w systemie.Wybierz aplikacje z której chcesz korzystać:Kalkulator/Bank\n").capitalize()

            if aplikacje == "Bank":
                while True:
                    Pin = input("Prosze stworzyć PIN czterocyfrowy:")
                    if len(Pin) > 4 or len(Pin) < 4:
                        print("Pin błędnie stowrzony")
                    else:
                        break
                Bank()
                break

            elif aplikacje == "Kalkulator":
                Kalkulator()
                break

            else:
                print("Podanej aplikacji nie ma!")
    else:
        print(f"Podane haslo {haslo} jest nie poprawne")


haslo()

