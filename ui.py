import tkinter as tk
import customtkinter as ctk

from config import Config
from counter import character_counter

class RenderUi():

    def __init__(self):
        self.window = ctk.CTk()
        self.label = None
        self.users_input = None
        self.label2 = None
        self.users_output = None
        self.button = None
        self.config = Config()

    def render_ui(self):
        ctk.set_appearance_mode(self.config.APP)
        ctk.set_default_color_theme(self.config.COLOR)
        self.build_ui()
        self.label.pack()
        self.users_input.pack()
        self.label2.pack()
        self.users_output.pack()
        self.button.pack()
        self.window.mainloop()
    
    def build_ui(self):
        self.window.title(self.config.TITLE)
        self.window.geometry(self.config.DIMENSIONS)
        self.label = tk.Label(self.window, text=self.config.DESCRIPTION)
        self.format_users_input(self.window)
        self.users_output = tk.Text(self.window, width=20, height=2, font=(self.config.FONT, 20), wrap=self.config.WRAP)
        self.render_buttons()
    
    def format_users_input(self, window):
        self.users_input = tk.Text(window, width=150, height=10, font=(self.config.FONT, 20), wrap=self.config.WRAP)
        self.decision = tk.IntVar()

    def render_buttons(self):
        self.button = ctk.CTkButton(
            self.window, 
            text=self.config.BUTTON, 
            command=self.do_count_words
        )
        self.label2=tk.Label(self.window, text=self.config.LABEL)


    def do_count_words(self):
        self.users_output.delete(0.0, self.config.INDEX)
        words = self.users_input.get(0.0, self.config.INDEX)
        counter = character_counter(words)
        counter = self.show_warning_popup(counter)
        self.users_output.insert(tk.INSERT,counter)
    
    def show_warning_popup(self, counter):
        if counter == 0:
            counter = self.config.WARNING
            tk.messagebox.showwarning(self.config.WARNING_TITLE,  self.config.WARNING_BODY)
        return counter