from email.policy import default
import PySimpleGUI as sg
import random

layout = [
    [sg.Text(f"Guess a number!", key="_RANGE_")],
    [sg.Input(size=(5, 0), key="_IN_")],
    [
        sg.Radio("Easy", "difficulty", key="easy", default=True),
        sg.Radio("Medium", "difficulty", key="medium"),
        sg.Radio("Hard", "difficulty", key="hard"),
        sg.Radio("impossible", "difficulty", key="impossible"),
    ],
    [sg.Button("Start", key="_BUTTON_")],
    [sg.Output(size=(40, 10), key="_OUTPUT_")],
]


class Screen:
    def __init__(self):
        self.window = sg.Window("Guess a number", layout, element_justification="c")

    def start(self):

        # game loop
        while True:
            self.button, self.values = self.window.Read()

            # dificulty
            min = 0
            max = 0

            if self.values["easy"]:
                random_num = random.randint(0, 25)
                max = 25

            elif self.values["medium"]:
                random_num = random.randint(0, 50)
                max = 50

            elif self.values["hard"]:
                random_num = random.randint(0, 100)
                max = 100

            elif self.values["impossible"]:
                random_num = random.randint(0, 500)
                max = 500

            # updade text
            self.window["_RANGE_"].Update(f"Guess a number between {min} and {max}!")
            self.window["_BUTTON_"].Update("OK!")
            # update button

            # verify is a valid number
            if not self.values["_IN_"]:
                print("Please enter a number")

            # verify if the number is in range
            else:
                usr_value = int(self.values["_IN_"])

                if random_num == usr_value:
                    print(f"U got it! Is {random_num}!!")

                elif random_num > usr_value:
                    print("Too low!")
                    self.window["_IN_"].Update("")

                elif random_num < usr_value:
                    print("Too high!")
                    self.window["_IN_"].Update("")


screen1 = Screen()
screen1.start()
