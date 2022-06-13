# RPi-Radio - Internetove radio cez Raspberry PI Zero

Python script na prihlasenie sa na internet cez USB modul (Wifi internet cez orange)
a nasledne online prehravania radia cez Raspberry pi a RPIO, kde staci jeden kablik ako antena

Testovane na Raspberry Pi Zero W+
	- vyzaduje wifi, pre pripojenie internetu

Vyzaduje
- Python
- PiFmRds (github)
- FFmpeg (balik)


Prikaz na spustenie radia:
	cd /home/pi/radio/PiFmRds/src
	ffmpeg -loglevel fatal -re -i https://listen.radioking.com/radio/276343/stream/321985 -f wav pipe:1  | sudo ./pi_fm_rds -audio - -freq 96.9 -ps Muzika -rt 'Radio Muzika len pre Vas!'
	 

Instalacia kniznice na prehravanie radia cez RPIO
	https://github.com/ChristopheJacquet/PiFmRds
  
Instalacia FFmpeg:
	sudo apt update
	sudo apt install -y ffmpeg
	

cez FFMpeg sa zavola spustenie online radia (da sa navolit lubovolne), kde cez PiFmRds sa vytvori transmitter na pozadovanej frekvencii (96.9).
+ pridany auto post pre orange internet, kedze je to datovo limitovany internet, a treba ho po precerpani dat aktivovat
- Sim karta za 1€ mesacne s limitom 100MB, kde po precerpani padne rychlost na 128/128kb s neobmezenym prenosom dat, kde 
prenosovva rychlost staci na prehravanie online radia (radio vyzaduje 32 / 64 / 128 podla kvality...)

Staci uz len na radiu naladit prislusnu stanicu :)