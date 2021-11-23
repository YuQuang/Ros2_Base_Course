import time
from pygame import mixer 
mixer.init()
mixer.music.load('test.mp3')
mixer.music.play()
while mixer.music.get_busy() == True:continue
mixer.music.stop()
mixer.quit()