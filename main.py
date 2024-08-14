# https://pypi.org/project/pytesseract/

from PIL import Image
import pytesseract
from gtts import gTTS
from playsound import playsound

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def run(filename):
    # Manual
    # image = Image.open('./images/nutri-info.jpeg')
    # Dynamic
    image = Image.open("./images/" + filename)

    text = pytesseract.image_to_string(image, lang='eng')

    tts = gTTS(text=text, lang='en')
    tts.save("./audios/output.mp3")
    playsound("./audios/output.mp3")

    # TXT file conversion possibly irrelevant
    with open('output.txt', 'w') as file:
        file.write(text)
        print(text)

if __name__ == "__main__":
    filename = input("Picture to be converted to text: ")
    run(filename)