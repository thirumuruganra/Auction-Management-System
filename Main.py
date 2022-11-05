import tkinter
from tkinter import *
#from PIL import ImageTk
#import PIL.Image
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="root", charset='utf8')
cur = con.cursor()
cur.execute("create database if not exists auction")
cur.execute("use auction")
cur.execute("create table if not exists auctionitems(itemid varchar(12) primary key,itemname char(20) not null,baseprice int not null,manufacturer char(30) not null)")

from Add import *
from Bid import *
from Delete import *
from ViewItems import *
from ViewBid import *
from Update import *
from Sort import *
from WinningBid import *

root = Tk()
root.title("CV")
root.geometry("1080x800")

Canvas1 = Canvas(root)

Canvas1.config(bg="#85DCB0")
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root,bg="#E27D60",bd=5)
headingFrame1.place(relx=0,rely=0,relwidth=1,relheight=0.16)

headingLabel = Label(headingFrame1, text=" Welcome to \nOpen Auction", bg='black', fg='white', font=('Courier',20))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Item Details", bg='black', fg='white', font=('Courier', 15), command=add)
btn1.place(relx=0.07, rely=0.25, relwidth=0.4, relheight=0.07)

btn2 = Button(root, text="Bid", bg='black', fg='white', font=('Courier', 15), command=bid)
btn2.place(relx=0.07, rely=0.35, relwidth=0.4, relheight=0.07)

btn3 = Button(root, text="View Item Details", bg='black', fg='white', font=('Courier', 15), command=viewitems)
btn3.place(relx=0.07, rely=0.45, relwidth=0.4, relheight=0.07)

btn4 = Button(root, text="View Bids", bg='black', fg='white', font=('Courier', 15), command=viewbid)
btn4.place(relx=0.07, rely=0.55, relwidth=0.4, relheight=0.07)

btn5 = Button(root, text="Delete Item Details", bg='black', fg='white', font=('Courier', 15), command=delete)
btn5.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.07)

btn6 = Button(root, text="Update Item Details", bg='black', fg='white', font=('Courier', 15), command=update)
btn6.place(relx=0.5, rely=0.35, relwidth=0.4, relheight=0.07)

btn7 = Button(root, text="Sort", bg='black', fg='white', font=('Courier', 15), command=sort)
btn7.place(relx=0.5, rely=0.45, relwidth=0.4, relheight=0.07)

btn8 = Button(root, text="Winning Bid", bg='black', fg='white', font=('Courier', 15), command=wbid)
btn8.place(relx=0.5,rely=0.55, relwidth=0.4,relheight=0.07)

Exitbtn = Button(root,text="Exit",bg='black', fg='white',font=('Courier',15), command = root.destroy)
Exitbtn.place(relx=0.28,rely=0.65, relwidth=0.4,relheight=0.1)


'''
#Adding image
#Specify your file path properly
image = PIL.Image.open(r"C:\thiru\Downloads\Computer Science Project\istockphoto-917901978-612x612.jpg")
img = ImageTk.PhotoImage(image)
l = Label(image=img)
l.place(relx=0.22, rely=0.64)

btn6 = Button(root, text="Exit", bg='black', fg='white', font=('Courier', 15), command=root.destroy)
btn6.place(relx=0.1, rely=8, relwidth=0.45, relheight=0.05)  
'''
root.mainloop()