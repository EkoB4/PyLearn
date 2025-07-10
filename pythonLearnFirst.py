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

"seklinde yeni dictinoaryide disaridan okuyabilirim"

"key ve isimleri ayni anda nasil cagiririz?"

adminPerson = {'name': "nagme", 'age' : 19}
print(adminPerson.items())

"Dict ornek amele solituon vs clean code"

"1- amele "
"TASK : You would like to count the number of fruits in your basket. In order to do this, you have the following dictionary and list of fruits. Use the dictionary and list to count the total number of fruits, but you do not want to count the other items in your basket."

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
fruitsList = {}
#Iterate through the dictionary

for fruitVal in fruits :
    fruitsList[fruitVal] = fruitVal #dict. i listeye aktardim
#if the key is in the list of fruits, add the value (number of fruits) to result
for itemVal in basket_items.items():
    print("{}".format(itemVal))
    itemTotal = basket_items["bananas"] + basket_items["grapes"]
    print("total fruit {}".format(itemTotal))#toplam meyve sayisi

#If your solution is robust, you should be able to use it with any dictionary of items to count the number of fruits in the basket. Try the loop for each of the dictionaries below to make sure it always works.
"AMELE KODA BAYBAY CUNKU HEPSINDE BASKET ITEMS DEGISTIRMEK ZORUNDA KALACAGIM BU GIDISLE SIMDI DIREKT CLEAN CODE"
#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here

for object, itemVal in basket_items.items() :
    if object in fruits :
        result += itemVal
print(result)

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here

for object, itemVal in basket_items.items():
    if object in fruits :
        result += itemVal
print(result)


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for object, itemVal in basket_items.items():
    if object in fruits : 
        result += itemVal
print(result)

#while loop

#TASK BU :"Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop. For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

#Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through the loop? What condition will you use to see when it's time to stop looping?

#After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. It is the case that break_num should be a number that is the first number larger than end_num."
start_num = 10 
end_num = 100
count_by = 10

breakNum = start_num 

while breakNum < end_num :
    breakNum += count_by
    print(breakNum)

#Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, and calculate break_num the way you did in the last quiz.
#Now in addition, address what would happen if someone gives a start_num that is greater than end_num. If this is the case, set result to "Oops! Looks like your start value is greater than the end value. Please try again." Otherwise, set result to the value of break_num.

if start_num > end_num :
    while breakNum < end_num :
        breakNum += count_by
    else:
        print("Oops! Looks like your start value is greater than the end value. Please try again.")

#Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.
#For example, if limit is 40, your code should set the nearest_square to 36.       
limit = 40

# write your while loop here
num = 0 
while (num + 1)**2 < limit :
    num += 1
    nearest_square = num**2
print(nearest_square)