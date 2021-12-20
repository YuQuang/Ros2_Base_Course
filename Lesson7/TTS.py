from gtts import gTTS
import os 
# Language we want to use 
# en, zh-TW
language = 'zh-tw'

text2trans = input(f"Enter an text to translate ({ language }) => ")
output = gTTS(text=text2trans, lang=language, slow=False)
output.save("output.mp3")
# Play the converted file 
os.system("start output.mp3")