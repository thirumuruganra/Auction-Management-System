from tkinter import *
from tkinter import messagebox
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password='root', charset='utf8', database='auction')
cur = con.cursor()
aucTable = "auctionitems"
BidTable = 'bid'


def wbid():
    root = Tk()
    root.title("CV")
    root.geometry("900x800")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#85DCB0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#E27D60", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Highest Bids", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25
    # to push the grid down by 6 rows
    Label(labelFrame, text="", bg='black').grid(row=1, column=0)
    Label(labelFrame, text="", bg='black').grid(row=2, column=1)
    Label(labelFrame, text="", bg='black').grid(row=3, column=2)
    Label(labelFrame, text="", bg='black').grid(row=4, column=0)
    Label(labelFrame, text="", bg='black').grid(row=5, column=0)
    Label(labelFrame, text="", bg='black').grid(row=6, column=0)
    # column headings
    attributes = ["Item ID", "Item Name", "Customer Name", "Winning Bid"]
    for i in range(len(attributes)):
        Label(labelFrame, text="\t           " + attributes[i], bg='black', fg='white', anchor='center').grid(row=3,
                                                                                                              column=i + 1)
    Label(labelFrame,
          text="-----------------------------------------------------------------------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)
    try:
        cur.execute("select itemid,itemname,customername,bidprice from bid natural join auctionitems where (itemid,bidprice) in (select itemid, max(bidprice) from bid group by itemid) order by itemid")
        data = cur.fetchall()
        con.commit()
        # using grid() function for alignment
        rows = len(data)
        columns = len(data[0])
        for i in range(rows):
            for j in range(columns):
                Label(labelFrame, text="\t           {}".format(data[i][j]), bg='black', fg='white').grid(row=i + 6,
                                                                                                          column=j + 1)
    except:
        messagebox.showinfo("Error", "Failed to fetch records from database")
    quitBtn = Button(root, text="CLOSE", bg='light blue', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.85, relwidth=0.18, relheight=0.08)
    root.mainloop()
