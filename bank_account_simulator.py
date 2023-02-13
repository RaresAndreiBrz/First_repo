"""
1. Declaram expected results - user, password, sold
2. Introducem username valid
3. Verificam corectitudinea user-ului
4. Introducem parola valida
5. Verificam corectitudinea parolei
6. Simulam log-in
7. Afisam msj expected sold
8. Intampinam userul cu msj "cat cash doresti sa transferi?"
9. Afisam in consola daca tranzactia are loc, cat ii ramane.
10. Extragem lungimea parolei
11. Daca lungimea parolei e mai mica decat 5 codul sa dea "eroare", folosind assert
12. Afisam in consola username-ul dar parola sa fie inlocuita cu "*****"
"""

user: str = "rares"
password: str = "abc123"
sold: int = 50000


actual_user = input("Introduceti username: ").lower()

print(actual_user)


assert user == actual_user

actual_password = input("Introdu parola: ")
print(actual_password)
assert password == actual_password
len_password = len(password)
assert len_password > 5

a = ["!", "@", "#", "$", "%", "^", "&", "*"]
b = password.count(a)
assert b > 0
print("Character found!")

print(f"Parola introdusa este ok! ")

input("Press Enter to Login")

print(f'Soldul dvs este : {sold}')

cash = int(input("Ce suma doriti sa retrageti?: "))


assert sold - cash >= 0

sold = sold - cash
print(f"Noul dvs sold este: {sold}")




