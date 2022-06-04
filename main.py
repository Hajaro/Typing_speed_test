from english_words import english_words_lower_set
import tkinter as tk
from tkinter import ttk
import random

game_on = False

count = 0
string_of_words = ""
for element in english_words_lower_set:
    string_of_words += element
    count += 1
    if count == 216:
        break


def start_timer():
    global game_on
    if not game_on:
        game_on = True
        count_down(60)



def count_down(count):
    global game_on
    if count >= 0 and game_on == True:
        global timer
        timer = window.after(1000, count_down, count - 1)
        l1.config(text=f"{count}")
    else:
        game_on = False



window = tk.Tk()
window.title("Typing speed test")
window.config(padx=25, pady=10)

my_font1=('times', 18, 'bold')
l1 = tk.ttk.Label(window, text='60', width=30, font=my_font1)
l1.grid(row=1, column=0)


b1 = tk.ttk.Button(window, text='Start the test',
   width=20, command=start_timer)
b1.grid(row=2, column=0)
l2 = tk.ttk.Label(window, text='Word', width=30, font=my_font1)
l2.grid(row=3, column=0)


while game_on:
    word = random.choice(tuple(english_words_lower_set))
    l2.config(text=f"{word}")

window.mainloop()