create table Guest ( 
Guest_ID int not null, 
Guest_email VARCHAR(128),
Last_name VARCHAR(20),
First_name VARCHAR(20),
Guest_phone VARCHAR(15), 
Gender char(1),
DOB date,
License_no VARCHAR(10),
primary key (Guest_ID)
);

create table Hotel(
Hotel_ID int not null, 
Hotel_name VARCHAR (20), 
Location VARCHAR(20), 
Num_stars int (1),
primary key (Hotel_ID)
);

create table RoomType(
Type_ID int not null,
Type_name VARCHAR (20),
Bed_num int (2), 
Room_price decimal (5,2), 
If_wifi char(1), 
If_balcony char(1),
primary key(Type_ID)
);

create table Occupation(
Occ_name VARCHAR (32),
Salary decimal (9,2), 
Department VARCHAR(25),
primary key (Occ_name)
); 

create table Employee(
Employee_ID int not null,
First_name VARCHAR (20),
Last_name VARCHAR (20),
Employee_email VARCHAR(128),
Employee_phone VARCHAR(15), 
Gender char(1), 
License_info VARCHAR(10), 
DOB date,
Occ_name VARCHAR (32),
primary key (Employee_ID),
foreign key (Occ_name) references Occupation(Occ_name)
);

create table Booking(
Booking_ID int not null,
Total_price decimal (8,2),
Num_of_children int(2),
Num_of_adults int(2),
Payment_method VARCHAR(15),
Departure_date date, 
Arrival_date date, 
Guest_ID int not null, 
Employee_ID int not null, 
Hotel_ID int not null,
primary key (Booking_ID),
foreign key (Guest_ID) references Guest(Guest_ID),
foreign key (Employee_ID) references Employee(Employee_ID),
foreign key (Hotel_ID) references Hotel(Hotel_ID)
);

create table BookingName(
Booking_ID int not null,
Guest_Name VARCHAR (50),
CONSTRAINT PK_BookingName PRIMARY KEY (Booking_ID, Guest_Name),
foreign key(Booking_ID) references Booking(Booking_ID)
);

create table Building(
Hotel_ID int not null, 
Num_rooms int not null,
Building_no int not null, 
Num_floors int not null,
CONSTRAINT PK_Building PRIMARY KEY (Hotel_ID, Num_rooms, Building_no, Num_floors),
foreign key (Hotel_ID) references Hotel(Hotel_ID)
);

create table Room (
Room_no int not null,
If_smoking char (1),
Floor_no int (2), 
Num_of_People int(2),
Booking_ID int not null, 
Hotel_ID int not null,
Type_ID int not null, 
Num_rooms int not null, 
Building_no int not null, 
Num_floors int not null,
primary key (Room_no),
foreign key(Booking_ID) references Booking(Booking_ID),
foreign key (Hotel_ID, Num_rooms, Building_no, Num_floors) references Building(Hotel_ID, Num_rooms, Building_no, Num_floors),
foreign key (Type_ID) references RoomType(Type_ID)
);

create table RoomAmenities (
Room_no int not null,
Amenities VARCHAR (20),
CONSTRAINT PK_RoomAmenities PRIMARY KEY (Room_no, Amenities),
foreign key (Room_no) references Room(Room_no)
);

create table Employed(
Employee_ID int not null,
Hotel_ID int not null,
Employed_ID int not null,
CONSTRAINT PK_Employed PRIMARY KEY (Employee_ID, Hotel_ID, Employed_ID),
foreign key (Employee_ID) references Employee(Employee_ID),
foreign key (Hotel_ID) references Hotel(Hotel_ID)
);
