from tkinter import *
from turtle import window_width
import customtkinter
import time

import func.listen
import func.understand
import func.say

class ChatApp:

    def __init__(self):
        self.win = Tk()
        self._setup_main_win()
        brain = "I'am listening..."
        self._insert_message("Robot", brain)

    def run(self):
        self.win.mainloop()

    def _setup_main_win(self):
        self.win.title('Lexas Assistant')
        self.win.geometry('500x500')
        self.win.resizable(False, False)
        self.win.config(bg="#000000")

        self.txt_widget = Text(self.win, width=450, bg="#000000", height=2, fg="#ffffff", padx=5, pady=5)
        self.txt_widget.place(relheight=0.855, relwidth=1, rely=0.01)
        self.txt_widget.configure(cursor="arrow", state=DISABLED)

        # scrollbar
        self.scrollBar = Scrollbar(self.txt_widget)
        self.scrollBar.place(relwidth=1, relheight=1, relx=0.974)
        self.scrollBar.configure(command=self.txt_widget.yview)

        # Bottom
        # Use CTkButton instead of tkinter Button
        self.voice_img = PhotoImage(file=r"D:\School\Report\final_project\module_file\image\voice_rm.png")
        self.voice_btn = customtkinter.CTkButton(master=self.win, text="", image=self.voice_img, command=lambda: self.listening(None))
        self.voice_btn.place(relx=0.07, rely=0.93, anchor=customtkinter.CENTER, height=40, width=40)

        self.send_btn = customtkinter.CTkButton(master=self.win, text="Send", command=lambda: self.send(None))
        self.send_btn.place(relx=0.91, rely=0.93, anchor=customtkinter.CENTER, height=40, width=60)

        # input
        self.entry = customtkinter.CTkEntry(master=self.win)
        self.entry.place(relx=0.14, rely=0.89, height=40, width=347)
        self.entry.focus()
        self.entry.bind("<Return>", self.send)

    def send(self, event):
        print("ok")
        msg = self.entry.get()
        print(msg)
        # self.txt_widget.insert(END, "\n" + msg)
        self._insert_message("You", msg)

    def _insert_message(self, sender, msg):
        if not msg:
            return

        self.entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.txt_widget.configure(state=NORMAL)
        self.txt_widget.insert(END, msg1)
        self.txt_widget.configure(state=DISABLED)

        self.txt_widget.see(END)


    def listening(self, event):
        brain = "I'am listening..."
        self._insert_message("Robot: ", brain)

        robot_listen = func.listen.listen()
        robot_brain = func.understand.understand(robot_listen)
        self._insert_message("You: ", robot_listen)
        self._insert_message("Robot: ", robot_brain)

        func.say.say(robot_brain)



if __name__ == "__main__":
    app = ChatApp()
    app.run()