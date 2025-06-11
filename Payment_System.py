from tkinter import *
import time
import calc_function
import random

root = Tk()
root.geometry("1400x700")
root.title("Restaurant Payment System")
top = Frame(root, width=1400, height=50)
top.pack(side=TOP)
frame1 =Frame(root, width=900, height=650)
frame1.pack(side=LEFT)
frame2 = Frame(root, width=400, height=650)
frame2.pack(side=RIGHT)


app_title =Label(top, font=("arial", 30, "bold"), text="Restaurant Payment System").grid(row=0, column=0)
localtime = time.asctime(time.localtime(time.time()))
app_time = Label(top, font=("arial", 20),text=localtime ).grid(row=1, column=0)
calc_function.calculator(frame2)


fries = StringVar()
largefries=StringVar()
ham_burger=StringVar()
filet = StringVar()
cheese_burger =StringVar()
drinks = StringVar()
order_no = StringVar()
cost = StringVar()
service_charge =StringVar()
tax =StringVar()
subtotal = StringVar()
total = StringVar()

price_lister = {"Fries": 4.99, "Large Fries": 9.99, "Hamburger": 12, "Filet": 3.5, "Cheese Burger": 6.7, "Drinks": 2.99}

def bill():
    x= str(random.randint(10000, 999999))
    order_no.set(x)
    count_of_fries =int(fries.get())
    count_of_large_fries =int(largefries.get())
    count_of_hamburger= int(ham_burger.get())
    count_of_filet= int(filet.get())
    count_of_cheese_burger= int(cheese_burger.get())
    count_of_drinks= int(drinks.get())
    cost_of_fries = count_of_fries * price_lister["Fries"]
    cost_of_large_fries = count_of_large_fries * price_lister["Large Fries"]
    cost_of_hamburger = count_of_hamburger * price_lister["Hamburger"]
    cost_of_filet = count_of_filet * price_lister["Filet"]
    cost_of_cheese_burger = count_of_cheese_burger * price_lister["Cheese Burger"]
    cost_of_drinks = count_of_drinks * price_lister["Drinks"]
    cost_of_everything = cost_of_fries+cost_of_large_fries+cost_of_hamburger+cost_of_filet+cost_of_cheese_burger+cost_of_drinks
    cost_of_meal = "$" +str("%.2f" %(cost_of_everything))
    PayTax = cost_of_everything * 0.1
    totalCost = cost_of_everything+PayTax
    servi_charges=totalCost*0.125
    service = "$"+str("%.2f" %(servi_charges))
    overall_cost = "$"+str("%.2f" %(totalCost+servi_charges))
    paid_tax ="$"+str("%.2f"%PayTax)
    service_charge.set(service)
    cost.set(cost_of_meal)
    tax.set(paid_tax)
    subtotal.set(cost_of_meal)
    total.set(overall_cost)



def exit():
    root.destroy()

def reset():
    fries.set("")
    largefries.set("")
    ham_burger.set("")
    filet.set("")
    cheese_burger.set("")
    drinks.set("")
    order_no.set("")
    cost.set("")
    service_charge.set("")
    tax.set("")
    subtotal.set("")
    total.set("")


def price():
    r =Tk()
    r.geometry("600x200")
    r.title("Price list")
    labelInfo =Label(r, font=("arial", 15, "bold"), text="ITEM", foreground="black").grid(row=0, column=0)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="_", foreground="white").grid(row=0, column=1)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="PRICE", foreground="black").grid(row=0, column=2)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="FRIES", foreground="steel blue").grid(row=1, column=0)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="$" +str("%.2f"% price_lister["Fries"]), foreground="black").grid(row=1, column=2)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="LARGE FRIES", foreground="steel blue").grid(row=2, column=0)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="$" +str("%.2f"% price_lister["Large Fries"]), foreground="black").grid(row=2, column=2)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="HAMBURGER", foreground="steel blue").grid(row=3, column=0)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="$" +str("%.2f"% price_lister["Hamburger"]), foreground="black").grid(row=3, column=2)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="FILET", foreground="steel blue").grid(row=4, column=0)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="$" +str("%.2f"% price_lister["Filet"]), foreground="black").grid(row=4, column=2)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="CHEESE BURGER", foreground="steel blue").grid(row=5, column=0)
    labelInfo =Label(r, font=("arial", 15, "bold"), text="$" +str("%.2f"% price_lister["Cheese Burger"]), foreground="black").grid(row=5, column=2)
    labelInfo =Label(r, font=("arial", 10, "bold"), text="DRINKS", foreground="steel blue").grid(row=6, column=0)
    labelInfo =Label(r, font=("arial", 10, "bold"), text="$" +str("%.2f"% price_lister["Drinks"]), foreground="black").grid(row=6, column=2)
    r.mainloop()


