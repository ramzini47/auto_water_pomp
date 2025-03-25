Bialy to prad w zsilczczu

Pomka podlaczenie:
Czerowny kabelek do 5VD na rasperyPI
Czarny kabelek do A pinu
IN1 podlaczony do PINU(18) ktory ma zarzadzac wlaczenie/wylacznie


18 - pompka wodna
16 - zawor

Trzeba bylo wiecej Voltow dac z zewnetrznego zasilania zeby zawoir 5v dzialal

#######
Podlaczenie pompki wodnej
Pomka wodna podlaczona jest do zasilacza zewnetrznego oraz modulu sterujacego.
Czerwony kabel z zasilacza to prad ktry podpinamy dezposrednio do zasialacza.
Bialy kabel podlaczamy do GND w tym samym miejscu w ktrym GND z sterownika
Sterownik podpisanmy z jednej strony PIN A do czarnegego kabla pomki wodnej,
a z drugiej pin IN1 (dokladnie przeciwny do PINu A) do pinu 18 na boardzie (GPIO24)

----- Czujnik wilgotnosci ----
Musze podlaczyc czujnik zeby czytal czy wiglotno czy nie
Potem zrobic jakas logike ze jak nie jest wulgotna to zacznij pompowac wode az czujnik nie powie ze juz wilgotnai
Czujnik ma VCC GND D0 ktor trzeba odpowiednio podlaczyc. VCC bezposrednio do zasilania
GND do wspolnej masy pomiedzy wszystkimi ukladami. D0 do pini na boardzie pini16 (GPIO17)
Wachania pradu zaburzaja odczyt wilgotnosci: TODO - trzeba rozkminic jak to zasilic i jak czeto sprawdzac wilgotnosc
Jak wgl bede mierzyl to ze juz trzeba podlewac?
------ Zawort magnetyczny ----------------
When power off, inlet A and outlet B are open, outlet C closed.
When power on, inlet A and outlet C open, outlet B closed.

~ - woda
GPIO.HIGHT
_________________
   |        |
~~~~~~~~~~~~~~~~~~~~~~
___|        |____
    |       |
    |       |____
    |_______|____
    |METAL PART|

GPIO.LOW
_________________
   |        |
~~~~~~~~~~~~|
___|~~~~~~~~|_____
    |~~~~~~~~~|
    |~~~~~~~~~|
    |~~~~~~~~~|___
    |~~~~~~~~~~~~~~~~~
    |____________
    |METAL PART|