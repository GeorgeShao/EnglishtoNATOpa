import os
import sys
from gtts import gTTS
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('EnglishtoNATOpa')

        self.text = QLabel("(NATO phonetic alphabet result will appear here)")
        self.textbox = QLineEdit("Enter English Text to Convert Here")
        self.button = QPushButton("Convert")
        self.button2 = QPushButton("Speak")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button.clicked.connect(self.magic)
        self.button2.clicked.connect(self.magic2)

    @Slot()
    def magic(self):
        print("Input: " + str(self.textbox.text()))
        output = ""
        self.text.setText("Converting...")

        first_letter_in_word = True

        for char in str(self.textbox.text().lower()):
            if first_letter_in_word == False:
                if char != " ":
                    output = output + "-"
            if char == " ":
                first_letter_in_word = True
                output = output + " "
            else:
                first_letter_in_word = False
            if char == "a":
                output = output + "Alpha"
            elif char == "b":
                output = output + "Bravo"
            elif char == "c":
                output = output + "Charlie"
            elif char == "d":
                output = output + "Delta"
            elif char == "e":
                output = output + "Echo"
            elif char == "f":
                output = output + "Foxtrot"
            elif char == "g":
                output = output + "Golf"
            elif char == "h":
                output = output + "Hotel"
            elif char == "i":
                output = output + "India"
            elif char == "j":
                output = output + "Juliett"
            elif char == "k":
                output = output + "Kilo"
            elif char == "l":
                output = output + "Lima"
            elif char == "m":
                output = output + "Mike"
            elif char == "n":
                output = output + "November"
            elif char == "o":
                output = output + "Oscar"
            elif char == "p":
                output = output + "Papa"
            elif char == "q":
                output = output + "Quebec"
            elif char == "r":
                output = output + "Romeo"
            elif char == "s":
                output = output + "Sierra"
            elif char == "t":
                output = output + "Tango"
            elif char == "u":
                output = output + "Uniform"
            elif char == "v":
                output = output + "Victor"
            elif char == "w":
                output = output + "Whiskey"
            elif char == "x":
                output = output + "X-ray"
            elif char == "y":
                output = output + "Yankee"
            elif char == "z":
                output = output + "Zulu"
            else:
                output = output + char

        self.text.setText(output)
        print("Output: " + output)

    def magic2(self):
        TTSobj = gTTS(text=self.text.text(), lang='en', slow=False)
        TTSobj.save("TTSobj.mp3")
        os.system("start TTSobj.mp3")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 300)
    widget.show()

    sys.exit(app.exec_())