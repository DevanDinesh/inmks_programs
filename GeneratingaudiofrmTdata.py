from gtts import gTTS
import os
text="Today is good day"
output=gTTS(text=text,lang='en',slow=False)
output.save('output.mp4')
os.system('start output.mp4')
# output.save('output.mp3')
# os.system('start output.mp3')