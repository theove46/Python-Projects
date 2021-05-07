from tkinter import*
import datetime

root = Tk()
root.geometry("1700x800+0+0")
root.configure(bg='gray12')
root.title("Ovemania Dines")


# Generate Date & Time
localtime = datetime.datetime.now()

# Restaurant Name top label
Top = Frame(root, bg="gray12", width=100, height=100, relief=FLAT)
Top.pack(side=TOP, pady=20)
# Restaurant Name, Date & Time
restaurant = Label(Top, font=('Times', 40, "bold"), text="Ovemania Dines", fg="dark orange", bg="gray12")
#restaurant.pack(side=TOP)
restaurant.grid(row=0,column=0)
date_time = Label(Top, font=('Times',20),text=localtime, fg="dark orange", bg="gray12")
#date_time.pack(side=TOP)
date_time.grid(row=1,column=0)


# Food Menu label
f1 = Frame(root, bg="gray12", width=100, height=500, relief=FLAT)
f1.pack(side=LEFT, padx=20)

# Calculator label
f2 = Frame(root, bg="gray5", bd=0, width=500, height=500, relief=FLAT)
f2.pack(side=RIGHT, padx=50, expand=YES)


# Calculator setup
display = StringVar()

cal_screen = Entry(f2, font=('Times', 20, 'bold'), textvariable=display , bd=5 ,insertwidth=7 ,bg="gray5", fg= "dark orange", justify='right', relief=FLAT)
cal_screen.grid(columnspan=4, ipady=30)

def calc(display):
    try: display.set(eval(display.get()))
    except: display.set("math error")

i = 1
j = 0
for button_line in ( ["c", "dl", "//", "/"],
             ["7", "8", "9", "*"], 
             ["4", "5", "6", "-"],
             ["1", "2", "3", "+"],
             [".", "0", "%", "="]):
    j = 0
    for text in button_line:
        if(text=="c"):
            btc = Button(f2, text=text, bd=3, bg="firebrick1", fg="white", height=2, width=5, font = ('Times', 16, 'bold'), relief=FLAT, command=lambda show=display: show.set(''))
            btc.grid(row=i, column=j)

        elif(text=="dl"):
            btdl = Button(f2, text=text, bd=3, bg="brown1", fg="white", height=2, width=5, font = ('Times', 16, 'bold'), relief=FLAT, command=lambda show=display, q=text: show.set(show.get()[:-1]))
            btdl.grid(row=i,column=j)

        elif(text=="="):
            bteq = Button(f2, text=text, bd=3, bg="dodger blue", fg="white", height=2, width=5, font = ('Times', 16, 'bold'), relief=FLAT, command=None)
            bteq.grid(row=i,column=j)
            bteq.bind('<ButtonRelease-1>', lambda e, show=display: calc(show), '+')

        elif(text=="+" or text=="-" or text=="*" or text=="/" or text=="//" or text=="%"):
            btop = Button(f2, text=text, bd=3, bg="gray5", fg="dark orange", height=2, width=5, font = ('Times', 16, 'bold'), relief=FLAT, command=lambda  show=display, q=text: show.set(show.get()+q))
            btop.grid(row=i,column=j)

        elif(text=="." or text=="0" or text=="1" or text=="2" or text=="3" or text=="4" or text=="5" 
            or text=="6" or text=="7" or text=="8" or text=="9"):
            btdg = Button(f2, text=text, bd=3, bg="gray5", fg="dark orange", height=2, width=5, font = ('Times', 16, 'bold'), relief=FLAT, command=lambda show=display, q=text: show.set(show.get()+q))
            btdg.grid(row=i,column=j)
        j+=1
    i+=1



# Cost setup
rand = StringVar()
Order_no = StringVar()
Cus_name = StringVar()
Itemname1 = StringVar()
Itemname2 = StringVar()
Itemname3 = StringVar()
Itemname4 = StringVar()
Itemname5 = StringVar()
Item1 = StringVar()
Item2 = StringVar()
Item3 = StringVar()
Item4 = StringVar()
Item5 = StringVar()
Sub_Total_Cost = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Total_Cost = StringVar()

