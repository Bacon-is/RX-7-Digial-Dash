from tkinter import *
from PIL import ImageTk, Image

root = Tk()

#Open's Asset Images
BackgroundImg = Image.open('Background.png')
SpeedoNeedleImg = Image.open('Speedometer Needle.png')

angle = 10

#Positions Gauge Needles on Screen
SpeedoNeedlePos = (0,0)

#Places Assets above the background
BackgroundImg.paste(SpeedoNeedleImg,(SpeedoNeedlePos), SpeedoNeedleImg.rotate(angle))
tkimage = ImageTk.PhotoImage(BackgroundImg)
panel1 = Label(root, image=tkimage)
panel1.grid(row=0, column=2, sticky=E)


root.mainloop()
