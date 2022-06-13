cd /home/pi/radio/PiFmRds/src
ffmpeg -loglevel fatal -re -i https://listen.radioking.com/radio/276343/stream/321985 -f wav pipe:1  | sudo ./pi_fm_rds -audio - -freq 96.9 -ps Muzika -rt 'Radio Muzika len pre vas Karolko.'
