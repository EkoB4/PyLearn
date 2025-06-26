"Data Types"
"1- int tam sayi degerlerini alir "
print(int(45/4))
"2- float burada da kesirli degerleri okuruz"
print(float(45/4))
"3- Bool true/false degerlerini okuruz"
osimhenPrice = 75
gsMoney = 40
if(gsMoney >= osimhenPrice ) :
    print(True)
else:
    print(False)
"4 - len() : texti okur kac tane harf var degerlendirir"
testVal = "buradaa kac tane har varr"
print(len(testVal))
"text de kac tane harf var onu okuruz sayisal bir deger okumayiz"
"TYPE degiskenleri kumlendiririz"
print(type(43))
print(type(43.0))
print(type("43"))
".count() istedigimiz degerin kac tane olduguna bakariz"

countVal = "test test test test test"
countTest = countVal.count("test")
print(countTest)
".islower() bu komutta da text in tum harflerinin kucuk olup olmadigini degerlendiririz"

lowerText = "ekob4"
if lowerText.islower():
    print("her sey yolunda")
else:
    print("harfleri duzenleyiniz")
".find()/.rfind() komutlari da istedigimiz datalari bulmaya yarar ornegi:"
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(len(verse))

questionSolve = "1.cevabi {}\n 2.nin cevabi{}\n 3.nun cevabi{}" 
firstVerse = verse.find("and")
secondVerse = verse.rfind("you")
youCount = verse.count("you")
lastVal = questionSolve.format(firstVerse, secondVerse , youCount)
print(lastVal)

