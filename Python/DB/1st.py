import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="data_science"
)
mycursor = mydb.cursor()

# mycursor.execute("create database data_science")
# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)

# tbl_query = "create table user1(id int AUTO_increment PRIMARY KEY,name text,email text,password text)"
# mycursor.execute(tbl_query)

# mycursor.execute("drop table user")

# mycursor.execute("alter table user add column rating text")

insert_query = f"insert into user(name,email,password)values(%s,%s,%s)"
val = ("demdo1","demos4d@gmail.com","dedmso@123")
mycursor.execute(insert_query,val)
mydb.commit()

mycursor.execute("select * from user")
data = mycursor.fetchall()
# mycursor.execute("SHOW tables")
for i in data:
    print(i)








