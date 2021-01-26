from tkinter import *

window = Tk()
window.geometry("450x450")
window.title("GB")
window.resizable(width=False,
                 height=False)
file_var = StringVar(window)
speed_var = StringVar(window)
choice = ["GB","Mbps"]
# In megabytes:
#File Size In (Gigabytes*1024) / (Download Speed In Megabits / 8) = Time In Seconds
def choicemaker():
    if choice[0]=="GB":
        forgigabytes()
    else:
        formegabytes()
        

def forgigabytes():
    global choice
    fileSizeInGb = float(entry1.get())
    megabytes=fileSizeInGb*1024
    downSpeed = int(entry2.get())
    if choice[1] == "Mbps":
        time=megabytes/(downSpeed/8) #formula
        result1.config(text=str(round(time,2)) + " seconds\n" +
        " = " + str(round((time/60),2)) + " Minutes\n" +
        " = " + str( round((time/60)/60,2)) + " Hours\n" + 
        " in " + str(downSpeed/8) + "MB per sec" )
    else:
        pass
        
def formegabytes():
    fileSizeInMegabytes = int(entry1.get())
    downSpeed = int(entry2.get())
    if choice[1] == "Mbps":
        time=fileSizeInMegabytes/(downSpeed/8) #formula
        result1.config(text=str(round(time,2)) + " seconds\n" +
        " = " + str(round((time/60),2)) + " Minutes\n" +
        " = " + str( round((time/60)/60,2)) + " Hours\n" + 
        " in " + str(downSpeed/8) + " MB per sec" )
    else:
        pass

# File size
label1= Label(window,text="File's size (GB) (E.g 1.4)",justify="center")
entry1= Entry(window,justify="center")
label1.place(x=15,y=20,width=220,height=25)
entry1.place(x=15,y=50,width=220,height=25)

file_choices = {'GB','MB'}
file_var.set('GB') # set the default option

popupMenu = OptionMenu(window, file_var, *file_choices)
popupMenu.place(x=300,y=45,width=100,height=25)

# Download Speed
label2 = Label(window,text="Download Speed (MegaBits) (E.g 25)",justify="center")
entry2 = Entry(window,justify="center")
label2.place(x=15,y=120,width=220,height=25)
entry2.place(x=15,y=150,width=220,height=25)

speed_choices = { 'Mbps','Kbps'}
speed_var.set('Mbps') # set the default option

popupMenu = OptionMenu(window, speed_var, *speed_choices)
popupMenu.place(x=300,y=145,width=100,height=25)

# Calculation 
calculate = Button(window,text= "Calculate!",command=choicemaker)
calculate.place(x=15,y=180,width=220,height=25)
# Result
result1 = Label(window,text="Result Will Shown Here.")
result1.place(x=15,y=210,width=220,height=75)

def change_dropdown(*args):
    print(file_var.get())
    choice[0] = file_var.get()
    print(speed_var.get())
    choice[1] = speed_var.get()
    print(choice)

# link function to change dropdown
file_var.trace('w', change_dropdown)
speed_var.trace('w', change_dropdown)

window.mainloop()