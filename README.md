# pictureToText

**pictureToText** is a Python program that converts images to text and then reads the text aloud using Google Text-to-Speech (gTTS). It utilizes the `pytesseract` library for Optical Character Recognition (OCR) and the `playsound` library to play the generated audio.

## Features

- **Image to Text Conversion**: Extracts text from images using `pytesseract`.
- **Text-to-Speech**: Converts the extracted text to speech using `gTTS`.
- **Audio Playback**: Plays the generated audio file.
- **Optional Text Output**: Saves the extracted text to a `.txt` file (optional feature).

## Installation

1. **Install Required Libraries**:
   ```bash
   pip install pytesseract pillow gtts playsound
   ```
   
2. **Tesseract Installation**:
   - Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
   - Update the `tesseract_cmd` path in the script if necessary:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
     ```

## Usage

1. **Prepare Your Image**:
   - Place the image you want to convert in the `./images/` directory.

2. **Run the Program**:
   - Run the script and provide the image filename when prompted:
     ```bash
     python main.py
     ```
   - Example:
     ```
     Picture to be converted to text: nutri-info.jpeg
     ```

3. **Output**:
   - The extracted text will be printed to the console.
   - The program will save the generated speech as an `output.mp3` file in the `./audios/` directory and play it.
   - The extracted text will also be saved to `output.txt` (this can be removed if not needed).
