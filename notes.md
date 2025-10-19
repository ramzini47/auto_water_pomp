#### Zasilacz zewnetrzny
Bialy to prad w zsilczczu

#### Podlaczenie pompki wodnej
Pomka wodna podlaczona jest do zasilacza zewnetrznego oraz modulu sterujacego.
Do sterowania pomka uzywajac modulu ULN2003 i zewnetrznego zasilania GND raspery pi,
sternownika i pompki musza miec wspolna mase. Czerwony kabel zasilania pomki podlaczamy
do zewnetrzengo zasilania. Nie-czerwony kabel(GND) pompki bedzie podlaczony do sterniownika w A-D.
GND rasperry pi, GND sterownika i GND zasilacza zewetrzenego nalezy polaczyc.
VCC sterownika nalezy polaczyc z VCC zasilacza zewnetrznego(czerwony kabel).
IN1-7 nalezy polaczyc z GPIO pinem raspery pi ktory bedziemy programowo wlaczac/wylaczac.

#### Czujnik wilgotnosci
Musze podlaczyc czujnik zeby czytal czy wiglotno czy nie
Potem zrobic jakas logike ze jak nie jest wulgotna to zacznij pompowac wode az czujnik nie powie ze juz wilgotnai
Czujnik ma VCC GND D0 ktor trzeba odpowiednio podlaczyc. VCC bezposrednio do zasilania
GND do wspolnej masy pomiedzy wszystkimi ukladami. D0 do pini na boardzie pini16 (GPIO17)
Wachania pradu zaburzaja odczyt wilgotnosci: TODO - trzeba rozkminic jak to zasilic i jak czeto sprawdzac wilgotnosc
Jak wgl bede mierzyl to ze juz trzeba podlewac?

#### Zawort magnetyczny 
Trzeba bylo wiecej Voltow dac z zewnetrznego zasilania zeby zawoir 5v dzialal
When power off, inlet A and outlet B are open, outlet C closed.
When power on, inlet A and outlet C open, outlet B closed.

#### ~ - woda
GPIO.HIGHT
```
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
```

Unfornetury moisture sensor failed. Need some sothering to fix it

