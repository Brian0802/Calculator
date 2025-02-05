from customtkinter import CTk, CTkTextbox
from tkinter import messagebox
import math
          
class Calculator:
    def __init__(self, root: CTk):
        self.root = root
        self.calculation = ""
        self.tab = "tab1"
        self.text_result = CTkTextbox(self.root, 
                             height=50, 
                             width=320, 
                             font=("Arial", 30, "bold"), 
                             bg_color="black")
        self.text_result.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
        self._handle_keypress()

    def _handle_keypress(self):
        self.root.bind("<Key-Escape>",lambda event: self.root.destroy())

    def switch_tab(self):
        from button_layout import ButtonLayout
        if self.tab == "tab1":
            self.tab = "tab2"
            self.clear_buttons()
            for i, (text, cmd) in enumerate(ButtonLayout.tab_2(self)):
                self._create_custom_button(text, cmd, row=i//4+1, column=i%4)
        else:
            self.tab = "tab1"
            self.clear_buttons()
            for i, (text, cmd) in enumerate(ButtonLayout.tab_1(self)):
                self._create_custom_button(text, cmd, row=i//4+1, column=i%4)
    
    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, self.calculation)
    

    def evaluate_calculation(self):
        try:
            self.calculation = str(eval(self.calculation))
            self.text_result.delete(1.0, "end")
            self.text_result.insert(1.0, self.calculation)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed")
            self.clear_field()
        except SyntaxError:
            messagebox.showerror("Error", "Invalid expression")
            self.clear_field()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.clear_field()

    def direct_calculation(self, operation):
        if self.calculation != "":
            try:
                if operation == 'sqrt':
                    self.calculation = str(math.sqrt(eval(self.calculation)))
                elif operation == 'log':
                    self.calculation = str(math.log10(eval(self.calculation)))
                elif operation == 'ln':
                    self.calculation = str(math.log(eval(self.calculation)))
                elif operation == 'sin':
                    self.calculation = str(math.sin(math.radians(eval(self.calculation))))
                elif operation == 'cos':
                    self.calculation = str(math.cos(math.radians(eval(self.calculation))))
                elif operation == 'tan':
                    self.calculation = str(math.tan(math.radians(eval(self.calculation))))
                elif operation == '**2':
                    self.calculation = str(eval(self.calculation) ** 2)
                elif operation == 'pow':
                    self.calculation = str(self.base ** float(self.calculation))
                self.text_result.delete(1.0, "end")
                self.text_result.insert(1.0, self.calculation)
            except Exception as e:
                self.clear_field()
                messagebox.showwarning(title="ERROR", message=f"{e}")

    def x_pow_y(self):
        if self.calculation:
            self.base = float(self.calculation)  # Store the base number
            self.calculation = ''  # Clear current calculation
            self.text_result.delete(1.0, "end")  # Clear display
            self.operation = 'pow'  # Mark that we're doing power operation
            return True

    def backward(self):
        if self.calculation is not None:
            self.calculation = self.calculation[:-1]
            self.text_result.delete(1.0, "end")
            self.text_result.insert(1.0, self.calculation)

    def clear_buttons(self):
        # Clear all widgets except the text result (which is in row 0)
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:  # Don't remove the text result
                widget.destroy()

    def clear_field(self):
        self.calculation = ""
        self.text_result.delete(1.0, "end")

