from tkinter import *
import time
import tkinter.messagebox

# Initializing the main windown

root = Tk()
root.geometry("210x130")
root.title("Basic Timer")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(root, width= 3 , font=("Calibri",20, "bold"), textvariable=hour)
hourEntry.place(x=30, y=30)

minuteEntry = Entry(root, width= 3 , font=("Calibri",20, "bold"), textvariable=minute)
minuteEntry.place(x=80, y=30)

secondEntry = Entry(root, width= 3 , font=("Calibri",20, "bold"), textvariable=second)
secondEntry.place(x=130, y=30)

def submit():

    # Disable the command for the button so it can no longer be clicked
    btn.config(command="")
    

    # Disable changing the values after the clock has been started
    hourEntry.config(state="disabled")
    minuteEntry.config(state="disabled")
    secondEntry.config(state="disabled")

    try:
        # The input provided by the user is stored in temp
        temp = int(hour.get()) * 3600 + int(minute.get()) *60 + int(second.get())
    except:
        tkinter.messagebox.showinfo("messagebox", "Please enter a valid string.")
        
    while temp > -1:
        
        # divmod(firstvalue = temp / 60, zecondvalue = temp % 60)
        mins,secs =divmod(temp,60)

        # Converting the input entered in mis or secs to hours, 
        # mins, secs(input = 110 minutes == 120*60 == 6000 == 1 hour + 50 minutes + 0 secs)
        hours = 00
        if mins > 60:
            hours, mins = divmod(mins,60)

        # using format to store the value up to 2 decimal places.
        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        # Updating the gui
        root.update()
        time.sleep(1)

        # when temp value = 0, then a message pops up, that notifies the user saying time is up. 
        if (temp==00):
            tkinter.messagebox.showinfo("messagebox", "Your timer is up!")

        # Every second, the value of temp will decrease by one
        temp -=1

btn = Button(root,text = "Start Timer", bd = "5", command=submit)
btn.place(x=50,y=70)



root.mainloop()
