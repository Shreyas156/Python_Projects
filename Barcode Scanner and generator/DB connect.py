import sqlite3

con = sqlite3.connect("tempdb.db")
# con.execute("create table emp (empid number(3), empname varchar(15), empcity varchar(15) )");
try:
    # a = con.execute("insert into stud_info values(15,'Ravi','Aurangabad')")
    con.execute("insert into stud_info values(21, 'Om', 'Aurangabad')")
    con.commit()
except Exception as ex:
    print(ex)
print("Data saved")