c_name = Label(f1, font=('Times', 16, 'bold'), text="Customers Name:", bg="gray12", fg="dodger blue", bd=0, width=14, anchor='w')
c_name.grid(row=0,column=0)
c_name_val = Entry(f1, font=('Times', 16, 'bold'), textvariable=Cus_name, bd=2, bg="gray12", fg="dark orange", justify='right', width=16)
c_name_val.grid(row=0,column=1)

odr_no = Label(f1, font=('Times', 16, 'bold'), text="Order No:", bg="gray12", fg="dodger blue", bd=0, width=14, anchor='w')
odr_no.grid(row=1,column=0)
odr_no_val = Entry(f1, font=('Times', 16, 'bold'), textvariable=Order_no, bd=2, bg="gray12", fg="dark orange", justify='right', width=16)
odr_no_val.grid(row=1,column=1)

st_cost = Label(f1, font=('Times', 16, 'bold'), text="Food Cost:", bg="gray12", fg="dodger blue", bd=0, width=14, anchor='w')
st_cost.grid(row=2,column=0)
st_cost_val = Entry(f1, font=('Times', 16, 'bold'), textvariable=Sub_Total_Cost, bd=2, bg="gray12", fg="dark orange", width=16, justify='right')
st_cost_val.grid(row=2,column=1)

sv_chrg = Label(f1, font=('Times', 16, 'bold'), text="Service Charge:", bg="gray12", fg="dodger blue", width=14, bd=0, anchor='w')
sv_chrg.grid(row=3,column=0)
sv_chrg_val = Entry(f1, font=('Times', 16, 'bold'), textvariable=Service_Charge, bd=2, bg="gray12", fg="dark orange", width=16, justify='right')
sv_chrg_val.grid(row=3,column=1)

vat = Label(f1, font=('Times', 16, 'bold'), text="VAT:", bg="gray12", fg="dodger blue", width=14, bd=0, anchor='w')
vat.grid(row=4,column=0)
vat_val = Entry(f1, font=('Times', 16, 'bold'), textvariable=Tax, bd=2, bg="gray12", fg="dark orange", width=16, justify='right')
vat_val.grid(row=4,column=1)

tot_cost = Label(f1, font=('Times', 16, 'bold'), text="Total Cost:", bg="gray12", fg="dodger blue", width=14, bd=0, anchor='w')
tot_cost.grid(row=5,column=0)
tot_cost_val = Entry(f1, font=('Times', 16, 'bold'), textvariable=Total_Cost, bd=2, bg="gray12", fg="dark orange", width=16, justify='right')
tot_cost_val.grid(row=5,column=1)



i_name = Label(f1, font=('Times', 16, 'bold'), text="Items:", bg="gray12", fg="dodger blue", width=14, bd=0)
i_name.grid(row=0,column=2)
prc = Label(f1, font=('Times', 16, 'bold'), text="Prices:", bg="gray12", fg="dodger blue", width=16, bd=0)
prc.grid(row=0,column=3)

itm1 = Entry(f1, font=('Times', 16, 'bold'), textvariable=Itemname1, bg="gray12", fg="dodger blue", width=14, bd=0, justify='left')
itm1.grid(row=1,column=2)
itm1_val = Entry(f1, font=('Times', 16, 'bold'), textvariable=Item1, bd=2, bg="gray12", fg="dark orange", width=16, justify='right')
itm1_val.grid(row=1,column=3)

itm2 = Entry(f1, font=('Times', 16, 'bold'), textvariable=Itemname2, bg="gray12", fg="dodger blue", width=14, bd=0, justify='left')
itm2.grid(row=2,column=2)
itm2_val = Entry(f1, font=('Times', 16, 'bold'), textvariable=Item2, bd=2, bg="gray12", fg="dark orange", width=16, justify='right')
itm2_val.grid(row=2,column=3)

itm3 = Entry(f1, font=('Times', 16, 'bold'), textvariable=Itemname3, bg="gray12", fg="dodger blue", width=14, bd=0, justify='left')
itm3.grid(row=3,column=2)
itm3_val = Entry(f1, font=('Times', 16, 'bold'), textvariable=Item3, bd=2, bg="gray12", fg="dark orange", width=16, justify='right')
itm3_val.grid(row=3,column=3)

