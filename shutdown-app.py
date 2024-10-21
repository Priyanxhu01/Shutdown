from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1") #/r= restart and /t 1=timeout and 1 'means' the computer will restart after a 1-second.

def restart_time():
    os.system("shutdown /r /t 20")

def log_out():
    os.system("shutdown -l") # -l = logoff

def shutdown():
     os.system("shutdown /s /t 1") # /s = shutdown

st = Tk() # class
st.title("ShutDown App") # title
st.geometry("500x500") # size of the frame
st.config(bg="black") # background color

# Restart button
r_button = Button(st,text="Restart",bg="red",font=("Time New Roman",15,"bold"),
                  relief = RAISED, cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

# Restart with time delay button
rtime_button = Button(st,text="Restart Time",bg="red",font=("Time New Roman",15,"bold"),
                      relief = RAISED, cursor="plus", command=restart_time)
rtime_button.place(x=150,y=170,height=50,width=200)


lg_button = Button(st,text="Log-Out",bg="red",font=("Time New Roman",15,"bold"),
                   relief = RAISED, cursor="plus",command=log_out)
lg_button.place(x=150,y=270,height=50,width=200)


sd_button = Button(st,text="Shut down",bg="red",font=("Time New Roman",15,"bold"),
                   relief = RAISED, cursor="plus",command=shutdown)
sd_button.place(x=150,y=370,height=50,width=200)





st.mainloop() # function