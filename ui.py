from calculator import Calculator
import customtkinter as ctk
from customtkinter import CTkButton
from button_layout import ButtonLayout

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class UI(Calculator):
    def __init__(self, root):
        super().__init__(root)
        for i, (text, cmd) in enumerate(ButtonLayout.tab_1(self)):
            self._create_custom_button(text, cmd, row=i//4+1, column=i%4)

    def _create_custom_button(self, text, command, row, column):
        button = CTkButton(self.root, 
                           text=text, 
                           command=command, 
                           font=("Arial", 20, "bold"), 
                           width=70, 
                           height=70)
        button.grid(row=row, column=column, padx=10, pady=10)