"""This is a Qr code genrator app in this app there are two section first for
link and second  for name... in  first section you can paste a link or type a
url and second section enter link name as qr code name"""
#first import some module
from tkinter import *
from tkinter.messagebox import *
import qrcode

#create a tkinter windows
tk=Tk()
tk.title("QR Code App")
#tk.iconbitmap("logo.ico")
tk.geometry("600x700")
tk.config(bg="pink")

#these function is use by button  command
def hello():#these fun. run by button command
    choice=askyesno('Verify','Really Submit?')
    if choice==True:
        link=e1.get()
        name=e2.get()
        img=qrcode.make(link)
        img.save("Qrcode/"+ str(name) +".png")
        global Image
        Image=PhotoImage(file="Qrcode/"+ str(name) +".png")
        #l5=Label(tk,image=Image,height=210,width=210)
        l4.config(image=Image)
        print("successful")
        showinfo('Yes','QrCode Generated successfully')
        
    else:
        showinfo('No','QrCode Generated cancelled')

#show messagebox for better experience
def close():
    choice=askyesno('Verify','Really Exit?')
    if choice==True:
        tk.destroy()
        showwarning('Yes',"I'am not intrested")
        

    else:
        showinfo('No','Exit has been cancelled')

#create entry Label and put your desired place
e1=Entry(tk,font=("Calisto MT",18))
e2=Entry(tk,font=("Calisto MT",18))
e1.place(x=200,y=60,height=40,width=350)
e2.place(x=200,y=120,height=40,width=350)

#create design for lebel and entries
l1=Label(tk,text="Qr Code App",font=("Arial Black",20))
l2=Label(tk,text="Paste Link",font=("Calisto MT",20))
l3=Label(tk,text="Enter Name",font=("Calisto MT",20))
l4=Label(tk)

l1.place(x=175,y=5,height=40,width=240)
l2.place(x=10,y=60,height=40,width=150)
l3.place(x=10,y=120,height=40,width=150)
l4.place(x=125,y=195,height=350,width=350)

#create buttons and their design
#and put buttons your desired place
b1=Button(tk,text="Submit",font=("Calisto MT",15,"bold"),bg="red",fg="yellow",
          activebackground="black",activeforeground="white",command=hello)
b2=Button(tk,text="Exit",font=("Calisto MT",15,"bold"),bg="red",fg="yellow",
          activebackground="black",activeforeground="white",command=close)
b1.place(x=100,y=580,height=50,width=100)
b2.place(x=400,y=580,height=50,width=100)








