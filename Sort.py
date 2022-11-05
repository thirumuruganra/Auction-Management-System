from tkinter import *
import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(host="localhost", user="root", password="root", charset='utf8', database="auction")
cur = con.cursor()


def itemid():
    root1 = Tk()
    root1.title("CV")
    root1.geometry("800x800")

    Canvas1 = Canvas(root1)
    Canvas1.config(bg="#85DCB0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root1, bg="#E27D60", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Ascending order", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root1, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="", bg='black').grid(row=1, column=0)
    Label(labelFrame, text="", bg='black').grid(row=2, column=0)
    Label(labelFrame, text="", bg='black').grid(row=3, column=0)
    Label(labelFrame, text="", bg='black').grid(row=4, column=0)
    Label(labelFrame, text="", bg='black').grid(row=5, column=0)
    Label(labelFrame, text="", bg='black').grid(row=6, column=0)
    attributes = ["Item ID", "Item Name", "Base Price", "Manufacturer"]
    for i in range(len(attributes)):
        Label(labelFrame, text=" \t          " + attributes[i], bg='black', fg='white', anchor='center').grid(row=3,
                                                                                                              column=i)
    Label(labelFrame,
          text="-----------------------------------------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)

    try:
        cur.execute("select * from auctionitems order by itemid")
        data = cur.fetchall()
        con.commit()
        # using grid() function for alignment
        rows = len(data)
        columns = len(data[0])
        for i in range(rows):
            for j in range(columns):
                Label(labelFrame, text="\t          {}".format(data[i][j]), bg='black', fg='white').grid(row=i + 6,column=j)

    except:
        messagebox.showinfo("Error", "Failed to fetch records from database")

    quitBtn = Button(root1, text="CLOSE", bg='light blue', fg='black', command=root1.destroy)
    quitBtn.place(relx=0.4, rely=0.85, relwidth=0.18, relheight=0.08)

    root1.mainloop()


def itemname():
    root2 = Tk()
    root2.title("CV")
    root2.geometry("800x800")

    Canvas1 = Canvas(root2)
    Canvas1.config(bg="#85DCB0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root2, bg="#E27D60", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Ascending order", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root2, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="", bg='black').grid(row=1, column=0)
    Label(labelFrame, text="", bg='black').grid(row=2, column=0)
    Label(labelFrame, text="", bg='black').grid(row=3, column=0)
    Label(labelFrame, text="", bg='black').grid(row=4, column=0)
    Label(labelFrame, text="", bg='black').grid(row=5, column=0)
    Label(labelFrame, text="", bg='black').grid(row=6, column=0)
    attributes = ["Item ID", "Item Name", "Base Price", "Manufacturer"]
    for i in range(len(attributes)):
        Label(labelFrame, text=" \t          " + attributes[i], bg='black', fg='white', anchor='center').grid(row=3,
                                                                                                              column=i)
    Label(labelFrame,
          text="-----------------------------------------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)

    try:
        cur.execute("select * from auctionitems order by itemname")
        data = cur.fetchall()
        con.commit()
        # using grid() function for alignment
        rows = len(data)
        columns = len(data[0])
        for i in range(rows):
            for j in range(columns):
                Label(labelFrame, text="\t          {}".format(data[i][j]), bg='black', fg='white').grid(row=i + 6,
                                                                                                         column=j)

    except:
        messagebox.showinfo("Error", "Failed to fetch records from database")
    quitBtn = Button(root2, text="CLOSE", bg='light blue', fg='black', command=root2.destroy)
    quitBtn.place(relx=0.4, rely=0.85, relwidth=0.18, relheight=0.08)

    root2.mainloop()


def baseprice():
    root3 = Tk()
    root3.title("CV")
    root3.geometry("800x800")

    Canvas1 = Canvas(root3)
    Canvas1.config(bg="#85DCB0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root3, bg="#E27D60", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Ascending order", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root3, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="", bg='black').grid(row=1, column=0)
    Label(labelFrame, text="", bg='black').grid(row=2, column=0)
    Label(labelFrame, text="", bg='black').grid(row=3, column=0)
    Label(labelFrame, text="", bg='black').grid(row=4, column=0)
    Label(labelFrame, text="", bg='black').grid(row=5, column=0)
    Label(labelFrame, text="", bg='black').grid(row=6, column=0)
    attributes = ["Item ID", "Item Name", "Base Price", "Manufacturer"]
    for i in range(len(attributes)):
        Label(labelFrame, text=" \t          " + attributes[i], bg='black', fg='white', anchor='center').grid(row=3,
                                                                                                              column=i)
    Label(labelFrame,
          text="-----------------------------------------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)

    try:
        cur.execute("select * from auctionitems order by baseprice")
        data = cur.fetchall()
        con.commit()
        # using grid() function for alignment
        rows = len(data)
        columns = len(data[0])
        for i in range(rows):
            for j in range(columns):
                Label(labelFrame, text="\t          {}".format(data[i][j]), bg='black', fg='white').grid(row=i + 6,
                                                                                                         column=j)

    except:
        messagebox.showinfo("Error", "Failed to fetch records from database")

    quitBtn = Button(root3, text="CLOSE", bg='light blue', fg='black', command=root3.destroy)
    quitBtn.place(relx=0.4, rely=0.85, relwidth=0.18, relheight=0.08)

    root3.mainloop()


def sort():
    # Add your own database name and password here to reflect in the code
    con = mysql.connector.connect(host="localhost", user="root", password="root", charset='utf8', database="auction")
    cur = con.cursor()

    root = Tk()
    root.title("CV")
    root.geometry("800x800")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#85DCB0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#E27D60", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="SORT ACCORDING TO", bg='black', fg='white', font=('Courier', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="Item ID", bg='black', fg='white', font=('Courier', 15), command=itemid)
    btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Item Name", bg='black', fg='white', font=('Courier', 15), command=itemname)
    btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn3 = Button(root, text="Base price", bg='black', fg='white', font=('Courier', 15), command=baseprice)
    btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn6 = Button(root, text="CLOSE", bg='light blue', fg='black', font=('Courier', 15), command=root.destroy)
    btn6.place(relx=0.38, rely=0.8, relwidth=0.25, relheight=0.1)

    root.mainloop()