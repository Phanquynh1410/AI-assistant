import tkinter as tk
from tkinter import *
from turtle import window_width
import customtkinter

import func.listen
import func.understand
import func.say

root = tk.Tk()
#window
root.title('Lexas Assistant')
root.geometry('500x500')
root.resizable(False, False)
root.config(bg="#000000")

#img
voice_wait_img = PhotoImage(file=r"D:\School\Report\final_project\module_file\image\cham.png")
voice_img = PhotoImage(file = r"D:\School\Report\final_project\module_file\image\voice_rm.png")

#btn
# def listen():
#     voice_btn = customtkinter.CTkButton(master=root, text="", image=voice_wait_img, command=lambda: not_listen())
#     voice_btn.place(relx=0.07, rely=0.93, anchor=customtkinter.CENTER, height=40, width=40)
#
# def not_listen():
#     voice_btn = customtkinter.CTkButton(master=root, text="", image=voice_img, command=lambda: listen())
#     voice_btn.place(relx=0.07, rely=0.93, anchor=customtkinter.CENTER, height=40, width=40)

#Use CTkButton instead of tkinter Button
voice_img = PhotoImage(file = r"D:\School\Report\final_project\module_file\image\voice_rm.png")
voice_btn = customtkinter.CTkButton(master=root,text="", image=voice_img)
voice_btn.place(relx=0.07, rely=0.93, anchor=customtkinter.CENTER, height=40, width=40)

send_btn = customtkinter.CTkButton(master=root, text="Send")
send_btn.place(relx=0.91, rely=0.93, anchor=customtkinter.CENTER, height=40, width=60)

#input
entry = customtkinter.CTkEntry(master=root, placeholder_text="You can right here if I don't listen")
entry.pack(pady=12, padx=10)
entry.place(relx=0.14, rely=0.89, height=40, width=347)

#msg

#left
frame_left = LabelFrame(root, text="Robot", font=("helvetica", 13),bg= '#000000', fg='#ffffff')
frame_left.pack(pady=10)

message_left = Message(frame_left, text="sjfokdsjfkdjfsjfodjfsjfosjfkdnfskfskjbfkjsnfkjnfsknfdsfjdnfsknf", font= ("helvetica", 10), bg= '#000000', fg='#ffffff', aspect=500, justify=LEFT )
message_left.pack(pady=5, padx=5)



root.mainloop()