import time
from pathlib import Path
from tkinter import *
from PIL import ImageTk, Image
import json
from subprocess import call

def submit():
    tubeLength = lenEntry.get()
    tubeID = idEntry.get()
    tubeWall = thicknessE.get()
    towWide = towWidthE.get()
    towThick= towThicknessE.get()
    numLayers = round(float(tubeWall)/float(towThick))
    dictionary = {
        "tubeLength": float(tubeLength),
        "tubeID": float(tubeID),
        "tubeWall": float(tubeWall),
        "towWide": float(towWide),
        "towThick": float(towThick),
        "numLayers": numLayers
    }
    json_object = json.dumps(dictionary, indent=4)

    with open('guistuff\\guiOut.json', 'w') as outfile:
        outfile.write(json_object)
    
    time.sleep(2)

    call(['python', 'guistuff\\guiTwo.py'])
    exit()
    
    

window =Tk()

window.title("Winder Software V0.1")

icon = ImageTk.PhotoImage(Image.open("guistuff\\logo.png"), master=window)
window.iconphoto(True, icon)
window.config(background='#ffffff')

titleBlock = Label(window, 
              text="Winder Software V0.1", 
              font=('Arial',20,'bold'), 
              fg='#b40000',
              bg='#ffffff', 
              relief=RAISED,
              bd=5,
              image=icon,
              compound='right')
titleBlock.grid(row=0, column=0, columnspan=2, sticky='W')

message= Label(window,
               fg='#b40000',
               bg='#ffffff', 
               text='Enter All Values in Milimeters unless otherwise specified.',
               font=('Arial',16,'bold'))
message.grid(row=1, column=0, sticky='W', columnspan=3)

#Entry Box Labels

length = Label(window,
               text='Tube Length:',
               bg='#ffffff', 
               font=('Arial', 14))
length.grid(row=2, column=0, sticky='E')

id = Label(window,
           text='Tube ID:',
           bg='#ffffff', 
           font=('Arial', 14))
id.grid(row=3, column=0, sticky='E')

thickness = Label(window,
                  text='Tube Thickness:',
                  bg='#ffffff', 
                  font=('Arial', 14))
thickness.grid(row=4, column=0, sticky='E')

towWidth = Label(window,
                 text='Tow Width:',
                 bg='#ffffff', 
                 font=('Arial', 14))
towWidth.grid(row=5, column=0, sticky='E')

towThickness = Label(window,
                 text='Tow Thickness:',
                 bg='#ffffff', 
                 font=('Arial', 14))
towThickness.grid(row=6, column=0, sticky='E')

#Entry Boxes

lenEntry=Entry(window,
            font=('Arial', 14),
            bg='#e6e6e6')
lenEntry.grid(row=2, column=1, pady=2, sticky='W')
idEntry=Entry(window,
              font=('Arial', 14),
              bg='#e6e6e6')
idEntry.grid(row=3, column=1, pady=2, sticky='W')
thicknessE=Entry(window,
              font=('Arial', 14),
              bg='#e6e6e6')
thicknessE.grid(row=4, column=1, pady=2, sticky='W')
towWidthE=Entry(window,
              font=('Arial', 14),
              bg='#e6e6e6')
towWidthE.grid(row=5, column=1, pady=2, sticky='W')
towThicknessE=Entry(window,
              font=('Arial', 14),
              bg='#e6e6e6')
towThicknessE.grid(row=6, column=1, pady=2, sticky='W')

#Submit Button

submit = Button(window,
                bg='#ffffff', 
                text='Submit',
                font=('Arial', 20),
                relief=RAISED,
                bd=5,
                command=submit)
submit.grid(row=7, column=2, sticky='W')

window.update()

window.mainloop()
