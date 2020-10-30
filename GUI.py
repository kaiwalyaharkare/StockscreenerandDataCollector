from tkinter import *
from stockscreener import *
from datetime import datetime as dt

root = Tk()
root.title("KNH Stockscreener")
root.iconbitmap()
root.geometry('400x250')


# intializingelemnets -----------------------------------------------------

StockcodeLabel = Label(root,text= "Enter Stock Code",fg="Black",bg= "White",padx=10,pady=10)
Stockcode = Entry(root,width=10,)

StartDateLable = Label(root, text="Enter Start Date YYYY,MM,DD",padx=10,pady=10)
StartDate = Entry(root,width=10)

EndDateLable = Label(root, text="Enter End Date YYYY,MM,DD",padx=10,pady=10)
EndDate = Entry(root,width=10)

        

def Getdata() :
    Start = dt.strptime(StartDate.get(),"%Y,%m,%d")
    End = dt.strptime(EndDate.get(),"%Y,%m,%d")
    chart(Stockcode.get(),start=Start,end=End,labley=Stockcode.get())
   # Bar(Stockcode.get(),start=Start,end=End,labley=Stockcode.get())

def savecsv():
     Start = dt.strptime(StartDate.get(),"%Y,%m,%d")
     End = dt.strptime(EndDate.get(),"%Y,%m,%d")
     df = web.DataReader(Stockcode.get(),'yahoo',Start,End)
     namefile = Stockcode.get()+"Price Data "+StartDate.get()+"  to   "+EndDate.get()
     df.to_csv(namefile)

def saveexel():
     Start = dt.strptime(StartDate.get(),"%Y,%m,%d")
     End = dt.strptime(EndDate.get(),"%Y,%m,%d")
     df = web.DataReader(Stockcode.get(),'yahoo',Start,End)
     namefile = Stockcode.get()+"Price Data From "+StartDate.get()+"  to  "+EndDate.get()
     df.to_excel(namefile +'.xlsx',engine= "xlsxwriter")



Submit = Button(root,text="PLOT PRICE GRAPH ",command=Getdata,fg="green",padx=10,pady=10,height=1)
Submitsavecsv = Button(root,text="SAVE ALL DATA  CSV",command=savecsv,fg="green",padx=10,pady=10,height=1)
Submitsaveexel = Button(root,text="SAVE ALL DATA EXCEL",command=saveexel,fg="green",padx=10,pady=10,height=1)



# Postioning the elements

StockcodeLabel.grid(column=1)
Stockcode.grid(column=1)

StartDateLable.grid(column=1)
StartDate.grid(column=1)

EndDateLable.grid(column=1)
EndDate.grid(column=1)

Submit.grid(column=2,row=1)
Submitsavecsv.grid(column=2,row=2)
Submitsaveexel.grid(column=2,row=3)



root.mainloop()

