#imports

import tkinter as tk
import csv
import pandas as pd
from PIL import Image, ImageTk


root=tk.Tk()
root.title("Textbox Input")
root.configure(background='SteelBlue1')
root.attributes('-topmost', 1)


frame=tk.Frame(root, bg='SteelBlue1')
frame.grid()


window_width = 900
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#root.resizable(0,0)
#^ this stops window from being resized but its helpful for it to be movable while the framework of the gui is changing

passport=0

#The function for getting the text in the textbox and putting it in the lbl Label
def retrieve_input():
    inp = inputtxt.get("1.0","end-1c")
    lbl.config(text="Input Text : "+inp)

#This function as of now just iterates through the csv 
#but is very flexable and eventually will also iterate through the images to show what the image the OCR had to work with

def nextpass():
    global passport
    passport = passport+1
    Temp=pd.read_csv("Testing.csv")
    PassData=Temp.iloc[passport]
    for i in range(0,len(Cat)):
        df=tk.Label(frame, text=Cat[i]+" : "+PassData[i]).grid(column=2,row=i)


#this is the same as the Next function but is sort of buggy both of these still need a way to tell the user when they are at the end of the list of passports.
def prevpass():
    global passport
    passport = passport-1
    Temp=pd.read_csv("Testing.csv")
    PassData=Temp.iloc[passport]
    for i in range(0,len(Cat)):
        df=tk.Label(frame, text=Cat[i]+" : "+PassData[i]).grid(column=2,row=i)

#Eventually I might try to have a search function that can go to the Passport # given certain information in the Text input but this seems complex
#Also just to be able to go to a certain # passport in the list by typing that number in a textbox


#This is just showing that text in a txt file can be read
with open("text.txt", "r") as h:
    tk.Label(frame, text="I wrote this in the py and this is a txt file : "+h.read(),bg='SteelBlue1').grid(column=1,row=0)

#This is reading in the csv file outside of the function to stop errors but is sort of buggy and their is sometimes overlap on the display
Temp=pd.read_csv("Testing.csv")
PassData=Temp.iloc[passport]
Cat=list(pd.read_csv("Testing.csv", nrows =1))
for i in range(0,len(Cat)):
    df=tk.Label(frame, text=Cat[i]+" : "+PassData[i]).grid(column=2,row=i)

#this is opening the image then displaying it we are able to resize the image too.
#I still need to see what the best way to have a iterable thing of images so I can use the next and prev functions with images

image1 = Image.open("Image.png")
image1=image1.resize((200,100))
test=ImageTk.PhotoImage(image1)
PassportImage=tk.Label(frame, image=test).grid(column=1,row=3)

#This is the input text boxs
inputtxt=tk.Text(frame, height=5,width=20,bg="#e4f5e8")
inputtxt.grid(column=0,row=0)

#The text on the button only shows up when you click it for me so I added a Label above each of them
#all three buttons just run the command corresponding with the text in the Label

Next=tk.Label(frame,text="Next Passport").grid(columnspan=1,row=3)
Buttonnext=tk.Button(frame,height=1,width=15,text="Next Passport", command = nextpass)
Buttonnext.grid(columnspan=1,row=4)

Prev=tk.Label(frame,text="Previous Passport").grid(columnspan=1,row=5)
Buttonprev=tk.Button(frame,height=1,width=15,text="Previus Passport", command = prevpass)
Buttonprev.grid(columnspan=1,row=6)

InputLabel=tk.Label(frame, text="Get the input").grid(columnspan=1,row=1)
buttonCommit=tk.Button(frame, height=1, width=15, text="get input",
                    command = retrieve_input)
buttonCommit.grid(columnspan=1,row=2)


lbl=tk.Label(frame,text="Input Text : ")
lbl.grid(column=1,row=1)

root.mainloop()
