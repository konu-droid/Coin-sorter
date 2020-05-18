from tkinter import *
import time
from tkinter import ttk
import webbrowser
import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3

root = Tk()
root.geometry("1600x800")
root.title("Autonomous Car")
#root.attributes("-fullscreen",True)
speed=100;
def getBatteryInfo():
    global percentBar
    percentBar["value"]=90


def GPS(url):
    webbrowser.open_new(url)
    
def SPEED():
    global speed
print(speed)

def directorychooser():


    file='D:\\music\\KaranAujla(DjPunjab.Com).mp3'
        

    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

#directorychooser()

    

TOPS1 =Frame(root,width =1500,height =50,bg="Black",relief="raise",bd=8)
TOPS1.pack(side=TOP,fill="both")


BOTTOMS =Frame(root,width =1600,height =150,bg="Grey",relief="raise",bd=8)
BOTTOMS.pack(side=BOTTOM,fill="both")



TOPS =Frame(root,width =1600,height =300,bg="powderBlue",relief="raise",bd=8)
TOPS.pack(fill="both",expand="yes")

DOWN =Frame(root,width =800,height =400,bg="powderBlue",relief="raise",bd=8)
DOWN.pack(fill="both",expand="yes")

DOWN2 =Frame(root,width =800,height =100,bg="powderBlue",relief="raise",bd=8)
DOWN2.pack(fill="both",expand="yes")




lblinfo =Label(TOPS1,text="Autonomous Car",font=('Helvertica',20,'bold italic'),fg='Steel Blue',bd=2)
lblinfo.pack(side=LEFT,fill="both",expand="yes")

time1 = ''
clock = Label(TOPS1, font=('Helvertica', 20, 'bold italic'), bg='Light Grey',fg='Steel Blue',bd=2)
clock.pack(side=RIGHT,fill="both")
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()


###########################
text1= Text(TOPS,width =55,height =10,font=('Helvertica',15,'bold italic'),bg="Light Grey",fg='White',bd=2)
text1.insert(INSERT," A self-driving car, also known as an autonomous vehicle,\n  ")
text1.insert(INSERT," connected and autonomous vehicle, driverless car, \n" )
text1.insert(INSERT," robo-car,is a vehicle that is capable of sensing  \n")
text1.insert(INSERT," its environment and moving or robotic car,\n")
text1.insert(INSERT," safely with little or no human input.")
text1.config(state="disabled")
text1.pack(side=LEFT,fill="both")

photo1 = PhotoImage(file = 'C:\\Users\\Gandhrav\\Downloads\\google.png') 
button1 =Button(TOPS,text="GPS",font=('Helvertica',20,'bold italic'),image = photo1,fg='Steel Blue',bd=2)
button1.pack(side=TOP,fill="both",expand="yes")


button1.bind("<Button-1>",lambda e:GPS("http://www.google.com"))

photo2 = PhotoImage(file = 'C:\\Users\\Gandhrav\\Downloads\\icons8-music-64.png')
button2 =Button(TOPS,text="MUSIC",font=('Helvertica',20,'bold italic'),image = photo2,fg='Steel Blue',bd=2,command=directorychooser)
button2.pack(side=TOP,fill="both",expand="yes")

photo3 = PhotoImage(file = 'C:\\Users\\Gandhrav\\Downloads\\telephone.png')
button3 =Button(TOPS,text="CALLING",font=('Helvertica',20,'bold italic'),image = photo3,fg='Steel Blue',bd=2)
button3.pack(side=TOP,fill="both",expand="yes")

#######################

speed = Label(DOWN2,width =5,height =3,font=('Helvertica',15,'bold italic'),bg="Light Grey",fg='White',bd=2,text=speed)
speed.pack(side=LEFT,fill="both",expand="yes")




photo4 = PhotoImage(file = 'C:\\Users\\Gandhrav\\Downloads\\speed (1).png')
button4 =Button(DOWN,text="SPEED",font=('arial',20,'bold italic'),image = photo4,fg='Steel Blue',bd=2)
button4.pack(side=LEFT,fill="both",expand="yes")



range1= Label(DOWN2,width =5,height =3,font=('Helvertica',15,'bold italic'),bg="Light Grey",fg='White',bd=2)
range1.pack(side=LEFT,fill="both",expand="yes")

button5=Button(DOWN,text="RANGE",font=('Helvertica',20,'bold italic'),fg='Steel Blue',bd=2)
button5.pack(side=LEFT,fill="both",expand="yes")


labelinfo =Label(BOTTOMS,text="BATTERY STATUS",font=('Helvertica',30,'bold italic'),fg='Steel Blue',bd=2)
labelinfo.pack(side=LEFT)

percentBar= ttk.Progressbar(BOTTOMS,length=100 ,orient="horizontal",mode="determinate") 
percentBar.pack(side=TOP,fill="both",expand="yes")
percentBar["maximum"]=100                       
percentBar["value"]=00

getBatteryInfo()
root.mainloop()
