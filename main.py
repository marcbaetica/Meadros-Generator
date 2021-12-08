from lib.SimpleMeandros import SimpleMeandros
from time import sleep


PEN_SIZE = 5
STROKE_SPEED = 15
PEN_COLOR = 'white'
BACKGROUND_COLOR = 'blue'


# sleep(1)
meandros = SimpleMeandros(PEN_SIZE, STROKE_SPEED, PEN_COLOR, BACKGROUND_COLOR)
meandros.draw(12, 10)
meandros = SimpleMeandros(PEN_SIZE, STROKE_SPEED, PEN_COLOR, BACKGROUND_COLOR)
meandros.draw(2, 2)
sleep(30)
