import tkinter as tk
from tkinter import *
import func.listen
import func.understand
import func.say

root = tk.Tk()
root.title('Lexas Assistant')
window_width = 500
window_height = 500
root.resizable(False, False)
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


def send():
        robot_listen = func.listen.listen()
        robot_brain = func.understand.understand(robot_listen)
        # robot_say = func.say.say(robot_brain)

        brain = "Robot: I'am listening..."
        you = "You: "+robot_listen
        # reply = "Robot: "+robot_say

        txt.insert(END, "\n" +brain)
        txt.insert(END, "\n" +you)
        # you.delete(0, END)
        # txt.insert(END, "\n" +reply)
        # reply.delete(0, END)

txt = Text(root, bg="#000000", fg="#ffffff", font=FONT, width=60, )
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)

root.mainloop()