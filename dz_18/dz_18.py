import mysql.connector
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='Byrchi1994',
#     database= 'pds_07'
# )

mycursor1 = mydb.cursor()
mycursor1.execute("CREATE DATABASE my_first_bd")

##################################################################################

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Byrchi1994',
    database= 'my_first_bd'
)

mycursor2 = mydb.cursor()
mycursor2.execute("CREATE TABLE student (id INT, name VARCHAR(255))")
print('Table created')
##################################################################################

mycursor3 = mydb.cursor()
mycursor3.execute("CREATE TABLE employess (id INT AUTO_INCREMENT PRIMARY KEY,"
                 "name VARCHAR(255), salary INT(6))")
print('Table created')

##################################################################################

mycursor4 = mydb.cursor()
mycursor4.execute("ALTER TABLE student ADD PRIMARY KEY (id)")
print('Changes made')

##################################################################################
sql1 = "INSERT INTO student (id, name) VALUES(%s, %s)"
val1 = [( 1, 'John')]

mycursor5_1 = mydb.cursor()
mycursor5_1.executemany(sql1, val1)
mydb.commit()
print('it was inserted')

##################################################################################
sql2 = "INSERT INTO employess (id, name , salary) VALUES(%s, %s, %s)"
val2 = [( 1, 'John', 10000)]

mycursor5_2 = mydb.cursor()
mycursor5_2.executemany(sql2, val2)
mydb.commit()
print('it was inserted')




