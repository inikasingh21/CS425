/* Displays every employee with salary greater than $50,000, in ascending order of salary. Also shows their occupation */
select First_name, Last_name, e.Occ_name, Salary from employee as e left join occupation as o on e.Occ_name = o.Occ_name where Salary > 50000.00 order by Salary asc;

/* Displays all rooms (and their types) where smoking is allowed */
select Room_no, Type_name, If_smoking from room as r left join roomtype as rt on r.Type_ID = rt.Type_ID where If_smoking = 'Y';

/* Shows number of rooms in Marriott Hotels in Chicago (for those unsure how to spell Chicago) */
select h.Hotel_ID, Hotel_name, Location, Num_rooms from hotel as h left join building as b on h.Hotel_ID = b.Hotel_ID where Location like 'Chi_a%';

/* Displays every booking for a three-day stay, in ascending order of arrival date */
select Booking_ID, Arrival_date, Departure_date from booking where DATEDIFF(Departure_date, Arrival_date) = 3 and Departure_date > Arrival_date order by Arrival_date asc;

/* Displays every female employee, from youngest to oldest */
select Employee_ID, First_name, Last_name, Gender, DOB from employee where Gender = 'F' order by DOB desc;

/* Displays every 5-star hotel */
select Hotel_name, Location, Num_stars from hotel where Num_stars = 5;

/* Displays every single room type and its price; room types are split into quartiles according to their prices */
select Type_name, Room_price, ntile(4) over (order by Room_price asc) as Quartile from roomtype;

/* Shows every employee who works in Los Angeles */
select e.Employee_ID, First_name, Last_name, Location from employee as e left join employed as d on e.Employee_ID = d.Employee_ID left join hotel as h on d.Hotel_ID = h.Hotel_ID where Location = 'Los Angeles';

/* Shows the name, email address and phone number of every person in the database, guest or employee */
select g.First_name as `First Name`, g.Last_name as `Last Name`, Guest_email as Email, Guest_phone as `Phone Number` from guest as g union select e.First_name as `First Name`, e.Last_name as `Last Name`, Employee_email as Email, Employee_phone as `Phone Number` from employee as e order by `Last Name` asc;

/* Displays every guest who booked a room with a TV */
select Guest_Name, r.Room_no, Amenities from bookingname as bn left join booking as b on bn.Booking_ID = b.Booking_ID left join room as r on b.Booking_ID = r.Booking_ID left join roomamenities as ra on r.Room_no = ra.Room_no where Amenities like 'TV%';