itm4 = Entry(f1, font=('Times', 16, 'bold'), textvariable=Itemname4, bg="gray12", fg="dodger blue", width=14, bd=0, justify='left')
itm4.grid(row=4,column=2)
itm4 = Entry(f1, font=('Times', 16, 'bold'), textvariable=Item4, bd=2, bg="gray12", fg="dark orange", width=16, justify='right')
itm4.grid(row=4,column=3)

itm5 = Entry(f1, font=('Times', 16, 'bold'), textvariable=Itemname5, bg="gray12", fg="dodger blue", width=14, bd=0, justify='left')
itm5.grid(row=5,column=2)
itm5_val = Entry(f1, font=('Times', 16, 'bold'), textvariable=Item5, bd=2, bg="gray12", fg="dark orange", width=16, justify='right')
itm5_val.grid(row=5,column=3)



# Price Button - List
def pricebt():
    plist = Tk()
    plist.geometry("650x250+0+0")
    plist.title("Prices")
    plist.configure(bg='gray12')

    lv1 = Label(plist, font=('Times', 22, 'bold'), text="Items", bg="gray12", fg="dark orange")
    lv1.grid(row=0, column=0)
    lv1 = Label(plist, text="    -----    ", bg="gray12", fg="dark orange")
    lv1.grid(row=0, column=2)
    lv1 = Label(plist, font=('Times', 22, 'bold'), text="Price", bg="gray12", fg="dark orange")
    lv1.grid(row=0, column=3)

    MK = Label(plist, font=('Times', 16, 'bold'), text="Mutton  Kacchi", bg="gray12", fg="dodger blue")
    MK.grid(row=1, column=0)
    MK = Label(plist, font=('Times', 16, 'bold'), text="180/340", bg="gray12", fg="dodger blue")
    MK.grid(row=1, column=3)

    MP = Label(plist, font=('Times', 16, 'bold'), text="Morog  Polaw", bg="gray12", fg="dodger blue")
    MP.grid(row=2, column=0)
    MP = Label(plist, font=('Times', 16, 'bold'), text="160/300", bg="gray12", fg="dodger blue")
    MP.grid(row=2, column=3)

    BT = Label(plist, font=('Times', 16, 'bold'), text="Beef  Tehari", bg="gray12", fg="dodger blue")
    BT.grid(row=3, column=0)
    BT = Label(plist, font=('Times', 16, 'bold'), text="160/340", bg="gray12", fg="dodger blue")
    BT.grid(row=3, column=3)

    IP = Label(plist, font=('Times', 16, 'bold'), text="Ilish  Polaw", bg="gray12", fg="dodger blue")
    IP.grid(row=4, column=0)
    IP = Label(plist, font=('Times', 16, 'bold'), text="160/340", bg="gray12", fg="dodger blue")
    IP.grid(row=4, column=3)

    VK = Label(plist, font=('Times', 16, 'bold'), text="Vhuna  Khicuri", bg="gray12", fg="dodger blue")
    VK.grid(row=5, column=0)
    VK = Label(plist, font=('Times', 16, 'bold'), text="150/280", bg="gray12", fg="dodger blue")
    VK.grid(row=5, column=3)


    lv2 = Label(plist, text="                    ", bg="gray12")
    lv2.grid(row=0, column=5)
    lv2 = Label(plist, font=('Times', 22, 'bold'), text="Items", bg="gray12", fg="dark orange")
    lv2.grid(row=0, column=9)
    lv2 = Label(plist, text="    -----    ", bg="gray12", fg="dark orange")
    lv2.grid(row=0, column=11)
    lv2 = Label(plist, font=('Times', 22, 'bold'), text="Price", bg="gray12", fg="dark orange")
    lv2.grid(row=0, column=12)

    CR = Label(plist, font=('Times', 16, 'bold'), text="Chicken  Roast", bg="gray12", fg="dodger blue")
    CR.grid(row=1, column=9)
    CR = Label(plist, font=('Times', 16, 'bold'), text="80", bg="gray12", fg="dodger blue")
    CR.grid(row=1, column=12)

    BR = Label(plist, font=('Times', 16, 'bold'), text="Beef  Rezala", bg="gray12", fg="dodger blue")
    BR.grid(row=2, column=9)
    BR = Label(plist, font=('Times', 16, 'bold'), text="140", bg="gray12", fg="dodger blue")
    BR.grid(row=2, column=12)

    JK = Label(plist, font=('Times', 16, 'bold'), text="Jali  Kabab", bg="gray12", fg="dodger blue")
    JK.grid(row=3, column=9)
    JK = Label(plist, font=('Times', 16, 'bold'), text="30", bg="gray12", fg="dodger blue")
    JK.grid(row=3, column=12)

    BH = Label(plist, font=('Times', 16, 'bold'), text="Borhani", bg="gray12", fg="dodger blue")
    BH.grid(row=4, column=9)
    BH = Label(plist, font=('Times', 16, 'bold'), text="30", bg="gray12", fg="dodger blue")
    BH.grid(row=4, column=12)

    FJ = Label(plist, font=('Times', 16, 'bold'), text="Firni/Jorda", bg="gray12", fg="dodger blue")
    FJ.grid(row=5, column=9)
    FJ = Label(plist, font=('Times', 16, 'bold'), text="40", bg="gray12", fg="dodger blue")
    FJ.grid(row=5, column=12)

    roo.mainloop()

