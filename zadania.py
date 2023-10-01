#1
zmienna_int = 42
zmienna_float = float(zmienna_int)
print(zmienna_float)

#2
pierwsza_zmienna_string = "3"
druga_zmienna_string = "3.14"
zmienna_int= int(pierwsza_zmienna_string)
zmienna_float = float(druga_zmienna_string)
print(zmienna_int, zmienna_float)

#3
zmienna_int = 42
zmienna_str = str(zmienna_int)
print(zmienna_str)

#4 i 5
a = 5
b = 3.5

suma = f"{a} + {b} = {a + b}"
roznica = f"{a} - {b} = {a - b}"
iloczyn = f"{a} * {b} = {a * b}"
ilorazCalkowity = f"{a} // {b} = {a // b}"
ilorazRzeczywisty = f"{a} / {b} = {a / b}"
potega = f"{a} / {b} = {a / b}"
modulo = f"{a} / {b} = {a / b}"

print(suma)
print(roznica)
print(iloczyn)
print(ilorazCalkowity)
print(ilorazRzeczywisty)
print(potega)
print(modulo)

#6 Modyfikacja krotki jest niemożliwa, ponieważ krotki są niemodyfikowalne. 
# Można za to zrobić nową krotkę z elementami starej i ewentualnie podmienić interesujące nas elementy.

#7 Zapisujemy prosto do zmiennych, przykład poniżej.
lista = [1, 2, 3]
a, b, c = lista
print(a, b, c)

#8
wyniki_lotto = [5, 12, 18, 22, 30, 42]
print(wyniki_lotto)

wyniki_lotto = []
wyniki_lotto.append(5)
wyniki_lotto.append(12)
wyniki_lotto.append(18)
wyniki_lotto.append(22)
wyniki_lotto.append(30)
wyniki_lotto.append(42)
print(wyniki_lotto)

#9
schorniska_info = {
    "Kraków": 10,
    "Warszawa": 15,
    "Poznań": 8
}
print(schorniska_info)

#10  Daty losowań i liczb są losowe
ostatnie_wyniki_lotto = {
    "2023-09-30": [5, 12, 18, 22, 30, 42],
    "2023-09-27": [2, 10, 15, 25, 31, 37],
    "2023-09-24": [8, 14, 20, 24, 28, 35]
}

print(ostatnie_wyniki_lotto)

#11
#Dla liczb całkowitych (int) i zmiennoprzecinkowych (float) dostępne są wszystkie operacje arytmetyczne wypisane w zadaniu 4 i 5.
#Dla list i krotek dostępne są operacje indeksowania, dodawania, usuwania, wycinania, itp.
#Dla słowników dostępne są operacje dodawania, usuwania i dostępu do wartości za pomocą klucza.