from tkinter import *
import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(host="localhost", user="root", password='root', charset='utf8', database='auction')
cur = con.cursor()


def updateitem():
    itemnme = Inf2.get()
    baseprce = Inf3.get()
    manufact = Inf4.get()
    try:
        cur.execute(
            "update auctionitems set itemname='{}',baseprice={},manufacturer='{}' where itemid={}".format(itemnme,
                                                                                                          baseprce,
                                                                                                          manufact,
                                                                                                          itemid))
        con.commit()
        messagebox.showinfo("Success", "item details updated successfully")
    except Exception as e:
        messagebox.showinfo("Error", "Enter the details" + str(e))

    root.destroy()
    root1.destroy()


def checkitemid():
    global root1, Info1, Inf2, Inf3, Inf4, itemid
    itemid = Info1.get()
    cur.execute("select * from auctionitems")
    row = cur.fetchall()
    for i in row:
        if i[0] == itemid:
            root1 = Tk()
            root1.title("CV")
            root1.geometry("800x800")
            Canvas1 = Canvas(root1)
            Canvas1.config(bg="#85DCB0")
            Canvas1.pack(expand=True, fill=BOTH)
            labelFrame = Frame(root1, bg='black')
            labelFrame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.3)
            Label(labelFrame, text="", bg='black').grid(row=1, column=0)
            Label(labelFrame, text="", bg='black').grid(row=2, column=0)
            Label(labelFrame, text="", bg='black').grid(row=3, column=0)
            Label(labelFrame, text="", bg='black').grid(row=4, column=0)
            Label(labelFrame, text="", bg='black').grid(row=5, column=0)
            Label(labelFrame, text="", bg='black').grid(row=6, column=0)
            Label(labelFrame, text="\t\tOld Details", bg='black', fg='white', font=('courier', 14)).place(relx=0.05,rely=0.10)
            Label(labelFrame, text="------------------------------------------------------------------", bg='black', fg='white').place(
                relx=0.1, rely=0.25)
            Label(labelFrame, text="Item ID\t\tItem Name                  Base Price\t     Manufacturer", bg='black', fg='white').place(
                relx=0.05, rely=0.35)
            Label(labelFrame, text="------------------------------------------------------------------------------------",
                  bg='black', fg='white').place(relx=0.05, rely=0.45)
            for j in range(len(i)):
                Label(labelFrame, text="\t     {}".format(i[j]), bg='black', fg='white').grid(row=7,column=j)
            labelFrame1 = Frame(root1, bg='black')
            labelFrame1.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.3)

            Label(labelFrame1, text="\tEnter the Details to be Modified", bg='black', fg='white',
                  font=('courier', 14)).place(relx=0.05, rely=0.1)
            Label(labelFrame1, text="---------------------------------------------------------------------------------------------------------", bg='black', fg='white').place(
                relx=0.05, rely=0.25)
            # Item name
            lb2 = Label(labelFrame1, text="Item Name : ", bg='black', fg='white')
            lb2.place(relx=0.05, rely=0.35, relheight=0.08)

            Inf2 = Entry(labelFrame1)
            Inf2.place(relx=0.3, rely=0.35, relwidth=0.40, relheight=0.08)

            Inf2.insert(0, i[1])
            # Base Price
            lb3 = Label(labelFrame1, text="Base Price : ", bg='black', fg='white')
            lb3.place(relx=0.05, rely=0.50, relheight=0.08)

            Inf3 = Entry(labelFrame1)
            Inf3.place(relx=0.3, rely=0.50, relwidth=0.40, relheight=0.08)
            Inf3.insert(0, i[2])
            # Manufacturer
            lb4 = Label(labelFrame1, text="Manufacturer : ", bg='black', fg='white')
            lb4.place(relx=0.05, rely=0.65, relheight=0.08)

            Inf4 = Entry(labelFrame1)
            Inf4.place(relx=0.3, rely=0.65, relwidth=0.40, relheight=0.08)
            Inf4.insert(0, i[3])

            # Update Button
            UpdateBtn = Button(root1, text="UPDATE", bg='light blue', fg='black', command=updateitem)
            UpdateBtn.place(relx=0.28, rely=0.85, relwidth=0.18, relheight=0.08)

            quitBtn = Button(root1, text="CLOSE", bg='light blue', fg='black', command=root1.destroy)
            quitBtn.place(relx=0.53, rely=0.85, relwidth=0.18, relheight=0.08)

            root1.mainloop()
            break

    else:
        messagebox.showinfo("Error", "Check the item id")
        root.destroy()


def update():
    global Info1, Inf2, Inf3, Inf4, Canvas1, con, cur, aucTable, root

    root = Tk()
    root.title("CV")
    root.geometry("800x800")

    # Enter Table Names here
    aucTable = "auctionitems"  # item Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#85DCB0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#E27D60", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Update item Details", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)

    # Item ID
    lb1 = Label(labelFrame, text="Item ID to be Searched : ", bg='black', fg='white', font=('Arial', 13))
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    Info1 = Entry(labelFrame)
    Info1.place(relx=0.4, rely=0.2, relwidth=0.40, relheight=0.1)

    checkbtn = Button(root, text="CHECK", bg="light blue", fg="black", command=checkitemid)
    checkbtn.place(relx=0.4, rely=0.5, relwidth=0.18, relheight=0.08)

    root.mainloop()