# Total Button
def Ref():
    zr = '0'
    i1 = float(Item1.get()+zr)/10
    i2 = float(Item2.get()+zr)/10
    i3 = float(Item3.get()+zr)/10
    i4 = float(Item4.get()+zr)/10
    i5 = float(Item5.get()+zr)/10

    sub_cost = str('%.2f' %(i1 + i2 + i3 + i4 + i5)), "Taka"
    tax_cost = str('%.2f' %((i1 + i2 + i3 + i4 + i5) * 0.15)), "Taka"
    service_cost = str('%.2f' %((i1 + i2 + i3 + i4 + i5) * 0.03)), "Taka"
    
    sub_cost1 = (i1 + i2 + i3 + i4 + i5)
    tax_cost1 = (i1 + i2 + i3 + i4 + i5) * 0.15
    service_cost1 = (i1 + i2 + i3 + i4 + i5) * 0.03

    total_cost = str('%.2f' %(sub_cost1 + tax_cost1 + service_cost1) ), "Taka"
    
    Sub_Total_Cost.set(sub_cost)
    Service_Charge.set(service_cost)
    Tax.set(tax_cost)
    Total_Cost.set(total_cost)

# Reset Button
def resetbt():
    Order_no.set("")
    Cus_name.set("")
    Itemname1.set("")
    Itemname2.set("")
    Itemname3.set("")
    Itemname4.set("")
    Itemname5.set("")
    Item1.set("")
    Item2.set("")
    Item3.set("")
    Item4.set("")
    Item5.set("")
    Sub_Total_Cost.set("")
    Service_Charge.set("")
    Tax.set("")
    Total_Cost.set("")

# Exit Button
def exitbt():
    root.destroy()

price_button=Button(f1, padx=16, pady=8, bd=0 , fg="gray12", font=('Times', 16, 'bold'), width=10, text="PRICE", bg="dark orange", relief=FLAT, command=pricebt)
price_button.grid(row=7, column=0, pady=30)

btnTotal=Button(f1,padx=16,pady=8, bd=0, fg="gray12", font=('Times', 16, 'bold'), width=10, text="TOTAL", bg="dodger blue", relief=FLAT, command=Ref)
btnTotal.grid(row=7, column=1)

reset_button=Button(f1,padx=16,pady=8, bd=0, fg="gray12", font=('Times', 16, 'bold'), width=10, text="RESET", bg="brown1", relief=FLAT, command=resetbt)
reset_button.grid(row=7, column=2)

exit_button=Button(f1,padx=16,pady=8, bd=0, fg="gray12", font=('Times', 16, 'bold'), width=10, text="EXIT", bg="firebrick1", relief=FLAT, command=exitbt)
exit_button.grid(row=7, column=3)

root.mainloop()
