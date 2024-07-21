from tkinter import *
from PIL import ImageTk, Image

root = Tk()

#set's Display Size
root.geometry("1024x600")
#Set's Title
root.title('RX-7 Dash')

#Set's the text font and size
GlobalFont = ('Calibri',20)

#Rotates Gauge Needles on Screen
SpeedoNeedleAngle = -90


#Positions Gauge Needles on Screen
SpeedoNeedlePos = (512,300)
MileagePos = (200,500)
AirTempPos = (825,500)


#Positions Text on Screen

#Open's Asset Image Files
BackgroundAsset = ImageTk.PhotoImage(file='Background.png')
SpeedoNeedleAsset = ImageTk.PhotoImage(file='Speedometer Needle.png')

#Create's Labels
Mileage = ("231259")
AirTemp = ("80")

#Creates the Canvas
canvas = Canvas(root, width=1024, height=600, bg='white')
canvas.pack(anchor=CENTER,expand=True)

#adds pictures and text to the canvas
canvas.create_image(SpeedoNeedlePos, image=BackgroundAsset)
canvas.create_image(SpeedoNeedlePos, image=SpeedoNeedleAsset)
canvas.create_text(MileagePos, text=Mileage, fill='White',font=GlobalFont,)
canvas.create_text(AirTempPos, text=AirTemp, fill='White',font=GlobalFont,)

root.mainloop()
