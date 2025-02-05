import customtkinter as ctk
from ui import UI

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Calculator")
    root.geometry("360x720")
    root.resizable(False,False)
    app = UI(root)
    root.mainloop()