from tkinter import *
top=Tk()
top.geometry ('700x300+80+60')
L00 = Label(top, text="Bill-o-Food", fg='dark blue', font=('Arial', 18, 'bold'))
L00.place(x=250, y=2)
L0=Label (top, text="The Boys Restaurant",fg='Green')
L0.place(x=260, y=35)
L1=Label (top, text="Fries")
L1.place(x=10, y=70)
e1=Entry(top, bd=7)
e1.place(x=90, y=70)
f1=Label(top,text="30/-")
f1.place(x=250, y=70)
L2=Label (top, text="Noodels")
L2.place(x=10, y=100)
e2=Entry(top, bd=7)
e2.place( x=90, y=100)
f2=Label(top,text="50/-")
f2.place(x=250, y=100)
L3=Label (top, text="Pizza")
L3.place(x=10, y=130)
e3=Entry(top, bd=7)
e3.place(x=90, y=130)
f3=Label(top,text="100/-")
f3.place(x=250, y=130)
L4=Label (top, text="Burger")
L4.place(x=10, y=160)
e4=Entry(top, bd=7)
e4.place(x=90, y=160)
f4=Label(top,text="90/-")
f4.place(x=250, y=160)
L5=Label (top, text="Sandwich")
L5.place(x=10, y=190)
e5=Entry(top, bd=7)
e5.place(x=90, y=190)
f5=Label(top,text="80/-")
f5.place(x=250, y=190)
L6=Label (top, text="Drinks")
L6.place(x=10, y=220)
e6=Entry(top, bd=7)
e6.place(x=90, y=210)
f6=Label(top,text="25/-")
f6.place(x=250, y=220)
L7=Label (top, text="Cost Of Meal")
L7.place(x=300, y=70)
e7=Entry(top, bd=7)
e7.place(x=390, y=70)
L8=Label (top, text="CGST")
L8.place(x=300, y=100)
e8=Entry(top, bd=7)
e8.place(x=390, y=100)
f8=Label(top,text="15%")
f8.place(x=550, y=100)
L9=Label (top, text="SGST")
L9.place(x=300, y=130)
e9=Entry(top, bd=7)
e9.place(x=390, y=130)
f9=Label(top,text="15%")
f9.place(x=550, y=130)
L11=Label (top, text="Total")
L11.place(x=300, y=160)
e11=Entry(top, bd=7)
e11.place(x=390, y=160)
def add ():
    if(e1.get().isdigit() ):
        f1=float(e1.get())*30
    else:
        f1=0
    if(e2.get().isdigit() ):
        f2=float(e2.get())*50
    else:
        f2=0
    if(e3.get().isdigit() ):
        f3=float(e3.get())*100
    else:
        f3=0
    if(e4.get().isdigit() ):
        f4=float(e4.get())*90
    else:
        f4=0
    if(e5.get().isdigit() ):
        f5=float(e5.get())*80
    else:
        f5=0
    if(e6.get().isdigit() ):
        f6=float(e6.get())*25
    else:
        f6=0

    COM=f1+f2+f3+f4+f5+f6
    e7.delete(0,END)
    e7.insert(0,COM)
    CGST=(COM*15)/100.0
    e8.delete(0,END)
    e8.insert(0,CGST)
    SGST=(COM*15)/100.0
    e9.delete(0,END)
    e9.insert(0,SGST)
    Total=COM+CGST+SGST
    e11.delete(0,END)
    e11.insert(0,Total)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e11.delete(0,END)

but=Button(top,text="Total",command=add, fg="green")
but.place(x=230,y=250)
but=Button(top,text="Reset",command=clear, fg="blue")
but.place(x=180,y=250)
but=Button(top,text="Quit",command=top.destroy, fg="red")
but.place(x=280,y=250)
mainloop()