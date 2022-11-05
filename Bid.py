from tkinter import *
import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(host="localhost", user="root", password="root", charset='utf8', database='auction')
cur = con.cursor()
cur.execute("create table if not exists bid(itemid varchar(12),customername varchar(20) not null,bidprice int)")
def aucRegister():
    itemid = Info1.get()
    customername = Info2.get()
    bidprice = Info3.get()
    insertitems = "insert ignore into " + aucTable + " values('" + itemid + "','" + customername + "','" + bidprice + "')"
    try:
        if itemid == '' and customername == '' and bidprice == '':
            messagebox.showinfo("Error", "Fields are empty")
        else:
            cur.execute(insertitems)
            con.commit()
            messagebox.showinfo("Success", "Bidding successful")
    except Exception as e:
        messagebox.showinfo("Error", "Item Id already present" )
    print(itemid)
    print(customername)
    print(bidprice)
    root.destroy()
def bid():
    global Info1, Info2, Info3, Canvas1, con, cur, aucTable, root

    root = Tk()
    root.title("CV")
    root.geometry("600x600")
    aucTable = "bid"  # bid Table
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#85DCB0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#E27D60", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Bid Details", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Item ID
    lb1 = Label(labelFrame, text="Item ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Customer name
    lb2 = Label(labelFrame, text="Customer Name : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    Info2 = Entry(labelFrame)
    Info2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Final Price
    lb3 = Label(labelFrame, text="Final Price : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    Info3 = Entry(labelFrame)
    Info3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='light blue', fg='black', command=aucRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="CLOSE", bg='light blue', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()