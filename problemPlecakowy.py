def plecak(pojemnosc, wagi, wartosci, ilosc):
    wyniki = [0] * (pojemnosc + 1)
    for i in range(ilosc):
        for j in range(pojemnosc, wagi[i] - 1, -1):
            if wagi[i] <= j:
                wyniki[j] = max(wyniki[j], wartosci[i] + wyniki[j - wagi[i]])
    return wyniki[pojemnosc]

wartosci = [60, 100, 120]
wagi = [10, 20, 30]
pojemnosc = 50
ilosc = len(wartosci)
print(plecak(pojemnosc, wagi, wartosci, ilosc))
