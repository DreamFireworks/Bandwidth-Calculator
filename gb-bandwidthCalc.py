from tkinter import *

window = Tk()
window.geometry("250x300")
window.title("GB")
window.resizable(width=False,
                 height=False)

# In megabytes:
#File Size In (Gigabytes*1024) / (Download Speed In Megabits / 8) = Time In Seconds

def megabytes():
    fileSizeInGb = float(entry1.get())
    megabytes=fileSizeInGb*1024
    downSpeed = int(entry2.get())
    time=megabytes/(downSpeed/8) #formula
    result1.config(text=str(round(time,2)) + " seconds\n" +
      " = " + str(round((time/60),2)) + " Minutes\n" +
      " = " + str( round((time/60)/60,2)) + " Hours\n" + 
      " in " + str(downSpeed/8) + "MB per sec" )
# File size
label1= Label(window,text="File's size (GB) (E.g 1.4)",justify="center")
entry1= Entry(window,justify="center")
label1.place(x=15,y=20,width=220,height=25)
entry1.place(x=15,y=50,width=220,height=25)
# Download Speed
label2= Label(window,text="Download Speed (MegaBits) (E.g 25)",justify="center")
entry2= Entry(window,justify="center")
label2.place(x=15,y=85,width=220,height=25)
entry2.place(x=15,y=120,width=220,height=25)
# Calculation 
button1= Button(window,text= "Calculate!",command=megabytes)
button1.place(x=15,y=150,width=220,height=25)
# Result
result1= Label(window,text="Result Will Shown Here.")
result1.place(x=15,y=190,width=220,height=75)

window.mainloop()