from lib.Degree2Meandros import Degree2Meandros
from lib.Degree3Meandros import Degree3Meandros
from lib.Degree4Meandros import Degree4Meandros
from lib.SimpleMeandros import SimpleMeandros
from time import sleep


PEN_SIZE = 5
STROKE_SPEED = 15
PEN_COLOR = 'white'
BACKGROUND_COLOR = 'blue'


meandros = Degree3Meandros(PEN_SIZE, STROKE_SPEED, PEN_COLOR, BACKGROUND_COLOR)
meandros.draw(12, 10)
meandros = Degree2Meandros(PEN_SIZE, STROKE_SPEED, PEN_COLOR, BACKGROUND_COLOR)
meandros.draw(2, 2)
sleep(30)
