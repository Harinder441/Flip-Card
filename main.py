#attach voice
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
from tkinter import *
import pandas as pd
import time


data = pd.read_csv("./data/french_words.csv")

#----------------------------------UI Functions-----------------------------------------------------
random_word = data.sample()
def french():
    """ get french word from random sample""""
    canvas.itemconfig(bg_image,image = card_front_image)
    canvas.itemconfig(language,text ="French", fill ="black")
    canvas.itemconfig(word, text =f"{random_word.French.item()}", fill ="black")
def english():
     """ get english word word from random sample""""
    canvas.itemconfig(bg_image,image = card_back_image)
    canvas.itemconfig(language,text ="English", fill ="white")
    canvas.itemconfig(word, text =f"{random_word.English.item()}", fill ="white")




def start():
    """Show english word at begning , french translation after some delay """
    global random_word
    random_word = data.sample()
    french()
    win.after(10000, english)


def right():
    """ this function remove the known french words from sample """
    data.drop(random_word.index,axis=0,inplace=True)
    data_csv = data.to_csv(index=False)
    with open("./data/french_words.csv","w") as file:
        file.write(data_csv)
    start()


def wrong():
    start()

#-----------------------------------------UI---------------------------------------------------
win = Tk()
win.title("Flash Card")
win.config(pady= 50,bg=BACKGROUND_COLOR,padx=10)
card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")
canvas = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
bg_image=canvas.create_image(400,263,image = card_back_image)
language = canvas.create_text(400,120, text="English" , font=(FONT_NAME, 30, "normal"),fill="white")
word = canvas.create_text(400,240, text=f"{random_word.English.item()}" , font=(FONT_NAME, 40, "bold"),fill="white")
# canvas.tag_bind(bg_image, '<Button-1>', lambda e :french() )
canvas.grid(row =0 , column=0 ,columnspan=2)
wrong_image = PhotoImage(file="./images/wrong.png")

wrong_button  = Button(image= wrong_image,command=wrong)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")

right_button  = Button(image= right_image,command=right)
right_button.grid(row=1, column=1)
start()


win.mainloop()
