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
# val = ("demdo1","demos4d@gmail.com","dedmso@123")
data =  [
    ("Emma Johnson", "emma.johnson01@example.com", "emma.johnso"),
    ("Liam Smith", "liam.smith02@example.com", "liam.smith0"),
    ("Olivia Brown", "olivia.brown03@example.com", "olivia.brown0"),
    ("Noah Davis", "noah.davis04@example.com", "noah.davis0"),
    ("Ava Miller", "ava.miller05@example.com", "ava.miller"),
    ("Isabella Wilson", "isabella.wilson06@example.com", "isabella.wilson"),
    ("Mason Moore", "mason.moore07@example.com", "mason.moore0"),
    ("Sophia Taylor", "sophia.taylor08@example.com", "sophia.taylor"),
    ("Ethan Anderson", "ethan.anderson09@example.com", "ethan.anders"),
    ("Mia Thomas", "mia.thomas10@example.com", "mia.thomas"),
    ("James Jackson", "james.jackson11@example.com", "james.jackso"),
    ("Charlotte White", "charlotte.white12@example.com", "charlotte.white1"),
    ("Benjamin Harris", "benjamin.harris13@example.com", "benjamin.harris"),
    ("Amelia Clark", "amelia.clark14@example.com", "amelia.clark1"),
    ("Alexander Lewis", "alexander.lewis15@example.com", "alexander.lewis1"),
    ("Harper Robinson", "harper.robinson16@example.com", "harper.robins"),
    ("Daniel Walker", "daniel.walker17@example.com", "daniel.walker"),
    ("Evelyn Hall", "evelyn.hall18@example.com", "evelyn.hall18"),
    ("Matthew Allen", "matthew.allen19@example.com", "matthew.allen1"),
    ("Lily Young", "lily.young20@example.com", "lily.young2"),
    ("Sebastian King", "sebastian.king21@example.com", "sebastian.king21")
]
# mycursor.execute(insert_query,data)
# mycursor.executemany(insert_query,data)
# mydb.commit()

# mycursor.execute("select * from user ")
# mycursor.execute("select name from user ")
# mycursor.execute("select name from user ")
# data = mycursor.fetchall()
# data = mycursor.fetchone()
# mycursor.execute("SHOW tables")

# where condition
# mycursor.execute("select * from user where name='demo'")
# mycursor.execute("select * from user where name like '%%demo' ")
# mycursor.execute("select * from user where name like 'demo%%' ")
# mycursor.execute("select * from user where name like '%%demo%%' ")

# sorting

# mycursor.execute("select * from user order by name")
# mycursor.execute("select * from user order by name desc")
# data = mycursor.fetchall()
# for i in data:
#     print(i)

#delete the data 
# mycursor.execute("delete from user where name='demo'")
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# drow the table
# mycursor.execute("drop table user1")
# mycursor.execute("show tables")
# for i in mycursor:
#     print(i)

#update the table 

# mycursor.execute("update user set name='Raj' where id=4")
# mydb.commit()

# mycursor.execute("select * from user where id=4")
# data = mycursor.fetchall()

# for i in data:
#     print(i)


# limit

# mycursor.execute("select * from user limit 5")
# mycursor.execute("select * from user limit 5 offset 6")
# data = mycursor.fetchall()
# for i in data:
#     print(i)


# mycursor.execute("create table product(id int primary key,name text,email text) ")
# val = [( 'fist', 'fist@gmail.com'),
#        ( 'thied', 'thied@gmail.com'),
#        ( 'four', 'four@gmail.com'),
#        ( 'secon','second@gmail.com')
#        ]

# insert_query = f"insert into product(name,email)values(%s,%s)"
# mycursor.executemany(insert_query, val)
# mydb.commit()

# mycursor.execute("select * from product")
# data = mycursor.fetchall()
# for i in data:
#     print(i)


# join 

# sql = "SELECT  user.name AS user,  product.name AS favorite  FROM user  INNER JOIN product ON user.id = product.id"
# sql = "SELECT  user.name AS user,  product.name AS favorite  FROM user  LEFT JOIN product ON user.id = product.id"
# sql = "SELECT  user.name AS user,  product.name AS favorite  FROM user  RIGHT JOIN product ON user.id = product.id"
mycursor.execute(sql)
data = mycursor.fetchall()

for i in data: 
    print(i)
