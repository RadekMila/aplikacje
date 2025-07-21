import json
import os
import msvcrt

imie = ""
PIN = 0
hasło =""

users = {
    "user1": {
        "imie": "Bartek kozinski",
        "hasło": "Ketrab1234",
        "PIN": 9283
    },
    "user2": {
        "imie": "Radek Mila",
        "hasło": "Kedar1234",
        "PIN": 2684
    },
    "user3": {
        "imie": "Mateusz karanczyk",
        "hasło": "Szuetam1234",
        "PIN": 8576
    }
}


def logowanie():
    etap = 1
    proby = 4
    while etap <= 3:

        if etap == 1:
            imie2 = input("Podaj swoje imie i nazwisko:")
            if imie2 != imie:
                proby -= 1
                print(f"Błędne imie,spróbuj ponownie.Pozostałe próby:{proby}")
                if proby == 0:
                    print("wpisano nieprawidłowe hasło 4 razy.")
                    break
            elif imie2 == imie:
                etap += 1
                proby = 4
                print("Prawidłowe imie i nazwisko")

        elif etap == 2:
            pin = int(input("Podaj swój PIN:"))
            if pin != PIN:
                proby -= 1
                print(f"Błędny PIN,spróbuj ponownie.Pozostałe próby:{proby}")
                if proby == 0:
                    print("wpisano nieprawidłowy PIN 4 razy.")
                    break
            elif pin == PIN:
                etap += 1
                proby = 4
                print("Prawidłowy PIN")

        elif etap == 3:
            haslo = input("Wpisz swoje hasło:")
            if haslo != hasło:
                proby -= 1
                print(f"Nieprawidłowe hasło,spróbuj ponownie.Pozostałe próby:{proby}")
                if proby == 0:
                    print("wpisano nieprawidłowe hasło 4 razy.")
                    break

            elif haslo == hasło:
                etap += 1
                proby = 4
                print("Prawidłowe hasło.Witamy w systemie")
                break


print("💰Witamy w banku💰.")
user = input("Wybierz użytkownika:user1,user2,user3.\n-")

if user == "user1":

    imie = users.get("user1", {}).get("imie")
    PIN = users.get("user1", {}).get("PIN")
    hasło = users.get("user1", {}).get("hasło")
    logowanie()

elif user == "user2":

    imie = users.get("user2", {}).get("imie")
    PIN = users.get("user2", {}).get("PIN")
    hasło = users.get("user2", {}).get("hasło")
    logowanie()

elif user == "user3":

    imie = users.get("user2", {}).get("imie")
    PIN = users.get("user2", {}).get("PIN")
    hasło = users.get("user2", {}).get("hasło")
    logowanie()
