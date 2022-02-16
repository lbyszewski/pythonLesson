
#zagnieżdżenia w pętli for
poczatek = int(input("podaj p: "))
koniec = int(input("podaj k: "))
dzielnik = int(input("podaj d: "))


if(poczatek >0 and koniec >0 and dzielnik >0):
    for liczby in range(poczatek,koniec+1):
        if(liczby % dzielnik == 0):
            print(liczby)

for t in range(1,10+1):
    print(t)
    for w in range(1,10+1):
        print(w)

#pętla while

c = int(input("podaj c: "))

x = 1
while(x<=c):
    x*=2
    print(x)





