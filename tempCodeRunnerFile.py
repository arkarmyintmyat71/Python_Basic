# import tkinter
from tkinter import *

# import messagebox from tkinter
import tkinter.messagebox as Msgbox

# import mysql connector
import mysql.connector as mysql

# create tkinter window
root = Tk()
root.geometry("500x400")
root.title("mysql_connector.com")

#Create Insert function
def Insert():
    id = id_Entry.get()
    name = name_Entry.get()
    phone = phone_Entry.get()

    if id == "" or name == "" or phone == "":
        Msgbox.showinfo("ALERT", "Please fill all entries!")
    else:
        con = mysql.connect(host = "localhost", user = "arkar", password = "Arkar123#@!", database = "mysql_connector_py")
        cursor = con.cursor()
        cursor.execute("insert into person values('" + id + "', '" + name + "', '" + phone + "')")
        cursor.execute("commit")
        Msgbox.showinfo("Status", "Successfully Inserted!")
        con.close()

#Create Labels and Entries
id_label = Label(root, text = "Enter ID: ", font= "Aerial 15")
id_label.place(x=30, y=30)
id_Entry = Entry(root, font="Arial 15")
id_Entry.place(x=150, y=30)
id_Entry.focus()


name_label = Label(root, text = "Enter Name: ", font= "Aerial 15")
name_label.place(x=30, y=80)
name_Entry = Entry(root, font="Arial 15")
name_Entry.place(x=150, y=80)

phone_label = Label(root, text = "Enter Phone: ", font= "Aerial 15")
phone_label.place(x=30, y=130)
phone_Entry = Entry(root, font="Arial 15")
phone_Entry.place(x=150, y=130)

#Insert Button
inset_btn = Button(root, text= "Insert", command= Insert, font= "Arial 18",
                   background="blue").place(x=50, y=180)
root.mainloop()