labelfries= Label(frame1, font=("arial", 16, "bold"), text="Fries").grid(row=0, column=0)
text_fries = Entry(frame1, font=("arial", 16, "bold"), textvariable=fries, borderwidth=6, background="white", justify="right")
text_fries.grid(row=0, column=1)


label_largefries= Label(frame1, font=("arial", 16, "bold"), text="Large Fries").grid(row=1, column=0)
text_largefries = Entry(frame1, font=("arial", 16, "bold"), textvariable=largefries , borderwidth=6, background="white", justify="right")
text_largefries.grid(row=1, column=1)

label_humburger= Label(frame1, font=("arial", 16, "bold"), text="Hamburger").grid(row=2, column=0)
text_humburger = Entry(frame1, font=("arial", 16, "bold"), textvariable=ham_burger, borderwidth=6, background="white", justify="right")
text_humburger.grid(row=2, column=1)

label_filet= Label(frame1, font=("arial", 16, "bold"), text="Filet'o Fish").grid(row=3, column=0)
text_filet = Entry(frame1, font=("arial", 16, "bold"), textvariable=filet, borderwidth=6, background="white", justify="right")
text_filet.grid(row=3, column=1)

label_cheese_burger = Label(frame1, font=("arial", 16, "bold"), text="Cheese Burger").grid(row=4, column=0)
text_cheese_burger = Entry(frame1, font=("arial", 16, "bold"), textvariable=cheese_burger, borderwidth=6, background="white", justify="right")
text_cheese_burger.grid(row=4, column=1)

label_drinks = Label(frame1, font=("arial", 16, "bold"), text="Drink").grid(row=5, column=0)
drink_text = Entry(frame1, font=("arial", 16, "bold"), textvariable=drinks, borderwidth=6, background="white", justify="right")
drink_text.grid(row=5, column=1)

label_order_no=Label(frame1, font= ("arial", 16, "bold"),text="Order No", foreground="steel blue").grid(row=0, column=2)
order_no_text=Entry(frame1, font=("arial", 16, "bold"), textvariable=order_no, borderwidth=6, background="powder blue", justify="right")
order_no_text.grid(row=0, column=3)

cost_label=Label(frame1, font= ("arial", 16, "bold"),text="Cost", foreground="steel blue").grid(row=1, column=2)
cost_text=Entry(frame1, font=("arial", 16, "bold"), textvariable=cost, borderwidth=6, background="powder blue", justify="right")
cost_text.grid(row=1, column=3)

service_charge_label=Label(frame1, font= ("arial", 16, "bold"),text="Service Charges", foreground="steel blue").grid(row=2, column=2)
service_charge_text=Entry(frame1, font=("arial", 16, "bold"), textvariable=service_charge, borderwidth=6, background="powder blue", justify="right")
service_charge_text.grid(row=2, column=3)

tax_label=Label(frame1, font= ("arial", 16, "bold"),text="Tax", foreground="steel blue").grid(row=3, column=2)
tax_text=Entry(frame1, font=("arial", 16, "bold"), textvariable=tax, borderwidth=6, background="powder blue", justify="right")
tax_text.grid(row=3, column=3)

subtotal_label=Label(frame1, font= ("arial", 16, "bold"),text="Subtotal", foreground="steel blue").grid(row=4, column=2)
subtotal_text=Entry(frame1, font=("arial", 16, "bold"), textvariable=subtotal, borderwidth=6, background="powder blue", justify="right")
subtotal_text.grid(row=4, column=3)

total_label=Label(frame1, font= ("arial", 16, "bold"),text="Total", foreground="steel blue").grid(row=5, column=2)
total_text=Entry(frame1, font=("arial", 16, "bold"), textvariable=total, borderwidth=6, background="powder blue", justify="right")
total_text.grid(row=5, column=3)



label_Total = Label(frame1, text="-", foreground="white")
label_Total.grid(row=6, columnspan=4)

btnPrice= Button(frame1, padx=16, pady=8, border=10, foreground="black", font=("arial", 16, "bold"), width=16, text="PRICE", background="powder blue", command=price)
btnPrice.grid(row=7, column=0)

btnTotal= Button(frame1, padx=16, pady=8, border=10, foreground="black", font=("arial", 16, "bold"), width=16, text="TOTAL", background="powder blue", command=bill)
btnTotal.grid(row=7, column=1)

btnReset= Button(frame1, padx=16, pady=8, border=10, foreground="black", font=("arial", 16, "bold"), width=16, text="RESET", background="powder blue", command=reset)
btnReset.grid(row=7, column=2)

btnExit= Button(frame1, padx=16, pady=8, border=10, foreground="black", font=("arial", 16, "bold"), width=16, text="EXIT", background="powder blue", command=exit)
btnExit.grid(row=7, column=3)

root.mainloop()