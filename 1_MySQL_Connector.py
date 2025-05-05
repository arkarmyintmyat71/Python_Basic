# import tkinter
from tkinter import *

# import messagebox from tkinter
import tkinter.messagebox as msgbox

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
        msgbox.showinfo("ALERT", "Please fill all entries!")
    else:
        con = mysql.connect(host = "localhost", user = "root", password = "Arkar123#@!", database = "mysql_connector_py")
        cursor = con.cursor()
        cursor.execute("insert into person values('" + id + "', '" + name + "', '" + phone + "')")
        cursor.execute("commit")
        msgbox.showinfo("Status", "Successfully Inserted!")
        con.close()

#Create Delete function
def Delete():
    id = id_Entry.get()

    if id == "":
        msgbox.showinfo("ALERT", "Please fill id for delete!")
    else:
        con = mysql.connect(host = "localhost", user = "root", password = "Arkar123#@!", database = "mysql_connector_py")
        cursor = con.cursor()
        cursor.execute("delete from person where id = '" + id + "'")
        cursor.execute("commit")
        msgbox.showinfo("Status", "Successfully Deleted!")

        id_Entry.delete(0, END)
        name_Entry.delete(0, END)
        phone_Entry.delete(0, END)

        con.close()

#Create Update function
def Update():
    id = id_Entry.get()
    name = name_Entry.get()
    phone = phone_Entry.get()

    if name == "" or phone == "":
        msgbox.showinfo("ALERT", "Please fill name and phone for update!")
    else:
        con = mysql.connect(host="localhost", user="root", password="Arkar123#@!", database="mysql_connector_py")
        cursor = con.cursor()
        cursor.execute("update person set name = '" + name + "', phone = '" + phone + "' where id = '" + id + "'")
        cursor.execute("commit")
        msgbox.showinfo("Status", "Successfully Updated!")
        con.close()

#Create Select function
def Select():
    id = id_Entry.get()
    name = name_Entry.get()
    phone = phone_Entry.get()

    if id == "":
        msgbox.showinfo("ALERT", "Please fill id for select!")
    else:
        con = mysql.connect(host="localhost", user="root", password="Arkar123#@!", database="mysql_connector_py")
        cursor = con.cursor()
        cursor.execute("select * from person where id = '" + id + "'")
        rows = cursor.fetchall()
        for row in rows:
            name_Entry.insert(0, row[1])
            phone_Entry.insert(0, row[2])
        cursor.execute("commit")
        con.close()

#Create Labels and Entries
id_label = Label(root, text = "Enter ID: ", font= "Aerial 15")
id_label.place(x=30, y=30)
id_Entry = Entry(root, font= "Aerial 15")
id_Entry.place(x=150, y=30)
id_Entry.focus()


name_label = Label(root, text = "Enter Name: ", font= "Aerial 15")
name_label.place(x=30, y=80)
name_Entry = Entry(root, font= "Aerial 15")
name_Entry.place(x=150, y=80)

phone_label = Label(root, text = "Enter Phone: ", font= "Aerial 15")
phone_label.place(x=30, y=130)
phone_Entry = Entry(root, font= "Aerial 15")
phone_Entry.place(x=150, y=130)

#Insert Button
inset_btn = (Button(root, text= "Insert", command= Insert,font= "Aerial 18", background= "blue")
             .place(x=30, y=180))
#Delete Button
delete_btn = (Button(root, text= "Delete", command= Delete,font= "Aerial 18", background= "red")
             .place(x=130, y=180))
#Update Button
update_btn = (Button(root, text= "Update", command= Update,font= "Aerial 18", background= "yellow")
             .place(x=230, y=180))
#Select Button
select_btn = (Button(root, text= "Select", command= Select,font= "Aerial 18", background= "orange")
             .place(x=350, y=180))
root.mainloop()


