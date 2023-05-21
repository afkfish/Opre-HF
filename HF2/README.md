# Fakultatív feladat: lapcsere-algoritmus megvalósítása

Készítsen egy programot Java vagy Python nyelven, amely egy lapcsere-rendszer működését szimulálja!

A program bemeneteként memóriaműveletek során hivatkozott lapok azonosítóit kapja a hivatkozásuk sorrendjében. Kimeneteként a végrehajtott lapcserék eredményeképpen lefoglalt fizikai memóriakeretek azonosítóit és a laphibák számát adja vissza.

A rendszerben 3 memóriakeret található, amelyek kezdetben mind üresek. Az induláskor a lapok a cserehelyen találhatók.

A lapokat számok (1-99), a kereteket betűk (A,B és C) jelölik.

## Bemenet (standard input, stdin)
Egyetlen sorban a lapokra történő hivatkozások egymástól vesszővel elválasztva. Például:

1,2,3,-1,5,-1\
A negatív számok írási műveleteket jeleznek a megadott lapon; ekkor a keretek "dirty" jelzést kapnak (ez nem minden algoritmus esetén releváns információ, de a bemeneten előfordulhat).

A bemenet végét EOF jelzi (előtte soremelés, üres sor lehet). Ekkor kell a kimenetre kiírni az eredményt.

## Kimenet (standard output, stdout)
A kimeneten az első sorban a bemeneti memóriahivatkozások kiszolgálásához lefoglalt memóriakeretek betűjelei szerepelnek a megfelelő sorrendben, szóközök nélkül, egybeírva, majd a következő sorban a laphibák száma. A kiírt eredmények előtt, után üres karakterek, további sorok ne legyenek!
Amennyiben egy memóriahivatkozáshoz nem kellett új keretet foglalni (már a memóriában volt a lap), a kimeneten az adott pozícióban "-" jel jelenik meg.
Ha egy memóriafoglalás nem teljesíthető (nincs szabad keret és egyetlen keret sem szabadítható fel), akkor a kimeneten "*" karakter jelenik meg (a műveletet nem ismétli meg az algoritmus). Ez utóbbi eset értelemszerűen nem minden algoritmusnál fordulhat elő.

Megvalósítandó algoritmus\
Újabb esély (SC) lapcsere maximum 3 lépésig tartó tárba fagyasztással

A program írja ki az algoritmus szerinti memóriafoglalásokat és a laphibák számát!
Pl. a fenti bemenetre adott válasz:

ABC-AB\
5

### Értékelés
Összesen 3 pont jár, ha minden teszten átmegy a megoldás. Arányosan kevesebb pont szerezhető, ha nem minden esetben működik helyesen a beküldött program.

### Technikai információk
A programot a HF portálon kell leadni a megadott határidőig egyetlen ZIP fájlba csomagolva. A feltöltött fájlok (a ZIP és a tartalmának) neve ékezetes betűt és szóközt ne tartalmazzon!

A portál automatikusan kiértékeli a programot, és visszajelzést küld a működéséről. A kiértékelésre nincs időbeli garancia. A program bármikor újra beküldhető a határidőig. A beadási határidő leteltekor a legutolsó feltöltött program beadottá válik, annak értékelése adja a végleges pontszámot.

A beküldött Java 8 programnak tartalmaznia kell egy "Main" nevű osztályt, melynek része a feladatot megoldó "main" függvény. A Java program tetszőleges számú forrásfájlból állhat. A program nem használhat a standard inputon és outputon kívül semmilyen más erőforrást, így nem végezhet fájlműveleteket és nem nyithat hálózati kapcsolatokat.

Python megoldás beküldése esetén a Python 3 verzióval kompatibilis megoldásokat fogadunk el, csak standard függvények használhatók (külső könyvtár, pl. NumPy nem), és a feltöltött ZIP fájlban egy db .py fájl lehet, más nem. Itt sem végezhetnek fájlműveleteket, nem nyithatnak meg hálózati kapcsolatokat.

### Tesztadatok
Az első beküldés előtt érdemes az alábbi tesztekkel megpróbálkozni.

1,2,3,5,4,2\
ABC*A-\
5

1,2,3,2,4,3,2,1\
ABC-A--B\
5

1,2,3,3,4,5,2,1\
ABC-ABC*\
7

1,2,3,4,5,4,3,2,1\
ABC*AB-CA\
8

-5,2,5,3,2,1,-3\
AB-C-A-\
4

A fagyasztott keretek kezelése vitatható. Eljárhatnánk úgy, mintha újabb esélyt kapnának (azaz a FIFO végére kerülnek), de ez nem tükrözné az SC abbéli törekvését, hogy valahol a használati időt veszi figyelembe. Ezért az ilyen kereteket hagyjuk meg a helyükön a FIFO-ban (csak ne használjuk azokat)!

Példa:

1,2,3,4,1,5,1,3,6,3\
ABC*-B--CB\
7
