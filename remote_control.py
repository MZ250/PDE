from Tkinter import *
import serial
import time
import struct
#Change to commit on GITHUB 1.1


usbport = "/dev/cu.usbmodem1421"
ser = serial.Serial(usbport, 9600, timeout=1)
time.sleep(2)

control=Tk()
control.title("Base Control")
control.geometry("500x800+355+10")
v = StringVar()
v.set("\nSTEERING\n")
cline0=Label(textvariable=v).pack()

shot=Tk()
shot.title("Cannon Control")
shot.geometry("350x500+0+10")



def get_values(*args):
        values = bytearray([cline2.get(), cline3.get(), cline4.get(),cannonh.get(), cannonv.get(), 0x7F])
        print (cline2.get(),"   ",cline3.get(),"    ",cline4.get(),"    ",cannonh.get(),"    ",cannonv.get())
        #print (cline3.get())
        #print (cline4.get())
        ser.write(values)
        time.sleep(0.1)

#BASE MOVEMENT CONTROLS.

cline2=Scale(control,orient=HORIZONTAL,length=300,width=20,sliderlength=30,from_=0,to=100,tickinterval=20, command=get_values)
cline2.set(50)
cline2.pack()
cline1=Label(text="\n\n\nSPEED\n").pack()


cline3=Scale(control,orient=VERTICAL,length=300,width=20,sliderlength=30,from_=100,to=0,tickinterval=20, command=get_values)
cline3.pack()

cline5=Label(text="\n\n\nFORWARD / BACKWARD\n").pack()
cline4=Scale(control,orient=HORIZONTAL,length=100,width=20,sliderlength=55,from_=1,to=2,tickinterval=1, command=get_values)
cline4.pack()

#CANNON CONTROLS.

can_h = Label(shot, text = "Horizontal control").pack()
cannonh = Scale(shot, orient=HORIZONTAL, length=200, width=20, sliderlength=55, from_=0, to=100, tickinterval=40, command=get_values)
cannonh.set(32)
cannonh.pack()

can_v = Label(shot, text = "\n\nVertical control").pack()
cannonv = Scale(shot, orient=VERTICAL, length=200, width=20, sliderlength=55, from_=40, to=127, tickinterval=40, command=get_values)
cannonv.set(60)
cannonv.pack()

trig = Label(shot, text="\n\n").pack()
trigger = Button(shot, text="FIRE").pack()



    #def print_value():
        #print val

     #   v.set(val)
      #  val = int(val)
        #ser.write(chr(val)
        #ser.write(struct.pack('>BBB',cline4.get(),cline3.get(),90)





    #ser.write(struct.pack('>BBB',cline4.get(),cline3.get(),90)

   # Button(control, text='Show', command=show_values).pack()


control.mainloop()
shot.mainloop()



