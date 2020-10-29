from tkinter import *
from stockscreener import *
from datetime import datetime as dt

root = Tk()
root.title("KNH Stockscreener")
root.iconbitmap()
root.geometry('250x250')




# intializingelemnets -----------------------------------------------------

StockcodeLabel = Label(root,text= "Enter Stock Code",fg="Black",bg= "White",padx=10,pady=10)
Stockcode = Entry(root,width=10,)

StartDateLable = Label(root, text="Enter Start Date YYYY,MM,DD",padx=10,pady=10)
StartDate = Entry(root,width=10)

EndDateLable = Label(root, text="Enter End Date YYYY,MM,DD",padx=10,pady=10)
EndDate = Entry(root,width=10)
#  Buttonpress fuction

def Getdata() :
    Start = dt.strptime(StartDate.get(),"%Y,%m,%d")
    End = dt.strptime(EndDate.get(),"%Y,%m,%d")
    chart(Stockcode.get(),start=Start,end=End)


Submit = Button(root,text="SUBMIT",command=Getdata)

# Postioning the elements
StockcodeLabel.pack()
Stockcode.pack()

StartDateLable.pack()
StartDate.pack()

EndDateLable.pack()
EndDate.pack()

Submit.pack()


root.mainloop()

