import PySimpleGUI as sg
import random
import time

layout = [
    [sg.Text("How many rows?")],
    [sg.Input(size=(5, 0), key="rows", default_text="1")],
    [sg.Text("Sides")],
    [
        sg.Radio("D4", "dice", key="4"),
        sg.Radio("D6", "dice", key="6", default=True),
        sg.Radio("D8", "dice", key="8"),
        sg.Radio("D10", "dice", key="10"),
        sg.Radio("D12", "dice", key="12"),
        sg.Radio("D20", "dice", key="20"),
    ],
    [sg.Button("Roll Out!")],
    [sg.Output(size=(40, 10), key="_output_")],
]


class Screen:
    def __init__(self):
        self.window = sg.Window("Dice Roller", layout,element_justification='c')

    def start(self):
        while True:

            self.button, self.values = self.window.Read()
            self.window.FindElement("_output_").Update("")

            rows = int(self.values["rows"]) #if self.values["rows"] else 1 
            dice_sides = 6
            dice_number = []

            # define sides
            for sides in ["4", "6", "8", "10", "12", "20"]:
                if self.values[f"{sides}"]:
                    dice_sides = int(sides)


            for i in range(rows):
                dice_number.append(random.randint(1, dice_sides))

                print(f"Dice {i+1} Roll on D{dice_sides}: {dice_number[i]}")
                #time.sleep(0.1)
                
            print(f"\nMax: {max(dice_number)} | Min: {min(dice_number)} | Average: {sum(dice_number)/len(dice_number)}", end="")


screen1 = Screen()
screen1.start()
