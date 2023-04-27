from tkinter import *
import tkinter as tk
from tkinter import ttk
from query_functions import execute_query
import mysql.connector
from mysql.connector import Error


root = Tk()
def display_results(results, cursor):
    root = tk.Tk()
    #root.title("Marriot Hotel Database") # set the window tit
    tree = ttk.Treeview(root)

    # configure the columns of the treeview using cursor.description
    columns = [desc[0] for desc in cursor.description]
    tree["columns"] = columns
    tree.column("#0", width=0, stretch=tk.NO)
    for column in columns:
        tree.column(column, anchor=tk.CENTER)
        tree.heading(column, text=column, anchor=tk.CENTER)

    # add the data to the treeview
    for row in results:
        tree.insert("", tk.END, values=row)

    tree.pack()
    root.mainloop()


    # Queries
def run_query1():
    query = " SELECT First_name, Last_name, e.Occ_name, Salary from employee as e left join occupation as o on e.Occ_name = o.Occ_name where Salary > 50000.00 order by Salary asc"
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="YOURDBNAME"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    display_results(results, cursor)
    cursor.close()
    connection.close()

def run_query2():
    query = "select Room_no, Type_name, If_smoking from room as r left join roomtype as rt on r.Type_ID = rt.Type_ID where If_smoking = 'Y';"
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="YOURDBNAME"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    display_results(results, cursor)
    cursor.close()
    connection.close()


def run_query2():
    query = "select Room_no, Type_name, If_smoking from room as r left join roomtype as rt on r.Type_ID = rt.Type_ID where If_smoking = 'Y';"
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="YOURDBNAME"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    display_results(results, cursor)
    cursor.close()
    connection.close()

def run_query3():
    query = "select h.Hotel_ID, Hotel_name, Location, Num_rooms from hotel as h left join building as b on h.Hotel_ID = b.Hotel_ID where Location like 'Chi_a%'"
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="YOURDBNAME"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    display_results(results, cursor)
    cursor.close()
    connection.close()   


def run_query4():
    query = "select Booking_ID, Arrival_date, Departure_date from booking where DATEDIFF(Departure_date, Arrival_date) = 3 and Departure_date > Arrival_date order by Arrival_date asc"
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="YOURDBNAME"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    display_results(results, cursor)
    cursor.close()
    connection.close() 

def run_query5():
    query = "select Employee_ID, First_name, Last_name, Gender, DOB from employee where Gender = 'F' order by DOB desc"
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="YOURDBNAME"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    display_results(results, cursor)
    cursor.close()
    connection.close() 

def run_query6():
    query = "select Hotel_name, Location, Num_stars from hotel where Num_stars = 5"
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="YOURDBNAME"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    display_results(results, cursor)
    cursor.close()
    connection.close() 

def run_query7():
    query = "select Type_name, Room_price, ntile(4) over (order by Room_price asc) as Quartile from roomtype"
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="YOURDBNAME"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    display_results(results, cursor)
    cursor.close()
    connection.close() 


def run_query8():
    query = "select e.Employee_ID, First_name, Last_name, Location from employee as e left join employed as d on e.Employee_ID = d.Employee_ID left join hotel as h on d.Hotel_ID = h.Hotel_ID where Location = 'Los Angeles'"
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="YOURDBNAME"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    display_results(results, cursor)
    cursor.close()
    connection.close() 


def run_query9():
    query = "select g.First_name as `First Name`, g.Last_name as `Last Name`,Guest_email as Email, Guest_phone as `Phone Number` from guest as g union select e.First_name as `First Name`, e.Last_name as `Last Name`, Employee_email as Email, Employee_phone as `Phone Number` from employee as e order by `Last Name` asc"
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="YOURDBNAME"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    display_results(results, cursor)
    cursor.close()
    connection.close() 


def run_query10():
    query = "select Guest_Name, r.Room_no, Amenities from bookingname as bn left join booking as b on bn.Booking_ID = b.Booking_ID left join room as r on b.Booking_ID = r.Booking_ID left join roomamenities as ra on r.Room_no = ra.Room_no where Amenities like 'TV%'"
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="YOURDBNAME"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    display_results(results, cursor)
    cursor.close()
    connection.close() 


# create the Tkinter window


def employeeWindow():
	newWindow = Toplevel(root)

	# title
	newWindow.title("Employee Menu")

	# employee view menu
	Label(newWindow, text ="Employee Menu", width= 45, height=5).pack()
	Label(newWindow).pack()
	Button(newWindow, text="Room availibility in Chicago", command=run_query3 ).pack() #3
	Button(newWindow, text="Check bookings for 3-day stays", command=run_query4).pack() #4
	Button(newWindow, text="Check bookings for TV rooms",command=run_query10).pack() #10
	Label(newWindow).pack()


# function to open a new guest window
def guestWindow():
	newWindow = Toplevel(root)

	# title
	newWindow.title("Guest Menu")

	# guest view menu 
	Label(newWindow, text ="Guest Menu", width=35, height=5).pack()
	Label(newWindow).pack()
	Button(newWindow, text="Look for smoking rooms",command=run_query2).pack() #2
	Button(newWindow, text="Look for 5-star hotels",command=run_query6).pack() #6
	Button(newWindow, text="Check and filter room prices",command=run_query7).pack() #7
	Label(newWindow).pack()
	

# function to open a new manager window
def managerWindow():
	newWindow = Toplevel(root)

	# title 
	newWindow.title("Manager Menu")
	# manager menu view
	Label(newWindow, text ="Manager Menu", width=24, height=5).pack()
	Label(newWindow).pack()
	Button(newWindow, text="Check salaries of premium employees",command=run_query1).pack() #1
	Button(newWindow, text="List female employees", command=run_query5).pack() #5
	Button(newWindow, text="Employees located in Los Angeles", command=run_query8).pack() #8
	Button(newWindow, text="Display contact info of guests and employees",command=run_query9).pack() #9
	Label(newWindow).pack()

root.title("Marriot Hotel Database")
hotelWelcome = Label(text="Marriott Hotel Main Menu", font=("Arial", 24,"underline"), fg="#1C136E",bg="#b8e2f4" )
root.geometry("800x500")
root.configure(bg="#b8e2f4")
hotelWelcome.pack()

Employee = Button(text="Employee View", font=("Arial", 14,"underline"), command = employeeWindow, width=24, height=5, fg = "#5C4DE9",)
Employee.pack(side= LEFT)
Guest = Button(text="Guest View", font=("Arial", 14,"underline"), command=guestWindow, width=24, height=5, fg = "#5C4DE9")
Guest.pack(side=LEFT)
Manager = Button(text="Manager View",font=("Arial", 14,"underline"), command=managerWindow, width=24, height=5, fg = "#5C4DE9")
Manager.pack(side= LEFT)

root.mainloop()
