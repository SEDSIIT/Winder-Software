from tkinter import *
from PIL import ImageTk, Image
import json

dictionary = {}
#Checkbox stuff THANK YOU MR GAURAV LEEKHA

def on_checkbox_change(checkbox_value, checkbox_var):
    if checkbox_var:
        response[checkbox_value]=1
    else:
        response[checkbox_value]=0

def create_checkboxes(root, num_checkboxes):
    checkboxes = []

    for x in range(numLayers):
        checkbox_var = BooleanVar()

        hoop = Checkbutton(tab,
                           text='Is helix layer?',
                           font=('Arial', 14),
                           bg='#ffffff',
                           variable=checkbox_var,
                           command=lambda x=x, var=checkbox_var:
                            on_checkbox_change(x, var))
        hoop.grid(row=x+1, column=1, sticky='W')
        checkboxes.append(checkbox_var)
    return checkboxes

def getValues():
        fAng = float(ang.get())
        fPatNum = float(patNum.get())
        fSkipInd = float(skipInd.get())
        fLockAng = float(lockAng.get())
        fLeadIn = float(leadIn.get())
        fLeadOut = float(leadOut.get())
        bSkipIni = bool(skipIni.get())

        return fAng, fPatNum, fSkipInd, fLockAng, fLeadIn, fLeadOut, bSkipIni

def submit():
    fAng, fPatNum, fSkipInd, fLockAng, fLeadIn, fLeadOut, bSkipIni = getValues()
    for x in range(numLayers):
        if (response[x]==0):
            y={"layer "+str(x): {
                "windType": "hoop"
            }}
            dictionary.update(y)
        else:
            y={
                "layer "+str(x): {
                    "windType": 'helix',
                    "windAngle": fAng,
                    "patternNum": fPatNum,
                    "skipIndex": fSkipInd,
                    "lockAngle": fLockAng,
                    "leadInMM": fLeadIn,
                    "leadOutAngle": fLeadOut,
                    "skipInitalNearLock": bSkipIni
                }
            }
            dictionary.update(y)
    
    json_object = json.dumps(dictionary, indent=4)
    
    with open('guistuff\\tempLayers\\layers.json', 'w') as outfile:
        outfile.write(json_object)
    
    exec(open("Cyclone Data Intake.py").read())
    
    exit()

file = open("guistuff\\guiOut.json")
data = json.load(file)

numLayers = data["numLayers"]

response = []

for x in range(numLayers):
    response.append(0)

tab = Tk()

tab.title("Winder Software V0.1")

frame = Frame(tab)
frame.grid(row=0, column=0)

logo = ImageTk.PhotoImage(Image.open("guistuff\\logo2.png"), master=tab)
tab.iconphoto(False, logo)
tab.config(background='#ffffff')

#Title Block and Message

titleBlock = Label(tab, 
              text="Winder Software V0.1", 
              font=('Arial',20,'bold'), 
              fg='#b40000',
              bg='#ffffff', 
              relief=RAISED,
              bd=5,
              image=logo,
              compound='right')
titleBlock.grid(row=0, column=0, columnspan=2)

message= Label(tab,
               fg='#b40000',
               bg='#ffffff', 
               text='Enter All Values in specified Units.',
               font=('Arial',16,'bold'))
message.grid(row=0, column=3, sticky='W', columnspan=2)

messageTwo = Label(tab,
               text='Helix Parameters:',
               fg='#b40000',
               bg='#ffffff', 
               font=('Arial', 16, 'bold'))
messageTwo.grid(row=1, column=4)

#Helix parameter labels

angL = Label(tab,
               text='Wind Angle(Degrees):',
               bg='#ffffff', 
               font=('Arial', 14))
angL.grid(row=2, column=3, sticky='E')

patNumL = Label(tab,
               text='Pattern Number(No Unit):',
               bg='#ffffff', 
               font=('Arial', 14))
patNumL.grid(row=3, column=3, sticky='E')

skipIndL = Label(tab,
               text='Skip Index(No Unit):',
               bg='#ffffff', 
               font=('Arial', 14))
skipIndL.grid(row=4, column=3, sticky='E')

lockAngL = Label(tab,
               text='Lock Angle(Degrees):',
               bg='#ffffff', 
               font=('Arial', 14))
lockAngL.grid(row=5, column=3, sticky='E')

leadInL = Label(tab,
               text='Lead In Distance(MM):',
               bg='#ffffff', 
               font=('Arial', 14))
leadInL.grid(row=6, column=3, sticky='E')

leadOutL = Label(tab,
               text='Lead Out Angle(Degrees):',
               bg='#ffffff', 
               font=('Arial', 14))
leadOutL.grid(row=7, column=3, sticky='E')

skipIniL = Label(tab,
               text='Skip Inital Near Lock(True or False):',
               bg='#ffffff', 
               font=('Arial', 14))
skipIniL.grid(row=8, column=3, sticky='E')

#Helix parameters

ang = Entry(tab,
            font=('Arial', 14),
            bg='#e6e6e6')
ang.grid(row=2, column=4, sticky='W')

patNum = Entry(tab,
            font=('Arial', 14),
            bg='#e6e6e6')
patNum.grid(row=3, column=4, sticky='W')

skipInd = Entry(tab,
            font=('Arial', 14),
            bg='#e6e6e6')
skipInd.grid(row=4, column=4, sticky='W')

lockAng = Entry(tab,
            font=('Arial', 14),
            bg='#e6e6e6')
lockAng.grid(row=5, column=4, sticky='W')

leadIn = Entry(tab,
            font=('Arial', 14),
            bg='#e6e6e6')
leadIn.grid(row=6, column=4, sticky='W')

leadOut = Entry(tab,
            font=('Arial', 14),
            bg='#e6e6e6')
leadOut.grid(row=7, column=4, sticky='W')

skipIni = Entry(tab,
            font=('Arial', 14),
            bg='#e6e6e6')
skipIni.grid(row=8, column=4, sticky='W')

#Array of layers

for x in range(numLayers):
    layerNum = Label(tab,
                     text='Layer '+str(x+1)+":",
                     bg='#ffffff',
                     font=('Arial', 14))
    layerNum.grid(row=x+1, column=0, sticky='W')

#Checkboxes

checkboxes = create_checkboxes(tab, data["numLayers"])

# Submit button

submitBut = Button(tab,
                   bg='#ffffff',
                   relief=RAISED,
                   bd=2,
                   text='Submit',
                   font=('Arial', 14),
                   command=submit)
submitBut.grid(row=numLayers+1, column=1)

tab.update()

tab.mainloop()
