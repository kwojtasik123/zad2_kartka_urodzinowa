print("podaj imie osoby do ktorej chcesz wyslac zyczenia")
imie_odbiorcy = input ()

print("w ktorym roku urodzil/a sie {}".format(imie_odbiorcy))
rok_urodzenia =int(input())

obecny_rok = 2024

wiek_odbiorcy = obecny_rok - rok_urodzenia


print("wpisz zyczenie dla {}".format(imie_odbiorcy))
zyczenia = input()

print("podaj swoje imie")
imie_nadawcy = input()

print(imie_odbiorcy)
print(f"Wszystkiego najlepszego z okazji {wiek_odbiorcy} urodzin!")
print(zyczenia)
print(f"zyczy {imie_nadawcy}")




