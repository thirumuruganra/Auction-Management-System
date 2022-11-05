from tkinter import *
from tkinter import messagebox
import mysql.connector

mypass = "root"
mydatabase = "auction"

con = mysql.connector.connect(host="localhost", user="root", password=mypass, charset='utf8', database=mydatabase)
cur = con.cursor()

aucTable = "auctionitems"  # auctionitems Table


def deleteitem():
    itemid = Info1.get()
    cur.execute("select * from auctionitems")
    row = cur.fetchall()
    for i in row:
        if (i[0] == itemid):
            cur.execute("delete from auctionitems where itemid = {}".format(itemid))
            cur.execute("delete from bid where itemid = {}".format(itemid))
            con.commit()
            messagebox.showinfo("Success", "Auction Items Record Deleted Successfully")
            break
    else:
        messagebox.showinfo("Error", "Please check the Item ID")
    print(itemid)

    Info1.delete(0, END)
    root.destroy()


def delete():
    global Info1, Canvas1, con, cur, stuTable, root

    root = Tk()
    root.title("CV")
    root.minsize(width=400, height=400)
    root.geometry("800x900")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#85DCB0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#E27D60", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Item", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Item ID to Delete
    lb2 = Label(labelFrame, text="Item ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.15)

    Info1 = Entry(labelFrame)
    Info1.place(relx=0.2, rely=0.15, relwidth=0.62)
    #Display table
    Label(labelFrame, text="Item ID\t\t     Item Name", bg='black',fg='white').place( relx=0.05, rely=0.3)
    Label(labelFrame,text="------------------------------------",bg='black', fg='white').place(relx=0.05, rely=0.4)
    cur.execute("select * from auctionitems")
    data = cur.fetchall()
    con.commit()
    y=0.5
    for i in data:
        Label(labelFrame, text=" {} \t\t  {} ".format(i[0],i[1]), bg='black',fg='white').place(relx=0.07, rely=y)
        y += 0.1
    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='light blue', fg='black', command=deleteitem)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="CLOSE", bg='light blue', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()