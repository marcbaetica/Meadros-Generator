from lib.SimpleMeandros import SimpleMeandros
from time import sleep


PEN_SIZE = 5
STROKE_SPEED = 15
PEN_COLOR = 'black'
BACKGROUND_COLOR = 'white'
MEANDROS_TYPE = 'line'


# sleep(1)
meandros = SimpleMeandros(PEN_SIZE, STROKE_SPEED, PEN_COLOR, BACKGROUND_COLOR, MEANDROS_TYPE)
meandros.draw()
sleep(30)
