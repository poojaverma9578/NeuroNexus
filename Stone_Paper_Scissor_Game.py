#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import random
from tkinter import messagebox

def show_continue_prompt():
    result = messagebox.askquestion("Continue?", "Do you want to continue?")
    if result == 'yes':
        result_label.config(text="")
        main_page()
    else:
        root.destroy()

def button_clicked(user_choice):
    show=""
    choices=['stone','paper','scissors']
    chosen=random.choice(choices)
    if(user_choice==chosen):
        show=f"I chose {chosen} \nOops! We got a tie..."
    else:
        if(user_choice=='stone' and chosen=='paper' or user_choice=='paper' and chosen=='scissors' or user_choice=='scissors' and chosen=='stone'):
            show=f"I chose {chosen} \nYayy! I won"
        else:
            show=f"I chose {chosen} \nCongrats! You won"
    
    result_label.config(text=show)
    result_label.grid(row=2, column=0, columnspan=3,pady=10)
    root.after(2000, show_continue_prompt)

def main_page():
    global result_label
    heading_label = tk.Label(root, text="Let's Play Stone - Paper - Scissors\nMake your Choice", font=("Helvetica", 16))
    button1 = tk.Button(root, text="Stone", command=lambda: button_clicked("stone"))
    button2 = tk.Button(root, text="Paper", command=lambda: button_clicked("paper"))
    button3 = tk.Button(root, text="Scissors", command=lambda: button_clicked("scissors"))
    result_label = tk.Label(root, text="", font=("Helvetica", 20))

    # Arrange the widgets using grid layout
    heading_label.grid(row=0, column=0, columnspan=3, pady=10)
    button1.grid(row=1, column=0, padx=10, pady=5)
    button2.grid(row=1, column=1, padx=10, pady=5)
    button3.grid(row=1, column=2, padx=10, pady=5)

    
root = tk.Tk()
root.title("Game")

main_page()
    
root.mainloop()

