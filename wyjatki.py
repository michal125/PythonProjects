
try:
    a = input('Podaj liczbe a: ')
    b = input('Podaj liczbe b: ')

    print(int(a)/int(b))

except ValueError:
    print("Wartośco są nie prawidłowe")

except ZeroDivisionError:
    print("Nie dzielimy przez zero")


print('To impreza dla chlopakow')

try:
    for _ in range(5):
        imie = input("Jak masz na imie")
        if imie[-1] == 'a':
            raise Exception("Jestes dziewczyna")
        print("Mozesz wejsc")

except Exception as error:
    print("Ojojo may blad")
    print(error)


class ToLowerAmount(Exception):
    pass

class ToHighAmount(Exception):
    pass

for _ in range(10):
    try:
        amount = int(input("Podaj kwote: "))
        if amount <= 0:
            raise ToLowerAmount()
        if amount > 1000:
            raise ToHighAmount()
    except ToHighAmount:
        print("zbyt mala kwota")
    except ToLowerAmount:
        print("zbyt duza kwota")
