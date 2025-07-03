print("ttesttttt")

print(3-5)
print(3/50)
print((32 - 5) * 2)
print(2**3)
print(9/2)
print(9//2)
print(9%2)
print(-2//0.533222323)

"Data Types"
"Int tam sayi degerlerini okur mesela "
print(int(45/4))

"Float ise kesirli sayilari gosterir(ozelinde int degerlerin de hepsini kapsar)"
print(float(45/4))

"Boolean degerler ise True ve ya False degerlerini okudugumuz degerlerdir ve mantik kurallari (ve, ve ya , degil) olmak uzere degerlendirir"
osimhensMoney = 75
galaMoney = 25 
if (galaMoney >= osimhensMoney):
    print(True)
else:
    print(False)

".len() o dizideki texti okur ve kac harf oldugunu verir"

testArray = "osimhen"
countArray = len(testArray)
print(countArray)
"ve evet int degeri okumaz"

"Types: aslinda bir kumelendirme islemi de diyebiliriz  ornegin "
print(type(4380))
print(type(4380.9))
print(type("4380"))

"Strings kismini direkt gectim ama burasi kritik (String Methods)"
"1 - .title bas harfini buyuk yazdirir"
titleVal = "testtirbu"
print(titleVal.title())

"2 - .format() {} degerleri arasina otomatik deger atar"
gsForvetSurname= "Osimhen"
gsForvetName = "Victor"
gsForvetPrice = 75

print("galatasarayin yeni transferi {} {} ".format(gsForvetName, gsForvetSurname ) + " "  +  "ve transfer ucreti {} milyon euro".format(gsForvetPrice))
"3 - .islower() tanimladigimiz degeri kontrol eder ve buyuk harf olup olmadigina bakar"

ekoVal = "ekob4"
if ekoVal.islower():
    print("her sey yolunda")
else:
    print(False)

"4- .count() icerisine istedigim deger istersem de ekstra kac kez n. indeksten sonra kac deger var "

countVal = "test test test test test"
print(countVal.count("test"))

secCountVal = " test test test test test"
secCount = secCountVal.count("test", 1)
print(secCount)
"5- .find() / .rfind()"
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(len(verse))

questionSolve = "1.cevabi {}\n 2.nin cevabi{}\n 3.nun cevabi{}" 
firstVerse = verse.find("and")
secondVerse = verse.rfind("you")
youCount = verse.count("you")
lastVal = questionSolve.format(firstVerse, secondVerse , youCount)
print(lastVal)

"Tuples"
".tuple() degistirilemez bir dizi olusturur mesela ben boyumu adimi ve kilomu kaydetmek istiyorum ve bu degerleri degisken olmayan(immutable) olarak atamak istiyorum "
"iki ve ya ikiden fazla degisken atadigimiz durumlarda kullaniyoruz."
"ozelinde bu bir listedir tabiki"
ekoBodyVal = [182, 85]
height , weight = ekoBodyVal
print("benim boyum{} ve kilom {} su sekildedir".format(height,weight))
"list yapisi degiskenleri kayit eder bu ise degismez datalari kayit eder"

"Set"
".set() komutu tekrarli dize icersindeki degerleri kaldirir"
allCountries = ["Netherlands", "Greece", "Sweden", "Poland", "Belgium", "Portugal", "Austria", "Switzerland","Switzerland","Switzerland"]
allCountriesLengthWithoutSet = len(allCountries)
allCountriesLengthWithSet = len(set(allCountries))
allCountriesLengthWithSetSec = set(allCountries)

print("{} set'siz dizi {} set'li dizi".format(allCountriesLengthWithoutSet,allCountriesLengthWithSet))
"mesela bu ulkeler arasinda hindistan var mi diye kontrol de edebilirim"
print("India" in allCountries)
"ve ya birden fazla var mi bu degerden"
print("Switzerland" in allCountries)
print("Switzerland" in allCountriesLengthWithSetSec)
"demekki birden fazla Isvicre degeri var diyebiliriz"

"Dictionary Data"
"Burasi da liste mantiginda ama listeden farkli calisir. List degerleri degisken ve siralidir ama dictinoary degerler ne sirali ne de degiskendir"
"yine boy kilo orneginden gidecegim"
MustafaKemal = {'height' : 1.74, 'title' : "Baskomutan"}
MustafKemalHeight = MustafaKemal.get('height')
print("a",MustafKemalHeight)
"peki bundan daha fazla datayi bir arada tutmak istesem nasil tutardim"

MustafaKemalInfos = {
    'bodyType': {
    'height' : 1.74,
    'eyeColor' : "Blue",
    'hairColor' : "yellow"
    },
    'achivments':{
        'warsWon' : 7
    }
}

print(MustafaKemalInfos["bodyType"],MustafaKemalInfos["achivments"])
"peki bu diziye nasil disaridan deger eklenir"

medalInfo = {"medal" : 24}
MustafaKemalInfos["medalInfo"] = medalInfo
print(MustafaKemalInfos["medalInfo"])

".split() bir diziyi paracalamak icin split komutunu kullaniriz"
countriesDic = "Netherlands, Greece, Sweden, Poland, Belgium, Portugal, Austria, Switzerland,Switzerland,Switzerland"
countriesDicSplit = countriesDic.split(",")
print(countriesDicSplit)
"bu sekilde de dizileri ayirabiliriz split(bu kisim ayirmak istedigim oruntuyu belirler)"
print(MustafaKemalInfos.keys())
".keys kullanarak da dic. olsutururken kullandigimiz datalari gorebiliriz"
"sorted metodunu ise sirali olmayan dizileri siralamak icin kullanabiliriz"
fruitVal = ["elma", "armut", "cilek", "muz"]
print(fruitVal)
print(sorted(fruitVal))

"ve ya"

fruitValSec = sorted(fruitVal)
print(fruitValSec)

"CONTROL FLOW"
"If Dongusu"

electionVal = 2027
if electionVal == 2027 :
    print("kurtulma sansin var")
else :
    print("kurtulmana son {} yil ".format(int(2027 - electionVal)))
"Else vs Elif"
"Eger kosulu devam ettiriyorsak elif kullaniriz. Ettirmiyorsak else."

electionVal = 2027
if electionVal == 2027 :
    print("kurtulma sansin var")
elif electionVal < 2027 :
    print("kurtulmana son {} yil ".format(int(2027 - electionVal)))
elif electionVal > 2027 :
    print("gg") 

"for loop"
"for dongusu bir diziyi sirayla isleyerek bastirir"

for fruits in fruitVal : 
    fruits = fruits.title()
    print(fruits)
"range()"
"bir aralikta diziyi okur ve ya yenilenen bir dize olusturur"
for rangeVal in range(3) :
    print("test")

for rangeVal in range(0,3):
    print(rangeVal)

"for ve ici su sekilde okunur = for(baslangic,bitis,oruntu) seklinde okunur"
"mesela aritmetik bir kume olustursak"
for rangeVal in range(0, 10 , 2 ): 
    print(rangeVal)

"bir listeyi for loop ile okumak"
"mesela her isim soy isim arasinda bir * istiyor olsam sunu yapardim"

userNames = ["Victor Osimhen", "Mauro Icardi" , "Leroy Sane"]

for userNameVal in userNames :
    userNameVal = userNameVal.replace(" ", "*").lower()
    print(userNameVal)
"ve yine bu degeri disaridaki bir print okumaz"
"For dongusu orijinal bir listeye dokunmaz degisikligi kendi icinde yapar bu yuzden ben disarida da bu degeri okumak istiyorsam bos bir liste olusturmaliyim"

userNamesForLoop = []

for userNamesVal in userNames :
    userNamesVal = userNamesVal.replace(" ", "*").lower()
    userNamesForLoop.append(userNamesVal)

print(userNamesForLoop)

"seklinde yeni listeyi de disaridan okuyabilirim"


