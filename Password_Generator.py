#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import random
import array
from tkinter import messagebox

def submit_action():
    user_input = entry.get()
    MAX_LEN = int(user_input)

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass += random.choice(COMBINED_LIST)

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password += x
        
    result_label.config(text=f"Result: {password}")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

root = tk.Tk()
root.title("Password Generator")

heading_label = tk.Label(root, text="Welcome to Password Generator", font=("Helvetica", 16))
input_label = tk.Label(root, text="Enter the Desired Length :")
entry = tk.Entry(root)
submit_button = tk.Button(root, text="Submit", command=submit_action)
result_label = tk.Label(root, text="", font=("Helvetica", 20))

heading_label.grid(row=0, column=0, columnspan=2, pady=10)
input_label.grid(row=1, column=0, pady=5)
entry.grid(row=1, column=1, pady=5)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

